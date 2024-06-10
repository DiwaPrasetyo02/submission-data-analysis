import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# URL file CSV dari dataset
url = 'https://raw.githubusercontent.com/DiwaPrasetyo02/submission-data-analysis/main/day.csv'
df = pd.read_csv(url)

# Judul Aplikasi
st.title("Analisis Rental Sepeda berdasarkan Cuaca dan Musim")

# Analisis Korelasi Cuaca dan Rental Sepeda
st.header("Analisis Korelasi Cuaca dan Rental Sepeda")

# Visualisasi jumlah rental sepeda berdasarkan kondisi cuaca
weather_counts = df.groupby('weathersit')['cnt'].sum().reset_index()
weather_counts.columns = ['Weather Condition', 'Total Rentals']
weather_condition_map = {1: 'Clear, Few clouds, Partly cloudy, Partly cloudy',
                         2: 'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist',
                         3: 'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds',
                         4: 'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog'}
weather_counts['Weather Condition'] = weather_counts['Weather Condition'].map(weather_condition_map)

fig1, ax1 = plt.subplots()
sns.barplot(x='Weather Condition', y='Total Rentals', data=weather_counts, ax=ax1)
ax1.set_xlabel("Kondisi Cuaca")
ax1.set_ylabel("Jumlah Rental Sepeda")
ax1.set_title("Jumlah Rental Sepeda berdasarkan Kondisi Cuaca")
ax1.tick_params(axis='x', rotation=45)
st.pyplot(fig1)

# Analisis Rental Sepeda Musiman
st.header("Analisis Rental Sepeda Musiman")

# Visualisasi jumlah rental sepeda berdasarkan musim
season_counts = df.groupby('season')['cnt'].sum().reset_index()
season_counts.columns = ['Season', 'Total Rentals']
season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
season_counts['Season'] = season_counts['Season'].map(season_map)

fig2, ax2 = plt.subplots()
sns.barplot(x='Season', y='Total Rentals', data=season_counts, ax=ax2)
ax2.set_xlabel("Musim")
ax2.set_ylabel("Jumlah Rental Sepeda")
ax2.set_title("Jumlah Rental Sepeda berdasarkan Musim")
st.pyplot(fig2)
