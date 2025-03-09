# Dicoding Collection Dashboard

## Deskripsi Proyek
Proyek ini merupakan dashboard interaktif berbasis Streamlit yang digunakan untuk menganalisis data peminjaman sepeda dari dataset Bike Sharing. Dashboard ini menyediakan berbagai visualisasi untuk memahami pola penggunaan sepeda berdasarkan faktor-faktor seperti cuaca, musim, dan waktu.

## Setup Environment
### Menggunakan Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Menggunakan Shell/Terminal
```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Menjalankan Aplikasi Streamlit
Untuk menjalankan aplikasi, gunakan perintah berikut:
```bash
streamlit run datavisualisasi.py
```

## Dataset
Proyek ini menggunakan dataset dari **Bike Sharing Dataset** yang terdiri dari dua file utama:
1. `day.csv` - Data peminjaman sepeda berdasarkan hari.
2. `hour.csv` - Data peminjaman sepeda berdasarkan jam.

## Fitur Dashboard
- **Visualisasi Tren Peminjaman Sepeda**: Menampilkan tren jumlah peminjaman sepeda berdasarkan waktu.
- **Analisis Faktor Cuaca**: Menunjukkan bagaimana cuaca mempengaruhi jumlah peminjaman.
- **Distribusi Peminjaman Berdasarkan Musim**: Menunjukkan pola penggunaan sepeda di berbagai musim.

## Contoh Visualisasi
Tangkapan layar berikut menunjukkan contoh visualisasi dari dashboard:
![Dashboard Preview]
![image](https://github.com/user-attachments/assets/f832d01c-cd9f-43e4-8f6a-9c511fb0b353)


## Catatan Tambahan
- Pastikan semua dependensi telah diinstal sebelum menjalankan aplikasi.
- Gunakan `streamlit run datavisualisasi.py` untuk menampilkan dashboard secara interaktif.

## Kontributor
- **[Nama Anda]** - Wiraldy Manggala Simanjuntak

## Lisensi
Proyek ini didistribusikan di bawah lisensi [MIT License](LICENSE).

---
Jika ada pertanyaan atau ingin berkontribusi, silakan hubungi saya! 🚀

