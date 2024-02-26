import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data from the given link
data_url = "https://raw.githubusercontent.com/rootAmr/Dashboard_Streamlit/main/streamlite/data_day_cleaned.csv"
data_day = pd.read_csv(data_url)

# Categorize days into weekdays and weekends
data_day['day_type'] = data_day['weekday'].apply(lambda x: 'Weekend/Holiday' if x in ['Sabtu', 'Minggu'] else 'Weekday')

# Group by day type and calculate rentals
day_type_rentals = data_day.groupby('day_type')['total_count'].sum()
day_type_percentages = (day_type_rentals / day_type_rentals.sum()) * 100

# Create a pie chart
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(day_type_rentals, labels=day_type_rentals.index, autopct=lambda p: '{:.1f}%\n({:.0f} rentals)'.format(p, p * sum(day_type_rentals) / 100), startangle=90, colors=['skyblue', 'lightcoral'])
ax.legend(wedges, day_type_rentals.index, title='Day Type', loc='center left', bbox_to_anchor=(1, 0, 0.5, 1))
plt.setp(autotexts, size=8, weight="bold")

ax.set_title('Persentase dan Jumlah Penyewaan Sepeda pada Hari Kerja dan Hari Libur')

# Display the pie chart using Streamlit
st.pyplot(fig)
