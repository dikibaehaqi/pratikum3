baris = 10
kolom = 10

for bar in range(baris):
    for kol in range(kolom):
        tab = bar+kol
        print("{0:>6}".format(tab), end='')
    print()