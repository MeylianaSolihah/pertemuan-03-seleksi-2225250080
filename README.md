# Pertemuan 03 Seleksi Python

Nama: Meyliana Solihah
NIM: 2225250080
Kelas: 2225250080

## Tujuan

Menulis program seleksi if, if-else, kondisi majemuk, dan nested if.

## Cara Menjalankan

python latihan/01_genap_ganjil.py
python latihan/02_bandingkan_dua_bilangan.py
python latihan/03_kelulusan_bersyarat.py
python latihan/04_jenis_segitiga.py
python tugas/analisis_persamaan_kuadrat.py

## Algoritma Tugas

1. Membaca nilai a, b, dan c sebagai float.
2. Memeriksa apakah nilai a sama dengan 0.
3. Jika a sama dengan 0, tampilkan bahwa input bukan persamaan kuadrat.
4. Jika a tidak sama dengan 0, hitung diskriminan dengan rumus:

   D = b² - 4ac

5. Jika D > 0, hitung dan tampilkan dua akar real yang berbeda.
6. Jika D = 0, hitung dan tampilkan satu akar real kembar.
7. Jika D < 0, tampilkan bahwa tidak ada akar real.

## Hasil Pengujian

| No | a | b | c | D | Hasil yang Diharapkan | Status |
|---|---:|---:|---:|---:|---|---|
| 1 | 1 | -5 | 6 | 1.00 | Dua akar real: 3 dan 2 | Berhasil |
| 2 | 1 | 2 | 1 | 0.00 | Akar kembar: -1 | Berhasil |
| 3 | 1 | 0 | 1 | -4.00 | Tidak ada akar real | Berhasil |
| 4 | 0 | 2 | 3 | - | Bukan persamaan kuadrat | Berhasil |

## Refleksi

Pada tugas ini saya belajar menggunakan nested if untuk menentukan kondisi berdasarkan nilai diskriminan.

Saya juga belajar bahwa nilai diskriminan menentukan jenis akar persamaan kuadrat. Selain itu, saya belajar pentingnya menguji beberapa test case, termasuk ketika a = 0, D > 0, D = 0, dan D < 0.

Salah satu kesalahan logika yang perlu diperhatikan adalah ketika a = 0 tetapi program tetap menghitung diskriminan atau akar. Kesalahan tersebut dapat diperbaiki dengan memeriksa kondisi a == 0 terlebih dahulu sebelum menghitung diskriminan.