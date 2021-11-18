x=100000000
sum=0
a=0 
laba=[ int(0), int(0), int(x)*.01, int(x)*.01, int(x)*.05, int(x)*.05, int(x)*.05, int(x)*.03]
print("Modal awal pengusaha :", x )
for i in laba :
    sum=sum+i
    a+=1 
    print('laba bulan ke - ', a , 'sebesar:', i)

print('Total laba yang didapat adalah:', sum)