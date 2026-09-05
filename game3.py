# 1.Bagian awal

import random
import time

# 2.Judul game

time.sleep(1)
print("=" * 53)
time.sleep(1)
print("           GAME TARUHAN TEBAK DADU KW")
time.sleep(1)
print("=" * 53)
time.sleep(1)

# 3.Variabel

dadu = random.randint(1,6)
uang = 100000

# 4.Loop game

while True:

    print(f"\nSilahkan pilih menu berikut")
    time.sleep(1)
    print(f"\n1.Bermain")
    time.sleep(1)
    print(f"simpan uang")
    time.sleep(1)
    print(f".Keluar")
    time.sleep(1)

    pilihan = int(input(f"\nmasukan pilihan anda: "))
    time.sleep(1)

    if pilihan == 1:
        time.sleep(1)

        dadu = random.randint(1,6)

        print(f"\nuang anda: {uang}")
        time.sleep(1)
        taruhan = int(input(f"\nMasukan taruhan anda: "))
        time.sleep(1)

        if taruhan > uang:
            print(f"\nUang anda tidak cukup!")
            continue

        else:
            print(f"\nuang anda: {uang}")
            tebakan = int(input(f"\nMasukan tebakan anda (1-6): "))
            time.sleep(1)

            if tebakan == dadu:
                print(f"\nSelamat! Anda benar!")
                time.sleep(1)
                uang += taruhan
                print(f"\nUang anda: {uang}")
                time.sleep(1)

            elif tebakan < dadu:
                print(f"\nAnda salah!")
                time.sleep(1)
                uang -= taruhan
                print(f"\nUang anda: {uang}")
                time.sleep(1)

            elif tebakan > dadu:
                print(f"\ntebakan anda salah!")
                time.sleep(1)
                print(f"\nangka dadu yg benar adalah: {dadu}")
                time.sleep(1)
                uang -= taruhan
                print(f"\nuang anda tersisa {uang}")

            elif uang <= 0:
                print(f"\nuang ada habis!")
                break

    elif pilihan == 2:
        print(f"\nselamat tinggal!\n")
        break

