A=int(input("Masukkan nilai A = "))
B=int(input("Masukkan nilai B = "))
C=int(input("Masukkan nilai C = "))

if A > B and B > C:
    print("Nilai terbesar dari 3 buah bilangan adalah :", A)
elif B > A and B > C:
    print("Nilai terbesar dari 3 buah bilangan adalah :", B)
else:
    print("Nilai terbesar dari 3 buah bilangan adalah :", C)