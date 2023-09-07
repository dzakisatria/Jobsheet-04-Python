# Program ini digunakan untuk menentukan apakah suatu bilangan adalah genap atau ganjil

# Fungsi cek_genap_ganjil menerima sebuah bilangan sebagai input dan mengembalikan hasil
def cek_genap_ganjil(bilangan):
    # Tambahkan kode di sini
    # jika bilangan di modulus 2 sama dengan 0
    if bilangan % 2 == 0 :
        print(bilangan, "adalah angka genap")
    else:
        print(bilangan, "adalah angka ganjil")
    pass

# Gunakan fungsi cek_genap_ganjil untuk menentukan apakah bilangan berikut adalah genap atau ganjil
bilangan = int(input("Masukan angka: "))
cek_genap_ganjil(bilangan)
# Panggil fungsi cek_genap_ganjil untuk menentukan apakah bilangan adalah genap atau ganjil
