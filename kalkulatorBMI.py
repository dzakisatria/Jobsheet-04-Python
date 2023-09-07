# Program ini digunakan untuk menghitung Indeks Massa Tubuh (BMI)

# Fungsi hitung_bmi menerima berat (dalam kilogram) dan tinggi (dalam meter) sebagai input
def hitung_bmi(berat, tinggi):
    # Tambahkan kode di sini
    bmi=berat/(tinggi/100)**2
    print("BMI anda adalah", bmi)

    if bmi >=30:
        print("Menurut WHO Anda Obesitas")
    elif bmi >=25:
        print("Menurut WHO Anda Gemuk")
    elif bmi >=18:
        print("Menurut WHO Anda Normal")
    elif bmi <=18:
        print("Menurut WHO Anda Kurus")
    pass

# Gunakan fungsi hitung_bmi untuk menghitung BMI dari berat dan tinggi berikut
berat = float(input("Masukan berat badan: "))
tinggi = float(input("Masukan tinggi badan: "))
hitung_bmi(berat, tinggi)
# Panggil fungsi hitung_bmi untuk menghitung BMI
