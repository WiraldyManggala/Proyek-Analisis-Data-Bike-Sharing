import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Analisis Data Bike Sharing')

st.header('1. Menentukan Pertanyaan Bisnis')
st.write('1. Bagaimana pengaruh cuaca terhadap jumlah peminjaman sepeda?')
st.write('2. Bagaimana tren peminjaman sepeda berdasarkan waktu (harian dan bulanan)?')

st.header('2. Import Data')
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')
st.write('Dataset Harian:', day_df.head())
st.write('Dataset Per Jam:', hour_df.head())

st.header('3. Data Wrangling')
st.subheader('Assessing Data')

st.subheader('Insight dari Assessing Data')
st.write("Dataset tidak memiliki missing values berdasarkan pengecekan awal.")
st.write("Data terdiri dari berbagai fitur seperti tanggal, musim, suhu, kelembaban, dan jumlah peminjaman.")
st.write("Tidak ada nilai yang perlu diisi ulang atau dihapus dalam tahap awal ini.")

st.subheader('Cleaning Data')
st.write("Tidak ditemukan data duplikat sehingga tidak ada data yang perlu dihapus.")

st.header('4. Exploratory Data Analysis (EDA)')
st.subheader('Distribusi jumlah peminjaman')
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(day_df['cnt'], bins=30, kde=True, ax=ax)
ax.set_title('Distribusi Total Peminjaman Sepeda Harian')
st.pyplot(fig)

st.subheader('Insight dari EDA')
st.write("Distribusi jumlah peminjaman sepeda menunjukkan pola yang mendekati distribusi normal.")
st.write("Ada kemungkinan adanya hari-hari tertentu dengan jumlah peminjaman yang jauh lebih tinggi atau lebih rendah dari biasanya.")

st.header('5. Visualization & Explanatory Analysis')
st.subheader('Pengaruh Cuaca terhadap Peminjaman Sepeda')
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x='weathersit', y='cnt', data=day_df, ax=ax)
ax.set_title('Pengaruh Cuaca terhadap Jumlah Peminjaman')
st.pyplot(fig)

st.subheader('Insight dari Visualisasi Pertanyaan 1')
st.write("Boxplot digunakan karena dapat menunjukkan distribusi data serta outlier yang mungkin ada.")
st.write("Cuaca yang lebih buruk cenderung mengurangi jumlah peminjaman sepeda.")

st.subheader('Tren Peminjaman Sepeda berdasarkan Bulan')
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='mnth', y='cnt', data=day_df, estimator='mean', ax=ax)
ax.set_title('Tren Peminjaman Sepeda berdasarkan Bulan')
st.pyplot(fig)

st.subheader('Insight dari Visualisasi Pertanyaan 2')
st.write("Lineplot digunakan karena efektif untuk menunjukkan tren data dari waktu ke waktu.")
st.write("Terlihat adanya tren musiman, dengan jumlah peminjaman meningkat pada bulan-bulan tertentu.")

st.header('6. Conclusion')
st.subheader('Kesimpulan Pertanyaan 1')
st.write("Cuaca memengaruhi jumlah peminjaman sepeda, dengan cuaca buruk menyebabkan penurunan jumlah peminjaman.")

st.subheader('Kesimpulan Pertanyaan 2')
st.write("Peminjaman sepeda menunjukkan pola musiman, dengan peningkatan pada bulan-bulan tertentu.")
