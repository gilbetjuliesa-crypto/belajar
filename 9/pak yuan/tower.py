def tower_of_hanoi(n, asal, tujuan, transit):
    if n == 0:
        return
    
    tower_of_hanoi(n-1, asal, transit, tujuan)
    print("Pindah Keping", n, "dari", asal, "ke", tujuan)
    tower_of_hanoi(n-1, transit, tujuan, asal)

# bagian utama program
n = 4
tower_of_hanoi(n, 'A', 'C', 'B')