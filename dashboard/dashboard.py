import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st


# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("dashboard/df_hour_cleaned.csv")
    df["dteday"] = pd.to_datetime(df["dteday"])
    df["weekday"] = df["dteday"].dt.weekday  # Tambahkan kolom weekday
    return df

df = load_data()

# Filter data untuk tahun 2012
hour_df_2012 = df[df["yr"] == 1]  # 1 menunjukkan tahun 2012, 0 menunjukkan 2011

# Sidebar navigation
st.sidebar.title("Dashboard Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ["Tentang Dataset", "Data Overview", "Visualisasi Data", "Clustering"])

# Filtering berdasarkan rentang tanggal
st.sidebar.subheader("Filter Data")
date_range = st.sidebar.date_input("Pilih Rentang Tanggal", [df["dteday"].min(), df["dteday"].max()], min_value=df["dteday"].min(), max_value=df["dteday"].max())

if isinstance(date_range, tuple) and len(date_range) == 2:
    df = df[(df["dteday"] >= pd.to_datetime(date_range[0])) & (df["dteday"] <= pd.to_datetime(date_range[1]))]

if page == "Tentang Dataset":
    st.title("Tentang Dataset 🚴‍♂️")
    st.write("""
    Dataset ini berisi **data penyewaan sepeda** dari sistem **Capital Bikeshare** di **Washington D.C., USA** selama tahun **2011-2012**.
    """)
    
    st.subheader("Informasi Dataset")
    st.write("""
    - **Sumber Data**: Capital Bikeshare system, Washington D.C., USA.
    - **Periode Data**: Tahun **2011 - 2012**.
    """)

elif page == "Data Overview":
    st.title("Ringkasan Data")
    st.write("Tampilan pertama dari dataset:")
    st.dataframe(df.head())
  
    st.write("Statistik Deskriptif:")
    st.write(df.describe())

elif page == "Visualisasi Data":
    st.title("Visualisasi Data Penyewaan Sepeda")
    
    # Boxplot untuk mendeteksi outlier
    st.subheader("Boxplot Variabel Utama")
    columns = ["cnt", "casual", "registered", "windspeed", "hum"]
    fig, axes = plt.subplots(1, len(columns), figsize=(20, 5))
    for i, col in enumerate(columns):
        sns.boxplot(y=df[col], ax=axes[i])
        axes[i].set_title(f"Boxplot of {col}")
    st.pyplot(fig)
    
    # Barplot Pengaruh Kondisi Cuaca
    st.subheader("Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda")
    weather_group = df.groupby("weathersit")["cnt"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=weather_group["weathersit"], y=weather_group["cnt"], palette="coolwarm")
    plt.xlabel("Kondisi Cuaca (1 = Cerah, 2 = Berawan, 3 = Hujan ringan, 4 = Badai)")
    plt.ylabel("Rata-rata Penyewaan Sepeda per Jam")
    st.pyplot(fig)
    
    # Lineplot Tren Permintaan Sepeda per Jam
    st.subheader("Tren Permintaan Penyewaan Sepeda Berdasarkan Jam")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x=df["hr"], y=df["cnt"], marker="o", color="b", ax=ax)
    ax.set_xlabel("Jam dalam Sehari")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda")
    st.pyplot(fig)
    
elif page == "Clustering":
    st.title("Clustering Kategori Jam")
    df["Hour_Category"] = df["hr"].apply(lambda x: 'Peak Hours' if 7 <= x <= 9 or 16 <= x <= 19 else ('Normal Hours' if 10 <= x <= 15 else 'Off-Peak Hours'))
    hourly_clustering = df.groupby("Hour_Category")["cnt"].mean().reset_index()
    
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x="Hour_Category", y="cnt", hue="Hour_Category", palette="coolwarm", legend=False, data=hourly_clustering, ax=ax)
    ax.set_xlabel("Kategori Jam")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda")
    st.pyplot(fig)
