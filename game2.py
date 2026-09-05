# 1. Import
import random
import time

# 2. Judul game
time.sleep(1)
print("•" * 50)
time.sleep(1)
print("     GAME PETUALANGAN TEKS RPG SEDERHANA")
time.sleep(1)
print("•" * 50)
time.sleep(1)

# 3. Variabel
status_hero_harley = {
    "nama" : "harley",
    "darah" : 100,
    "senjata" : "tongkat",
    "heal" : 3
}

status_hero_alucard = {
    "nama" : "alucard",
    "darah" : 120,
    "senjata" : "pedang",
    "heal" : 3
}

status_hero_lancelot = {
    "nama" : "lancelot",
    "darah" : 110,
    "senjata" : "pedang",
    "heal" : 3
}


# 4. Loop game
while True:
    print(f"\nSilahkan pilih menu berikut ini👇")
    time.sleep(1)
    print(f"\n1.Bermain")
    time.sleep(1)
    print(f"2.keluar")
    time.sleep(1)
    pilihan = int(input(f"\npilih menu (1/2): "))
    time.sleep(1)

    if pilihan == 1:
        time.sleep(1)

        # Variabel pilihan game
        serang_musuh = random.randint(10,25)
        serang_player = random.randint(10,20)
        player_heal = random.randint(20,40)
        darah_musuh = 100
        status_hero = status_hero_harley

        while True:

            print(f"\nSilahkan pilih opsi berikut👇")
            time.sleep(1)
            print(f"\n1.Serang musuh")
            time.sleep(1)
            print(f"2.gunakan heal")
            time.sleep(1)
            print(f"3.Mundur")
            time.sleep(1)
            print(f"4.lihat status hero")
            time.sleep(1)
            aksi = int(input(f"\nMasukan pilihan (1/2/3/4): "))
            time.sleep(1)

            if aksi == 1:
                time.sleep(1)

                # Variabel aksi 1
                serang_musuh = random.randint(10,25)
                serang_player = random.randint(10,20)
                print(f"\nkamu menyerang musuh sebesar: {serang_musuh}")
                time.sleep(1)
                print(f"\nMusuh menyerang balik sebesar: {serang_player}")
                time.sleep(1)

                status_hero["darah"] -= serang_musuh
                darah_musuh -= serang_player
                print(f"\nDarah kamu: {status_hero["darah"]}  |  darah musuh: {darah_musuh}")

                if darah_musuh <= 0:
                    print(f"Anda menang!")
                    time.sleep(1)
                    break
                if status_hero["darah"] <= 0:
                    print(f"Anda kalah!")
                    time.sleep(1)
                    break

            elif aksi == 2:

                if status_hero["heal"] <= 0:
                    print(f"\nHeal habis!")
                    time.sleep(1)
                    continue

                status_hero["darah"] += player_heal
                print(f"\nkamu menggunakan heal sebesar: {player_heal}")
                time.sleep(1)
                status_hero["heal"] -= 1
                print(f"\ndarah kamu tersisa: {status_hero["darah"]}")
                time.sleep(1)
                print(f"\nheal = {status_hero["heal"]}")
                time.sleep(2)

            elif aksi == 3:

                print(f"kamu mundur dulu untuk memulihkan HP")
                time.sleep(1)

                while True:

                    print(f"Silahkan pilih: ")
                    print(f"\n1.Kembali maju menyerang musuh")
                    print(f"2.Ganti hero")
                    print(f"3.Ganti senjata")
                    pilihan_mundur = int(input(f"\nmasukan pilihan: "))

                    if pilihan_mundur == 1:
                        break

                    elif pilihan_mundur == 2:

                        print(f"\nSilahkan pilih mau ganti ke hero mana")
                        print(f"\n1.hero harley")
                        print(f"2.hero alucard")
                        print(f"3.hero lancelot")

                        pilihan_hero = int(input(f"\nSilahkan pilih (1/2/3): "))

                        if pilihan_hero == 1:
                            status_hero = status_hero_harley

                        elif pilihan_hero == 2:
                            status_hero = status_hero_alucard

                        elif pilihan_hero == 3:
                            status_hero = status_hero_lancelot

                            print(f"\nHero anda saat ini adalah: {status_hero}")

            elif aksi == 4:

                print(f"\n==== STATUS HERO ====")
                time.sleep(1)
                print(f"\nNama    : {status_hero["nama"]}")
                time.sleep(1)
                print(f"Darah   : {status_hero["darah"]}")
                time.sleep(1)
                print(f"Senjata : {status_hero["senjata"]}")
                time.sleep(1)
                print(f"heal    : {status_hero["heal"]}")
                time.sleep(1)

    elif pilihan == 2:

        print("\nSampai jumpa lagi!\n")
        time.sleep(1)
        break

    else:
        print(f"Input salah! silahkan pilih input yg benar!")
