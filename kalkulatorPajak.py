# Program ini digunakan untuk menghitung jumlah pajak yang harus dibayar
# def 1
def hitung_pajak(penghasilan):
    # Menghitung pajak tahunan
    hitung = round ((pajaktahun/100) * penghasilan)
    return hitung
# def 2 parameter sama kayak def 1
def jadiperbulan(penghasilan):
    # hitung perbulan harus bayar berapa(perbulan = tulis def 1 dibagi 12)
    perbulan = round(hitung_pajak(penghasilan)/12)
    return perbulan

# Fungsi hitung_pajak menerima penghasilan sebagai input dan mengembalikan jumlah pajak
    # Tambahkan kode di sini
# Masukan Penghasilan mu setiap gajian
penghasilan = int(input("Masukan Penghasilan: "))
# Masukan pajak tiap tahun di daerah mu
pajaktahun = int(input('Masukan pajak tahunan (%): '))

# Hasil yang ditampilkan
hasil = hitung_pajak(penghasilan)
print("Jadi, pajak penghasilan per tahun yang harus Anda setor ke negara" ,pajaktahun,"% adalah",hasil)
bulan = jadiperbulan(penghasilan)
print("Perbulannya bayar", bulan)
pass

# Gunakan fungsi hitung_pajak untuk menghitung jumlah pajak dari penghasilan berikut
# Panggil fungsi hitung_pajak untuk menghitung jumlah pajak yang harus dibayar
