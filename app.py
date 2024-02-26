import streamlit as st
import pandas as pd
import altair as alt


data_url = "https://raw.githubusercontent.com/rootAmr/Dashboard_Streamlit/main/streamlite/data_day_cleaned.csv"
data_day = pd.read_csv(data_url)

def kategorikan_hari(hari):
    return 'Akhir Pekan/Libur' if hari in ['Sabtu', 'Minggu'] else 'Hari Kerja'

data_day['jenis_hari'] = data_day['weekday'].apply(kategorikan_hari)

jumlah_penyewaan_per_jenis_hari = data_day.groupby('jenis_hari')['total_count'].sum()
persentase_penyewaan_per_jenis_hari = (jumlah_penyewaan_per_jenis_hari / jumlah_penyewaan_per_jenis_hari.sum()) * 100

st.title('Analisis Penyewaan Sepeda')

st.subheader('Data Mentah')
st.write(data_day)


st.subheader('Persentase Penyewaan Sepeda pada Hari Berbeda')

bar_chart = st.bar_chart(jumlah_penyewaan_per_jenis_hari)

for i, val in enumerate(jumlah_penyewaan_per_jenis_hari):
    st.text(f"{jumlah_penyewaan_per_jenis_hari.index[i]}: {val} ({persentase_penyewaan_per_jenis_hari[i]:.1f}%)")

st.header('Korelasi antara Suhu dan Jumlah Total Penyewaan Sepeda')

korelasi = data_day['temp'].corr(data_day['total_count'])
if korelasi > 0:
    interpretasi_korelasi = "Terdapat korelasi positif antara suhu dan jumlah total penyewaan sepeda."
elif korelasi < 0:
    interpretasi_korelasi = "Terdapat korelasi negatif antara suhu dan jumlah total penyewaan sepeda."
else:
    interpretasi_korelasi = "Tidak ada hubungan linear yang signifikan antara suhu dan jumlah total penyewaan sepeda."

scatter_chart = alt.Chart(data_day).mark_circle().encode(
    x='temp',
    y='total_count',
    tooltip=['temp', 'total_count']
).properties(
    title=f'Korelasi antara Suhu dan Jumlah Total Penyewaan Sepeda ({korelasi:.2f})',
    width=600,
    height=400
)

st.altair_chart(scatter_chart, use_container_width=True)

st.write(interpretasi_korelasi)

st.header('Kesimpulan')

st.write("""
Terdapat hubungan positif antara suhu dan jumlah total sepeda, informasi ini bisa berguna untuk pengelola sistem penyewaan sepeda. 
Mereka dapat mengoptimalkan strategi pemasaran atau menyesuaikan inventaris sepeda berdasarkan perubahan musim.

Terdapat perbedaan yang signifikan dalam pola penyewaan sepeda antara hari kerja dan hari libur. 
Mayoritas penyewaan terjadi pada hari kerja, sedangkan penyewaan pada hari libur merupakan sebagian kecil dari total penyewaan sepeda. 
Ini mungkin disebabkan oleh aktivitas bersepeda yang lebih tinggi di hari kerja, saat orang-orang mungkin menggunakan sepeda untuk transportasi sehari-hari.
""")
