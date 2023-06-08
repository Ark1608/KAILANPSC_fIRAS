jenis_bahan = ["MPPF Foam","Control Horn","Push Rod Wire","Brushless Motor","Linkage stopper","ESC(SWSOA)","Receiver (LA108 RX)","Carbon fiber rod","Servo 9g","RC LIPO battery","Propeller","FLYSKY-16X Remote control"]
harga_bahan = [3,2,15.79,12,67,61,25.30,5.20,57.56,5.50,161]
jumlah = [0,1,2,3,4,5,6,7,8,9,10,11]

print("HARGA MPPF Foam-RM3,HARGA Control Horn-RM3,HARGA Push Rod Wire-RM2,HARGA Brushless Motor-RM15.79,HARGA Linkage stopper-RM12,HARGA ESC(SWSOA)-RM67,HARGA Receiver (LA108 RX)-RM61,HARGA Carbon fiber rod-RM25.30,HARGA Servo 9g-RM5.20,HARGA RC LIPO battery-RM57.56,HARGA Propeller-RM5.50,HARGA FLYSKY-16X Remote control")
a=int(input("\nMasukkan tempahan untuk MPPF Foam:"))
b=int(input("Masukkan tempahan untuk Control Horn:"))
c=int(input("Masukkan tempahan untuk Push Rod Wire:"))
d=int(input("Masukkan tempahan untuk Brushless Motor:"))
e=int(input("Masukkan tempahan untuk Linkage stopper:"))
f=int(input("Masukkan tempahan untuk ESC(SWSOA):"))
g=int(input("Masukkan tempahan untuk Receiver (LA108 RX):"))
h=int(input("Masukkan tempahan untuk Carbon fibre rod:"))
i=int(input("Masukkan tempahan untuk Servo 9g:"))
j=int(input("Masukkan tempahan untuk RC LIPO battery:"))
k=int(input("Masukkkan tempahan untuk Propeller:"))
l=int(input("Masukkan tempahan untuk FLYSKY-16X Remote control:"))

tempahan = (a,b,c,d,e,f,g,h,i,j,k,l)

def jumlah_harga():
    for i in range(4):
        jumlah[i] = harga_bahan[i]*tempahan[i]
    return(jumlah)

def cetak():
    print("\n\nTempahan anda ialah:")
    print(a,"bahan", jenis_bahan[0])
    print(b,"bahan", jenis_bahan[1])
    print(c,"bahan", jenis_bahan[2])
    print(d,"bahan", jenis_bahan[3])
    print(e,"bahan", jenis_bahan[4])
    print(f,"bahan", jenis_bahan[5])
    print(g,"bahan", jenis_bahan[6])
    print(h,"bahan", jenis_bahan[7])
    print(i,"bahan", jenis_bahan[8])
    print(j,"bahan", jenis_bahan[9])
    print(k,"bahan", jenis_bahan[10])
    print(l,"bahan", jenis_bahan[11])
    
    print("\n Jumlah harga untuk tempahan ialah RM",sum (jumlah))
jumlah_harga()
cetak()