def nilai():
    data=[]
    if data == [] :
        data1  = int(input("Masukkan Nilai Pertama\t\t: "))
        data2  = int(input("Masukkan Nilai Kedua\t\t: "))
    else :
        print("Terima Kasih");

    data=[data1,data2] 
    nilai_terbesar = max(data)
    print("Nilai Terbesar Dari 2 Nilai Diatas Adalah " ,nilai_terbesar)
nilai()
