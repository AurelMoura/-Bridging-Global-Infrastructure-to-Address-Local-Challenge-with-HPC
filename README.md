# -Bridging-Global-Infrastructure-to-Address-Local-Challenge-with-HPC
# Rainfall-Based Flood Early Warning Simulation

## 1. Deskripsi Proyek

Proyek ini merupakan implementasi sederhana dari materi Praktisi Mengajar berjudul *Bridging Global Infrastructure to Address Local Challenge with HPC* yang disampaikan oleh Worawan Diaz Carballo dari Thammasat University, Thailand.

Proyek ini menerapkan pengolahan data menggunakan Python untuk membuat simulasi pengelompokan kondisi berdasarkan curah hujan dan tinggi muka air.

## 2. Tujuan

- Memahami tahapan dasar pengolahan data.
- Memeriksa kualitas dataset.
- Mengolah data curah hujan dan tinggi muka air.
- Membuat kategori kondisi berdasarkan aturan simulasi.
- Menampilkan hasil analisis melalui grafik dan tabel.

## 3. Tools yang Digunakan

- Python 3.13
- Pandas
- Matplotlib
- Visual Studio Code

## 4. Dataset

Dataset yang digunakan merupakan data simulasi selama tujuh hari. Data terdiri dari tanggal, curah hujan dalam milimeter, dan tinggi muka air dalam sentimeter.

Dataset ini dibuat untuk pembelajaran dan bukan data pengamatan resmi.

## 5. Metode

Program melakukan pemeriksaan data, klasifikasi berbasis aturan, serta visualisasi perubahan curah hujan dan tinggi muka air.

Ambang kategori Normal, Waspada, dan Siaga hanya digunakan sebagai ilustrasi pemrograman. Ambang tersebut bukan standar resmi peringatan dini banjir.

## 6. Hasil dan Insight

Hasil simulasi menunjukkan bahwa data dapat dikelompokkan berdasarkan ambang yang ditentukan. Grafik membantu memperlihatkan perubahan curah hujan dan tinggi muka air dari hari ke hari.

Pengolahan data seperti ini dapat menjadi bagian awal dari alur kerja komputasi untuk memahami permasalahan lokal. Namun, proyek ini belum menggunakan infrastruktur HPC dan tidak dapat digunakan untuk menentukan risiko banjir sebenarnya.

## 7. Cara Menjalankan Program

Instal library yang diperlukan:

`python -m pip install pandas matplotlib`

Jalankan program:

`python analisis_banjir.py`

Program akan menampilkan hasil analisis dan grafik, serta menyimpan tabel hasil klasifikasi.

## 8. Kesimpulan

Proyek ini menunjukkan penerapan dasar pengolahan data, klasifikasi berbasis aturan, dan visualisasi menggunakan Python. Tahapan tersebut memperkenalkan alur kerja komputasi yang dapat dikembangkan lebih lanjut untuk penelitian berbasis data.

## 9. Catatan

Seluruh data merupakan simulasi. Hasil klasifikasi tidak boleh digunakan sebagai dasar keputusan keselamatan, evakuasi, atau peringatan banjir nyata.
