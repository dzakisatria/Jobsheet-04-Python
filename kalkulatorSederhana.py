# Program ini adalah kalkulator sederhana

# Fungsi penjumlahan menerima dua angka sebagai input dan mengembalikan hasil penjumlahan
def penjumlahan(angka1, angka2):
    # Tambahkan kode di sini
    hasil = angka1 + angka2
    print(hasil)
     #untuk melewati program

# Fungsi pengurangan menerima dua angka sebagai input dan mengembalikan hasil pengurangan
def pengurangan(angka1, angka2):
    # Tambahkan kode di sini
    hasil = angka1 - angka2
    print(hasil)
     #untuk melewati program

# Fungsi perkalian menerima dua angka sebagai input dan mengembalikan hasil perkalian
def perkalian(angka1, angka2):
    # Tambahkan kode di sini
    hasil = angka1 * angka2
    print(hasil)
     #untuk melewati program

# Fungsi pembagian menerima dua angka sebagai input dan mengembalikan hasil pembagian
def pembagian(angka1, angka2):
    # Tambahkan kode di sini
    hasil = angka1 / angka2
    print(hasil)
     #untuk melewati program

inputuser = input("Masukan opsi /,* atau +: ")
inputangka1 = int(input("Masukan angka 1: "))
inputangka2 = int(input("Maukan angka 2: "))
if inputuser == "+":
    penjumlahan(inputangka1, inputangka2)
elif inputuser == "-":
    pengurangan(inputangka1, inputangka2)
elif inputuser == "*":
    perkalian(inputangka1, inputangka2)
elif inputuser == "/":
    pembagian(inputangka1, inputangka2)

# Gunakan fungsi-fungsi ini untuk mengimplementasikan kalkulator sederhana
# Anda perlu mengisi kode di dalam fungsi-fungsi tersebut.