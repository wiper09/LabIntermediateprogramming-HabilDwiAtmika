import random

# Variabel global untuk menyimpan skor
menang = 0
kalah = 0

# Daftar kata rahasia
kata_rahasia = [
    "python", "komputer", "pemrograman", "algoritma", "database",
    "jaringan", "internet", "aplikasi", "pengembangan", "pembelajaran"
]

def main():
    global menang, kalah
    
    while len(kata_rahasia) > 0:
        kata = pilih_kata()
        if main_hangman(kata):
            menang += 1
        else:
            kalah += 1
        
        print(f"\nSkor saat ini: Menang {menang}, Kalah {kalah}")
        
        if not main_lagi():
            break
    
    if len(kata_rahasia) == 0:
        print("Semua kata telah digunakan. Permainan berakhir.")
    
    print(f"\nSkor akhir: Menang {menang}, Kalah {kalah}")
    print("Terima kasih telah bermain!")

def pilih_kata():
    kata = random.choice(kata_rahasia)
    kata_rahasia.remove(kata)
    return kata

def main_hangman(kata):
    tebakan = set()
    kesempatan = 6
    
    while kesempatan > 0:
        print_kata(kata, tebakan)
        print(f"Kesempatan tersisa: {kesempatan}")
        
        huruf = input("Tebak sebuah huruf: ").lower()
        if len(huruf) != 1 or not huruf.isalpha():
            print("Masukkan satu huruf saja!")
            continue
        
        if huruf in tebakan:
            print("Anda sudah menebak huruf ini!")
            continue
        
        tebakan.add(huruf)
        
        if huruf in kata:
            print("Tebakan benar!")
            if set(kata) <= tebakan:
                print(f"Selamat! Anda menebak kata '{kata}'")
                return True
        else:
            print("Tebakan salah!")
            kesempatan -= 1
    
    print(f"Maaf, Anda kehabisan kesempatan. Kata yang benar adalah '{kata}'")
    return False

def print_kata(kata, tebakan):
    for huruf in kata:
        if huruf in tebakan:
            print(huruf, end=" ")
        else:
            print("_", end=" ")
    print()

def main_lagi():
    while True:
        jawaban = input("Apakah Anda ingin bermain lagi? (y/n): ").lower()
        if jawaban in ['y', 'n']:
            return jawaban == 'y'
        print("Masukkan 'y' untuk ya atau 'n' untuk tidak.")

if __name__ == "__main__":
    main()