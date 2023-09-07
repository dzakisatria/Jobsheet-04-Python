# Program ini digunakan untuk menentukan angka terbesar dari dua angka

# Fungsi angka_terbesar menerima dua angka sebagai input dan mengembalikan angka terbesar
def angka_terbesar(angka1, angka2):
    # Tambahkan kode di sini
    if angka1 < angka2:
    # angka1 lebih dari angka2 berarti angka1 terbesar
        print("Angka terbesar adalah",angka2)
    elif angka1 > angka2:
    # angka2 lebih dari angka1 berarti angka2 terbesar
        print("Angka terbesar adalah",angka1)
    else:
    # jika angka kedua duanya sama maka dinyatakan sama
        print("Angka sama")
    pass

# Gunakan fungsi input untuk menentukan angka 1 dan 2
angka1 = int(input("Masukan Angka pertama: "))
angka2 = int(input("Masukan Angka kedua: "))
angka_terbesar(angka1, angka2)
# Panggil fungsi angka_terbesar untuk menentukan angka terbesar
