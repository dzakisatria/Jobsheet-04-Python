# Program ini digunakan untuk mencari data dalam daftar

# Fungsi cari_data menerima daftar dan data yang ingin dicari sebagai input
def cari_data(data_mahasiswa, target):
    # Tambahkan kode di sini
    if target in data_mahasiswa :
        return f"{target} ditemukan dalam list."
    else : 
        return f"{target} tidak ditemukan dalam list."


# Gunakan fungsi cari_data untuk mencari data dalam daftar berikut
data_mahasiswa = ["alice", "bob", "charlie", "david"]
target = input("Masukan nama mahasiswa: ")
# Panggil fungsi cari_data untuk mencari data_yang_dicari dalam data_mahasiswa
hasil = cari_data(data_mahasiswa, target)
print(hasil)