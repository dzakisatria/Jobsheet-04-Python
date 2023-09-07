# Program ini digunakan untuk menentukan apakah sebuah kata adalah palindrom

# Fungsi cek_palindrom menerima sebuah kata sebagai input dan mengembalikan hasil
def cek_palindrom(kata):
    # Tambahkan kode di sini
    if kata == kata [::-1]:
        print("itu kata palindrom")
    else:
        print("itu bukan kata palindrom")
    pass

# Gunakan fungsi cek_palindrom untuk menentukan apakah kata berikut adalah palindrom
kata = input("Masukan kata: ")
cek_palindrom(kata)
# Panggil fungsi cek_palindrom untuk menentukan apakah kata adalah palindrom
