
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set title of the app
st.title('Bike Sharing Data Analysis')

# Load dataset
@st.cache
def load_data():
    day_data = pd.read_csv('day.csv')  # Path ke dataset harian Anda
    return day_data

data = load_data()

# Show raw data
st.subheader('Raw Data')
if st.checkbox('Show raw data'):
    st.write(data.head())

# Visualisasi: Penggunaan sepeda berdasarkan cuaca
st.subheader('Pengaruh Cuaca terhadap Penggunaan Sepeda')
weather_option = st.selectbox('Pilih Kondisi Cuaca:', ['1 = Cerah', '2 = Mendung', '3 = Hujan'])
filtered_data = data[data['weathersit'] == int(weather_option[0])]

fig, ax = plt.subplots()
sns.barplot(x='weathersit', y='cnt', data=filtered_data, ax=ax)
ax.set_title('Pengaruh Kondisi Cuaca terhadap Penggunaan Sepeda')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Jumlah Pengguna Sepeda')
st.pyplot(fig)

# Visualisasi: Penggunaan sepeda berdasarkan musim
st.subheader('Penggunaan Sepeda Berdasarkan Musim')
fig, ax = plt.subplots()
sns.barplot(x='season', y='cnt', data=data, ax=ax)
ax.set_title('Penggunaan Sepeda Berdasarkan Musim')
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Pengguna Sepeda')
st.pyplot(fig)

# Kesimpulan
st.subheader('Kesimpulan')
st.write("""
1. Cuaca cerah meningkatkan penggunaan sepeda, sedangkan kondisi hujan menguranginya secara signifikan.
2. Musim semi dan musim panas memiliki jumlah pengguna sepeda tertinggi, sedangkan musim gugur dan musim dingin menunjukkan penurunan penggunaan sepeda.
""")
