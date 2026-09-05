# 1. Import
import random
import time

# 2. Judul game
time.sleep(1)
print("~" * 50)
print("               GAME TEBAK ANGKA ")
print("~" * 50)
time.sleep(1.5)

# 3. Variabel
angka_rahasia = random.randint(1,10)
percobaan = 0

# 4. Loop game
while True:
    print("\nSilahkan pilih menu berikut👇")
    time.sleep(1)
    print(f"\n1.Bermain game")
    time.sleep(1)
    print(f"2.Keluar")
    time.sleep(1)
    pilihan = input(f"\nPilih menu (1/2): ")
    time.sleep(1)

    if pilihan == "1":
        time.sleep(1)

        angka_rahasia = random.randint(1,10)

        while True:
            tebakan = int(input("\nMasukan angka (1-10): "))
            time.sleep(1)

            if tebakan == angka_rahasia:
                print(f"\nSelamat, anda menang!\n")
                time.sleep(1)
                percobaan += 1
                print(f"percobaan = {percobaan}")
                percobaan = 0
                time.sleep(1)
                break
            elif tebakan > angka_rahasia:
                print(f"\nAngka terlalu besar!\n")
                time.sleep(1)
                percobaan += 1
                print(f"percobaan = {percobaan}")
                time.sleep(1)
            elif tebakan < angka_rahasia:
                print(f"\nAngka terlalu kecil!")
                time.sleep(1)
                percobaan += 1
                print(f"\npercobaan = {percobaan}")
                time.sleep(1)

    elif pilihan == "2":
        print(f"\nSelamat tinggal👍\n")
        time.sleep(1)
        break

    else:
        print(f"\ninput salah!\n")





