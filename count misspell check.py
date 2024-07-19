# Impor modul yang diperlukan
from collections import Counter

# Fungsi untuk membaca file dan mengembalikan list kata-kata
def baca_file(nama_file):
    with open(nama_file, 'r', encoding='utf-8') as file:
        return file.read().lower().split()

# Fungsi untuk menghitung kata dan kata unik
def hitung_kata(kata_kata):
    jumlah_kata = len(kata_kata)
    jumlah_kata_unik = len(set(kata_kata))
    return jumlah_kata, jumlah_kata_unik

# Fungsi untuk menemukan kata yang salah eja
def temukan_kata_salah_eja(kata_kata, kata_kata_benar):
    return [kata for kata in set(kata_kata) if kata not in kata_kata_benar]

# Program utama
def main():
    # Baca file teks
    kata_kata_alice = baca_file("alice.txt")
    
    # Hitung kata dan kata unik
    jumlah_kata, jumlah_kata_unik = hitung_kata(kata_kata_alice)
    print(f"Jumlah kata: {jumlah_kata}")
    print(f"Jumlah kata unik: {jumlah_kata_unik}")
    
    # Baca file kata-kata yang benar
    kata_kata_benar = set(baca_file("words.txt"))
    
    # Temukan kata yang salah eja
    kata_salah_eja = temukan_kata_salah_eja(kata_kata_alice, kata_kata_benar)
    print(f"Jumlah kata yang salah eja: {len(kata_salah_eja)}")
    print("Kata-kata yang salah eja:")
    for kata in kata_salah_eja:
        print(kata)

if __name__ == "__main__":
    main()