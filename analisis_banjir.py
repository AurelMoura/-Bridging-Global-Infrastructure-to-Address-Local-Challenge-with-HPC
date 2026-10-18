
import pandas as pd
import matplotlib.pyplot as plt

# 1. Membaca dataset
df = pd.read_csv("data_banjir.csv")

# 2. Memeriksa kualitas data
print("=== DATA AWAL ===")
print(df)

print("\n=== PEMERIKSAAN DATA ===")
print("Jumlah data kosong:")
print(df.isnull().sum())

print("\nJumlah data duplikat:", df.duplicated().sum())

# Memastikan kolom numerik berisi angka
df["curah_hujan_mm"] = pd.to_numeric(
    df["curah_hujan_mm"], errors="coerce"
)
df["tinggi_muka_air_cm"] = pd.to_numeric(
    df["tinggi_muka_air_cm"], errors="coerce"
)

# Menghentikan analisis jika ada data yang tidak valid
if df[
    ["tanggal", "curah_hujan_mm", "tinggi_muka_air_cm"]
].isnull().any().any():
    raise ValueError(
        "Ada data kosong atau tidak valid. Periksa CSV."
    )

if (df[["curah_hujan_mm", "tinggi_muka_air_cm"]] < 0).any().any():
    raise ValueError("Nilai curah hujan dan tinggi air tidak boleh negatif.")

# 3. Menentukan kategori simulasi
# Ambang berikut hanya untuk latihan, bukan ambang resmi.
def tentukan_kategori(baris):
    hujan = baris["curah_hujan_mm"]
    air = baris["tinggi_muka_air_cm"]

    if hujan >= 50 or air >= 70:
        return "Siaga"
    elif hujan >= 20 or air >= 40:
        return "Waspada"
    else:
        return "Normal"

df["kategori_simulasi"] = df.apply(
    tentukan_kategori, axis=1
)

# 4. Menampilkan hasil analisis
print("\n=== HASIL ANALISIS ===")
print(df.to_string(index=False))

print("\n=== RINGKASAN KATEGORI ===")
print(df["kategori_simulasi"].value_counts())

# 5. Membuat grafik
fig, axes = plt.subplots(2, 1, figsize=(9, 7))

axes[0].plot(
    df["tanggal"],
    df["curah_hujan_mm"],
    marker="o"
)
axes[0].set_title("Curah Hujan Harian (Simulasi)")
axes[0].set_ylabel("Curah hujan (mm)")
axes[0].grid(True)

axes[1].plot(
    df["tanggal"],
    df["tinggi_muka_air_cm"],
    marker="o"
)
axes[1].set_title("Tinggi Muka Air Harian (Simulasi)")
axes[1].set_ylabel("Tinggi muka air (cm)")
axes[1].set_xlabel("Tanggal")
axes[1].grid(True)

plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("hasil_analisis_banjir.png", dpi=150)
plt.show()

# 6. Menyimpan hasil analisis ke CSV
df.to_csv("hasil_kategori_banjir.csv", index=False)

print("\nGrafik disimpan sebagai hasil_analisis_banjir.png")
print("Hasil tabel disimpan sebagai hasil_kategori_banjir.csv")
