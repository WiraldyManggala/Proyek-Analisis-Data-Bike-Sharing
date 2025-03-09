Analisis Data Bike Sharing

Setup Environment - Anaconda

Untuk menyiapkan lingkungan menggunakan Anaconda, jalankan perintah berikut:

conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

Setup Environment - Shell/Terminal

Jika menggunakan pipenv, jalankan perintah berikut:

mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt

Jalankan Aplikasi Streamlit

Setelah lingkungan telah dikonfigurasi, jalankan aplikasi Streamlit dengan perintah berikut:

streamlit run datavisualisasi.py

Tampilan Dashboard

Dashboard akan berjalan di browser dan menampilkan hasil analisis data peminjaman sepeda.

Contoh Tampilan:

![image](https://github.com/user-attachments/assets/ae934ab0-6ff1-403d-9741-6430f1d92b34)

Dashboard ini menampilkan berbagai visualisasi seperti distribusi peminjaman sepeda, pengaruh cuaca, serta tren peminjaman berdasarkan waktu.

Pastikan Anda memiliki dataset day.csv dan hour.csv dalam direktori proyek sebelum menjalankan aplikasi ini.

Selain itu, analisis data lebih lanjut dapat ditemukan dalam notebook Google Colab dengan nama file Proyek Analisis Data.ipynb.
