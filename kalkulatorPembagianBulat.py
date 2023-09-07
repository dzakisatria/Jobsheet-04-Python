# Program ini digunakan untuk menghitung pembagian bulat dua angka

# Fungsi pembagian_bulat menerima dua angka sebagai input dan mengembalikan hasil pembagian bulat
def pembagian_bulat(angka1, angka2):
    bagi = round (angka1/angka2)
    return bagi
    # Tambahkan kode di sini
    pass

# Gunakan fungsi pembagian_bulat untuk menghitung pembagian bulat dari dua angka berikut
angka1 = int(input("Masukan angka pertama:"))
angka2 = int(input("Masukan angka kedua:"))
hasil = pembagian_bulat(angka1, angka2)
print(hasil)
# Panggil fungsi pembagian_bulat untuk menghitung hasil pembagian bulat
