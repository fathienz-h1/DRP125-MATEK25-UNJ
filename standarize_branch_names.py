from pathlib import Path
import pandas as pd

# membaca data hasil tahap sebelumnya
df = pd.read_csv(Path("data") / "patientinfo_bersih_1.csv")

# ========== STANDARISASI SPASI & FORMAT HURUF ==========

kolom_kategori = [
    "sex",
    "age",
    "country",
    "province",
    "city",
    "infection_case",
    "state",
]

# 1. Hapus spasi berlebih dan samakan format huruf dengan str.title()
for kolom in kolom_kategori:
  df[kolom] = df[kolom].astype("string").str.strip().str.title()

# 2. Perbaiki kasus khusus yang kurang pas setelah str.title()
# Kembalikan label dekade usia agar tetap huruf kecil 's' (misal '20S' -> '20s')
df["age"] = df["age"].str.replace(r"^(\d+)S$", r"\1s", regex=True)

# 3. Simpan hasil file
output_dir = Path("data")
output_dir.mkdir(parents=True, exist_ok=True)
df.to_csv(output_dir / "patientinfo_bersih_2.csv", index=False)

print(
    "Standarisasi selesai. File tersimpan di:",
    output_dir / "patientinfo_bersih_2.csv",
)