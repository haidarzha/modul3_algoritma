print("Selamat datang di Segitiga Detektor")
#input panjang sisi
while True:
    a = float(input("Masukkan panjang sisi pertama: "))
    b = float(input("Masukkan panjang sisi kedua: "))
    c = float(input("Masukkan panjang sisi ketiga: "))
#tentuin segitiganya
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Segitiga sama sisi")
        elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
            print("Segitiga siku-siku")
        else:
            print("Segitiga sembarang")
    else:
        print("Bukan segitiga")

    print("Terima kasih!")
#repeat ulang segitiga detector
    ulang = input("Apakah ingin mencoba lagi? (y/n): ").lower()
    if ulang != 'y':
        break

print("Terima kasih! Program selesai.")
