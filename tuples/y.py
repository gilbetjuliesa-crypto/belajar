def reconcile_cache(server_a, server_b):
    identik = set()
    konflik = set()
    unik_a = set()
    unik_b = set()

    x = set(server_a.keys())
    y = set(server_b.keys())

    z = x & y
    for a in z:
        if server_a[a] == server_b[a]:
            identik.add(a)
        else:
            konflik.add(a)


    unik_a = x - y
    unik_b = y - x

    format = {'identik': identik, 'konflik': konflik, 'unik_a': unik_a, 'unik_b': unik_b}

    print(format)


a, b = eval(input()), eval(input())
reconcile_cache(a, b)