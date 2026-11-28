from pathlib import Path
import pandas as pd

# membaca file data (PatientInfo.csv memakai pemisah koma bawaan, bukan ';')
df = pd.read_csv(Path("data") / "PatientInfo.csv")

# ========== HAPUS DUPLIKAT DATA ==========

# cek duplikat data
jumlah_duplikat_data = df.duplicated().sum()
print(f"jumlah data duplikat = {jumlah_duplikat_data}")
print()

# menghapus duplikat data
df = df.drop_duplicates()

# validasi duplikat data
jumlah_duplikat_data = df.duplicated().sum()
print(f"jumlah data duplikat setelah dilakukan drop_duplicates = {jumlah_duplikat_data}")
print()

# simpan hasil
output_dir = Path("data")
output_dir.mkdir(parents=True, exist_ok=True)
df.to_csv(output_dir / "patientinfo_bersih_1.csv", index=False)