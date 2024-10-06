import math
while True:
    print("\n=====Selamat Datang di Program Mencari Akar Persamaan Kuadrat dan Determinan=====")
    A = int(input("Masukkan nilai A: "))
    B = int(input("Masukkan nilai B: "))
    C = int(input("Masukkan nilai C: "))
    print(f"Persamaan kuadrat {int(A)}x^2 + {int(B)}x + {int(C)}")
    if A == 0:
        print("Bukan merupakan persamaan kuadrat, karena nilai A = 0")
    else:
        D = B**2 - 4*A*C
        print(f"Determinan = {int(D)}")
        if D > 0:
            x1 = (-B + math.sqrt(D)) / (2*A)
            x2 = (-B - math.sqrt(D)) / (2*A)
            x1 = int(x1)
            x2 = int(x2)
            print("Memiliki Akar Berbeda")
            print(f"Akar x1 = {x1}")
            print(f"Akar x2 = {x2}")
        elif D == 0:
            x = -B / (2*A)
            x = int(x)  
            print("Merupakan Akar Kembar")
            print(f"Akar = {x}")
        else:
            real_part = -B / (2*A)
            imag_part = math.sqrt(abs(D)) / (2*A)
            real_part = int(real_part)  
            imag_part = int(imag_part)  
            print("Merupakan Akar Imajiner")
            print(f"Akar x1 = {real_part} + {imag_part}i")
            print(f"Akar x2 = {real_part} - {imag_part}i")
    #repeat
    ulang = input("\nApakah Anda ingin menghitung lagi? (y/n): ").lower()
    if ulang != 'y':
        print("Terima kasih telah menggunakan program ini!")
        break
