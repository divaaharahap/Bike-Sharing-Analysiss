# Proyek Analisis Data: Bike Sharing Dataset

## 1. Informasi Proyek
**Nama**: Diva Anggreini Harahap  
**Email**: divaanggreiniharahap@gmail.com  
**ID Dicoding**: divaaharahap  

## 2. Tentang Dataset 🚴‍♂️
Dataset ini berisi **data penyewaan sepeda** dari sistem **Capital Bikeshare** di **Washington D.C., USA** selama tahun **2011-2012**.
Sistem ini memungkinkan pengguna untuk menyewa sepeda dari satu lokasi dan mengembalikannya di lokasi lain secara otomatis.

### 2.1 Informasi Dataset
- **Sumber Data**: Capital Bikeshare system, Washington D.C., USA.
- **Periode Data**: Tahun **2011 - 2012**.
- **Struktur Data**:
    - Data dikumpulkan **per jam** dengan informasi terkait cuaca dan musim.
    - Informasi meliputi **jumlah penyewaan sepeda**, kondisi cuaca, suhu, kecepatan angin, dan faktor lain.
- **Sumber Cuaca**: Data cuaca diperoleh dari **freemeteo.com**.
- **Tujuan Penggunaan**:
    - Menganalisis pola penyewaan sepeda berdasarkan waktu dan cuaca.
    - Melakukan **clustering jam operasional** berdasarkan jumlah penyewaan.

## 3. Menentukan Pertanyaan Bisnis
- **Bagaimana pengaruh kondisi cuaca terhadap jumlah sepeda yang disewa per jam di tahun 2012?**
- **Pada jam berapa dalam sehari permintaan penyewaan sepeda mencapai puncaknya?**

## 4. Install Semua Packages yang Dibutuhkan
`pip install numpy pandas matplotlib seaborn`

## 5. Cara Menjalankan Dashboard
- Pastikan Streamlit sudah terinstal
`pip install streamlit`
- Navigasi ke direktori proyek
`cd path/to/dashboard`
- Jalankan aplikasi Streamlit
`streamlit run dashboard.py`
