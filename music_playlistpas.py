"""
Music Explorer - Cari lagu / album / artis dan analisis genre
Sumber data : iTunes Search API (gratis, tanpa API key)
Library     : streamlit, pandas, matplotlib, requests

Jalankan:
    uv add streamlit pandas matplotlib requests
    uv run streamlit run music_explorer.py
"""
import json

import matplotlib.pyplot as plt
import pandas as pd
import requests
import streamlit as st
from matplotlib.ticker import MaxNLocator

# ---------------------------------------------------------------
# Konfigurasi & konstanta
# ---------------------------------------------------------------
st.set_page_config(page_title="Music Explorer", page_icon="🎵", layout="wide")

ITUNES_URL = "https://itunes.apple.com/search"

# Dictionary: label tampilan -> nilai parameter `entity` di iTunes API
MODE = {"Lagu": "song", "Album": "album", "Artis": "musicArtist"}

NEGARA = {
    "Indonesia": "ID",
    "Amerika Serikat": "US",
    "Inggris": "GB",
    "Jepang": "JP",
    "Korea Selatan": "KR",
    "Australia": "AU",
}

# Tuple: urutan kolom DataFrame yang konsisten untuk semua mode
KOLOM = (
    "kueri", "artis", "lagu", "album", "genre", "rilis", "tahun",
    "durasi_menit", "harga", "mata_uang", "sampul", "preview", "tautan",
)


# ---------------------------------------------------------------
# Fungsi pengambilan & pengolahan data
# ---------------------------------------------------------------
@st.cache_data(ttl=600, show_spinner=False)
def ambil_data(kueri, entity, negara, limit):
    """Memanggil iTunes Search API. Hasil di-cache 10 menit."""
    params = {
        "term": kueri,
        "media": "music",
        "entity": entity,
        "country": negara,
        "limit": limit,
    }
    resp = requests.get(ITUNES_URL, params=params, timeout=15)
    resp.raise_for_status()
    return resp.json().get("results", [])


def normalisasi(hasil, kueri, mode):
    """Mengubah list dictionary JSON menjadi DataFrame dengan kolom seragam."""
    baris = []
    for r in hasil:
        durasi = r.get("trackTimeMillis")
        baris.append({
            "kueri": kueri,
            "artis": r.get("artistName"),
            "lagu": r.get("trackName") if mode == "Lagu" else None,
            "album": r.get("collectionName"),
            "genre": r.get("primaryGenreName") or "Tidak diketahui",
            "rilis": r.get("releaseDate"),
            "durasi_menit": round(durasi / 60000, 2) if durasi else None,
            "harga": r.get("trackPrice") if mode == "Lagu" else r.get("collectionPrice"),
            "mata_uang": r.get("currency"),
            "sampul": r.get("artworkUrl100"),
            "preview": r.get("previewUrl"),
            "tautan": (r.get("trackViewUrl") or r.get("collectionViewUrl")
                       or r.get("artistLinkUrl")),
        })
    df = pd.DataFrame(baris, columns=list(KOLOM))
    waktu = pd.to_datetime(df["rilis"], errors="coerce", utc=True)
    df["tahun"] = waktu.dt.year.astype("Int64")
    df["rilis"] = waktu.dt.strftime("%Y-%m-%d")
    df["durasi_menit"] = pd.to_numeric(df["durasi_menit"], errors="coerce")
    df["harga"] = pd.to_numeric(df["harga"], errors="coerce")
    return df


def tampilkan(fig):
    """Tampilkan figure Matplotlib di Streamlit lalu tutup agar memori bebas."""
    st.pyplot(fig)
    plt.close(fig)


def ringkasan_genre(df):
    """Groupby genre -> jumlah item, jumlah artis unik, rata-rata durasi & harga."""
    ring = (
        df.groupby("genre")
        .agg(
            jumlah=("genre", "size"),
            artis_unik=("artis", "nunique"),
            rata_durasi_menit=("durasi_menit", "mean"),
            rata_harga=("harga", "mean"),
        )
        .sort_values("jumlah", ascending=False)
        .round(2)
        .reset_index()
    )
    ring["persen"] = (ring["jumlah"] / ring["jumlah"].sum() * 100).round(1)
    return ring


# ---------------------------------------------------------------
# Session state (data tetap ada walau script di-rerun)
# ---------------------------------------------------------------
if "df" not in st.session_state:
    st.session_state["df"] = None
if "mode_aktif" not in st.session_state:
    st.session_state["mode_aktif"] = "Lagu"
if "riwayat" not in st.session_state:
    st.session_state["riwayat"] = []

# ---------------------------------------------------------------
# Sidebar: input pencarian
# ---------------------------------------------------------------
with st.sidebar:
    st.header("🔎 Pencarian")
    mode = st.radio("Cari berdasarkan", list(MODE.keys()), horizontal=True)
    teks = st.text_input("Kata kunci", placeholder="mis. Coldplay, Tulus, Dewa 19")
    st.caption("Pisahkan dengan koma untuk **membandingkan** beberapa artis/kata kunci (maks. 5).")
    negara_label = st.selectbox("Toko iTunes (negara)", list(NEGARA.keys()))
    limit = st.slider("Jumlah hasil per kata kunci", 10, 200, 50, 10)
    cari = st.button("Cari", type="primary")

    if st.session_state["riwayat"]:
        st.divider()
        st.caption("Riwayat pencarian terakhir:")
        for item in st.session_state["riwayat"][-5:][::-1]:
            st.write(f"• {item}")

# ---------------------------------------------------------------
# Proses pencarian
# ---------------------------------------------------------------
if cari:
    # dict.fromkeys -> hapus duplikat sambil menjaga urutan
    daftar_kueri = list(dict.fromkeys(k.strip() for k in teks.split(",") if k.strip()))[:5]
    if not daftar_kueri:
        st.sidebar.error("Masukkan kata kunci terlebih dahulu.")
    else:
        kumpulan = []
        try:
            with st.spinner("Mengambil data dari iTunes..."):
                for k in daftar_kueri:
                    hasil = ambil_data(k, MODE[mode], NEGARA[negara_label], limit)
                    kumpulan.append(normalisasi(hasil, k, mode))
            df_baru = pd.concat(kumpulan, ignore_index=True)
            st.session_state["df"] = df_baru
            st.session_state["mode_aktif"] = mode
            st.session_state["riwayat"].append(f"{mode}: {', '.join(daftar_kueri)}")
        except requests.RequestException as e:
            st.error(f"Gagal mengambil data dari iTunes API: {e}")

# ---------------------------------------------------------------
# Halaman utama
# ---------------------------------------------------------------
st.title("🎵 Music Explorer")
st.caption("Cari lagu, album, atau artis lalu analisis sebaran genre-nya • Data: iTunes Search API")

df_all = st.session_state["df"]

if df_all is None:
    st.info("Masukkan kata kunci di sidebar lalu klik **Cari** untuk memulai.")
    st.stop()

if df_all.empty:
    st.warning("Tidak ada hasil. Coba kata kunci lain atau ganti negara toko iTunes.")
    st.stop()

mode_aktif = st.session_state["mode_aktif"]

# Filter genre global (berlaku untuk semua tab)
with st.sidebar:
    st.divider()
    st.header("🎚️ Filter")
    pilih_genre = st.multiselect("Genre", options=sorted(set(df_all["genre"])))

df = df_all[df_all["genre"].isin(pilih_genre)] if pilih_genre else df_all
if df.empty:
    st.warning("Tidak ada data untuk filter yang dipilih.")
    st.stop()

# Ringkasan metrik
c1, c2, c3, c4 = st.columns(4)
c1.metric(f"Jumlah {mode_aktif.lower()}", len(df))
c2.metric("Artis unik", df["artis"].nunique())
c3.metric("Genre unik", df["genre"].nunique())
rata_durasi = df["durasi_menit"].mean()
c4.metric("Rata-rata durasi", f"{rata_durasi:.2f} mnt" if pd.notna(rata_durasi) else "-")

tab1, tab2, tab3, tab4 = st.tabs(["📋 Hasil", "🎼 Analisis Genre", "📊 Statistik", "💾 Ekspor"])

# ---------------------------------------------------------------
# Tab 1: Hasil pencarian
# ---------------------------------------------------------------
with tab1:
    st.subheader("Hasil Pencarian")
    kolom_tampil = ["sampul", "artis", "lagu", "album", "genre", "rilis",
                    "durasi_menit", "harga", "mata_uang", "kueri", "tautan"]
    kolom_tampil = [k for k in kolom_tampil if df[k].notna().any()]
    st.dataframe(
        df[kolom_tampil],
        column_config={
            "sampul": st.column_config.ImageColumn("Sampul"),
            "tautan": st.column_config.LinkColumn("Buka di iTunes", display_text="Buka"),
            "durasi_menit": st.column_config.NumberColumn("Durasi (mnt)", format="%.2f"),
        },
        hide_index=True,
    )

    if mode_aktif == "Lagu":
        dg = df.dropna(subset=["preview"]).reset_index(drop=True)
        if not dg.empty:
            st.subheader("🎧 Preview 30 detik")
            opsi = [f"{r.lagu} — {r.artis}" for r in dg.itertuples()]
            idx = st.selectbox("Pilih lagu", range(len(opsi)), format_func=lambda i: opsi[i])
            kiri, kanan = st.columns([1, 4])
            with kiri:
                if pd.notna(dg.loc[idx, "sampul"]):
                    st.image(dg.loc[idx, "sampul"], width=150)
            with kanan:
                st.write(f"**{dg.loc[idx, 'lagu']}**")
                st.write(f"{dg.loc[idx, 'artis']} • {dg.loc[idx, 'album']}")
                st.write(f"Genre: {dg.loc[idx, 'genre']}")
                st.audio(dg.loc[idx, "preview"], format="audio/mp4")

# ---------------------------------------------------------------
# Tab 2: Analisis genre
# ---------------------------------------------------------------
with tab2:
    st.subheader("Sebaran Genre")
    tren = df["genre"].value_counts()
    dominan = tren.index[0]
    persen_dominan = tren.iloc[0] / len(df) * 100

    st.success(
        f"Genre dominan adalah **{dominan}** dengan {tren.iloc[0]} item "
        f"({persen_dominan:.1f}% dari total). Terdapat **{len(tren)}** genre berbeda."
    )

    kiri, kanan = st.columns(2)

    with kiri:
        st.write("### Jumlah per Genre")
        top = tren.head(10).sort_values()  # urut naik agar terbesar di atas pada barh
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.barh(top.index, top.values, color="skyblue", edgecolor="black")
        ax.set_xlabel("Jumlah")
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.grid(axis="x", linestyle="--", alpha=0.5)
        plt.tight_layout()
        tampilkan(fig)

    with kanan:
        st.write("### Proporsi Genre (Top 5)")
        top5 = tren.head(5)
        lainnya = tren.iloc[5:].sum()
        nilai = list(top5.values) + ([lainnya] if lainnya > 0 else [])
        label = list(top5.index) + (["Lainnya"] if lainnya > 0 else [])
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.pie(nilai, labels=label, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
        plt.tight_layout()
        tampilkan(fig)

    # Perbandingan antar kata kunci (hanya jika > 1 kueri)
    if df["kueri"].nunique() > 1:
        st.write("### Perbandingan Genre antar Kata Kunci")
        top_genre = list(tren.head(8).index)
        tabel = pd.crosstab(df["genre"], df["kueri"]).loc[top_genre]
        fig, ax = plt.subplots(figsize=(10, 4))
        tabel.plot(kind="bar", ax=ax, edgecolor="black")
        ax.set_xlabel("Genre")
        ax.set_ylabel("Jumlah")
        ax.tick_params(axis="x", rotation=45)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        ax.grid(axis="y", linestyle="--", alpha=0.5)
        ax.legend(title="Kata kunci")
        plt.tight_layout()
        tampilkan(fig)

    st.write("### Tabel Ringkasan Genre")
    ring = ringkasan_genre(df)
    st.dataframe(ring, hide_index=True)

# ---------------------------------------------------------------
# Tab 3: Statistik (durasi & tahun rilis)
# ---------------------------------------------------------------
with tab3:
    st.subheader("Statistik Numerik")
    ada_durasi = df["durasi_menit"].notna().any()
    ada_tahun = df["tahun"].notna().any()

    if not ada_durasi and not ada_tahun:
        st.info("Mode **Artis** tidak memiliki data durasi/tahun rilis. Coba mode Lagu atau Album.")

    kolA, kolB = st.columns(2)

    with kolA:
        if ada_durasi:
            st.write("### Histogram Durasi")
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.hist(df["durasi_menit"].dropna(), bins=10, color="purple",
                    edgecolor="black", rwidth=0.9)
            ax.set_xlabel("Durasi (menit)")
            ax.set_ylabel("Frekuensi")
            ax.yaxis.set_major_locator(MaxNLocator(integer=True))
            plt.tight_layout()
            tampilkan(fig)

            st.write("### Boxplot Durasi per Genre (Top 5)")
            top_g = list(tren.head(5).index)
            data_box, label_box = [], []
            for g in top_g:
                nilai_g = df.loc[df["genre"] == g, "durasi_menit"].dropna()
                if not nilai_g.empty:
                    data_box.append(nilai_g)
                    label_box.append(g)
            if data_box:
                fig, ax = plt.subplots(figsize=(6, 4))
                ax.boxplot(data_box)
                ax.set_xticklabels(label_box, rotation=30, ha="right")
                ax.set_ylabel("Durasi (menit)")
                ax.grid(axis="y", linestyle="--", alpha=0.5)
                plt.tight_layout()
                tampilkan(fig)

    with kolB:
        if ada_tahun:
            st.write("### Jumlah Rilis per Tahun")
            per_tahun = df.dropna(subset=["tahun"]).groupby("tahun").size().sort_index()
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.plot(per_tahun.index.astype(int), per_tahun.values, marker="o", color="b")
            ax.set_xlabel("Tahun")
            ax.set_ylabel("Jumlah")
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            ax.yaxis.set_major_locator(MaxNLocator(integer=True))
            ax.grid(True, linestyle="--", alpha=0.6)
            plt.tight_layout()
            tampilkan(fig)

        if ada_tahun and ada_durasi:
            st.write("### Scatter: Tahun vs Durasi")
            dsc = df.dropna(subset=["tahun", "durasi_menit"])
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.scatter(dsc["tahun"].astype(int), dsc["durasi_menit"],
                       color="orange", s=60, alpha=0.7, edgecolor="black")
            ax.set_xlabel("Tahun rilis")
            ax.set_ylabel("Durasi (menit)")
            ax.xaxis.set_major_locator(MaxNLocator(integer=True))
            ax.grid(True, linestyle="--", alpha=0.5)
            plt.tight_layout()
            tampilkan(fig)

    if ada_tahun:
        tahun_valid = df["tahun"].dropna().astype(int)
        st.caption(f"Rentang tahun rilis pada data: {tahun_valid.min()} – {tahun_valid.max()}")

# ---------------------------------------------------------------
# Tab 4: Ekspor
# ---------------------------------------------------------------
with tab4:
    st.subheader("Ekspor Data")
    ring = ringkasan_genre(df)

    csv_bytes = df.to_csv(index=False).encode("utf-8")

    ringkasan_json = {
        "mode": mode_aktif,
        "kata_kunci": list(dict.fromkeys(df["kueri"])),
        "total_item": int(len(df)),
        "genre_dominan": str(ring.loc[0, "genre"]),
        "jumlah_per_genre": {str(k): int(v) for k, v in df["genre"].value_counts().items()},
    }
    json_bytes = json.dumps(ringkasan_json, ensure_ascii=False, indent=2).encode("utf-8")

    e1, e2 = st.columns(2)
    with e1:
        st.download_button("Unduh data (CSV)", data=csv_bytes,
                           file_name="music_explorer.csv", mime="text/csv")
    with e2:
        st.download_button("Unduh ringkasan genre (JSON)", data=json_bytes,
                           file_name="ringkasan_genre.json", mime="application/json")

    with st.expander("Lihat pratinjau JSON"):
        st.json(ringkasan_json)