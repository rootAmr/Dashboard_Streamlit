import streamlit as st
import pandas as pd

# Muat data dari tautan yang diberikan
data_url = "https://raw.githubusercontent.com/rootAmr/Dashboard_Streamlit/main/streamlite/data_day_cleaned.csv"
data_day = pd.read_csv(data_url)

def kategorikan_hari(hari):
    return 'Akhir Pekan/Libur' if hari in ['Sabtu', 'Minggu'] else 'Hari Kerja'

data_day['jenis_hari'] = data_day['weekday'].apply(kategorikan_hari)

jumlah_penyewaan_per_jenis_hari = data_day.groupby('jenis_hari')['total_count'].sum()
persentase_penyewaan_per_jenis_hari = (jumlah_penyewaan_per_jenis_hari / jumlah_penyewaan_per_jenis_hari.sum()) * 100

# Dashboard Streamlit
st.title('Analisis Penyewaan Sepeda')

st.subheader('Data Mentah')
st.write(data_day)

# Tampilkan diagram pie dengan Streamlit
st.subheader('Persentase Penyewaan Sepeda pada Hari Berbeda')
st.pie_chart(jumlah_penyewaan_per_jenis_hari)

st.header('Korelasi antara Suhu dan Jumlah Total Penyewaan Sepeda')

korelasi = data_day['temp'].corr(data_day['total_count'])
if korelasi > 0:
    interpretasi_korelasi = "Terdapat korelasi positif antara suhu dan jumlah total penyewaan sepeda."
elif korelasi < 0:
    interpretasi_korelasi = "Terdapat korelasi negatif antara suhu dan jumlah total penyewaan sepeda."
else:
    interpretasi_korelasi = "Tidak ada hubungan linear yang signifikan antara suhu dan jumlah total penyewaan sepeda."

# Visualisasi scatter plot dengan Streamlit
st.subheader('Korelasi antara Suhu dan Jumlah Total Penyewaan Sepeda')
st.scatter_chart(data_day[['temp', 'total_count']])

st.write(interpretasi_korelasi)
