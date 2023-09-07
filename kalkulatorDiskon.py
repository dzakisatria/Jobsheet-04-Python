# Program ini digunakan untuk menghitung harga setelah diskon
def hitung_diskon(hargabarang, persendiskon):
    hitungdiskon = hargabarang * (persendiskon/100)
    hargadiskon = round (hargabarang - hitungdiskon)
    return hargadiskon
# Masukan Harga Barang
hargabarang = int(input("Harga Barang: Rp."))
# Masukan Mau dikasih diskon berapa
persendiskon = int(input('masukan persentase diskon (%): '))
# Persen Diskon (diskon dibagi 100 dahulu lalu dikali harga barang)

# Diskon yang sudah dibagi 100 dan dikali harga barang itu untuk mengurangi harga barang

# Hasil
hasil = hitung_diskon(hargabarang, persendiskon)
print(f"Total Harga Setelah diskon adalah {hasil}")