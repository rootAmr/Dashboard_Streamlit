import streamlit as st
import pandas as pd
import altair as alt

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

# Tampilkan diagram pie
st.subheader('Persentase Penyewaan Sepeda pada Hari Berbeda')
fig, ax = plt.subplots(figsize=(8, 8))
potongan, teks, teks_otomatis = plt.pie(
    jumlah_penyewaan_per_jenis_hari,
    labels=jumlah_penyewaan_per_jenis_hari.index,
    autopct=lambda p: '{:.1f}%\n({:.0f} kali penyewaan)'.format(p, p * sum(jumlah_penyewaan_per_jenis_hari) / 100),
    startangle=90,
    colors=['skyblue', 'lightcoral']
)
plt.legend(potongan, jumlah_penyewaan_per_jenis_hari.index, title='Jenis Hari', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
plt.setp(teks_otomatis, size=8, weight="bold")
plt.title('Persentase dan Jumlah Penyewaan Sepeda pada Hari Kerja dan Hari Libur')
st.pyplot(fig)

st.header('Korelasi antara Suhu dan Jumlah Total Penyewaan Sepeda')

korelasi = data_day['temp'].corr(data_day['total_count'])
if korelasi > 0:
    interpretasi_korelasi = "Terdapat korelasi positif antara suhu dan jumlah total penyewaan sepeda."
elif korelasi < 0:
    interpretasi_korelasi = "Terdapat korelasi negatif antara suhu dan jumlah total penyewaan sepeda."
else:
    interpretasi_korelasi = "Tidak ada hubungan linear yang signifikan antara suhu dan jumlah total penyewaan sepeda."

# Create an Altair scatter plot
scatter_chart = alt.Chart(data_day).mark_circle().encode(
    x='temp',
    y='total_count',
    tooltip=['temp', 'total_count']
).properties(
    title=f'Korelasi antara Suhu dan Jumlah Total Penyewaan Sepeda ({korelasi:.2f})',
    width=600,
    height=400
)

# Display the Altair chart using Streamlit
st.altair_chart(scatter_chart, use_container_width=True)

st.write(interpretasi_korelasi)
