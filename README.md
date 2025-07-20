# Analisis Sentimen Ulasan Singapore Airlines dengan BERT & RoBERTa

Proyek ini bertujuan untuk melakukan analisis sentimen pada ulasan pelanggan Singapore Airlines menggunakan model deep learning canggih, yaitu BERT dan RoBERTa, untuk mengklasifikasikan sentimen sebagai positif atau negatif.

---

## Daftar Isi

1. [Deskripsi](#deskripsi)
2. [Tujuan](#tujuan)
3. [Dataset](#dataset)
4. [Data Dictionary](#data-dictionary)
5. [Tech Stack](#tech-stack)
6. [Instalasi & Cara Menjalankan](#instalasi--cara-menjalankan)
7. [Hasil Model](#hasil-model)

---

## Deskripsi

Dalam proyek ini, sebuah aplikasi web interaktif dibangun menggunakan Streamlit untuk menganalisis sentimen dari ulasan pelanggan Singapore Airlines. Pengguna dapat memasukkan teks ulasan, dan aplikasi akan memprediksi sentimennya menggunakan model yang telah dilatih, yaitu BERT atau RoBERTa. Analisis ini memberikan wawasan berharga bagi maskapai untuk memahami persepsi pelanggan.

## Tujuan

- Mengembangkan model klasifikasi sentimen dengan akurasi tinggi menggunakan arsitektur Transformer (BERT & RoBERTa).
- Membangun aplikasi web yang mudah digunakan untuk mendemokan kemampuan model.
- Membantu maskapai penerbangan dalam memonitor dan memahami umpan balik pelanggan secara efisien.

---

## Dataset

Dataset yang digunakan dalam proyek ini adalah [Singapore Airline Reviews](https://www.kaggle.com/datasets/kanchana1990/singapore-airlines-reviews) yang berisi ulasan teks dari pelanggan beserta label sentimennya.

## Data Dictionary

| Variabel | Tipe Data | Deskripsi |
| :--- | :--- | :--- |
| **reviews** | Teks | Ulasan dari pelanggan dalam format teks. |
| **sentiment**| Kategorikal | Sentimen dari ulasan (0: negatif, 1: positif). |

---

## Tech Stack

- **Bahasa Pemrograman:** Python 3.9.0
- **Framework Aplikasi Web:** Streamlit
- **Library Utama:**
  - `torch==2.1.0`
  - `transformers==4.31.0`
  - `scikit-learn==1.3.1`
  - `pandas==2.1.3`
  - `joblib==1.3.0`
  - `altair==4.2.2`
  - `streamlit-extras`
  - `streamlit-lottie`

---

## Instalasi & Cara Menjalankan

1.  **Clone Repositori**
    ```bash
    git clone https://github.com/haaahabib/sentiment-analysis.git
    ```

2.  **Masuk ke Direktori Proyek**
    ```bash
    cd Sentiment-Analysis
    ```

3.  **Buat Virtual Environment** (direkomendasikan)
    ```bash
    python -m venv venv
    ```

4.  **Aktivasi Virtual Environment**
    -   **Windows:** `.\venv\Scripts\activate`
    -   **macOS/Linux:** `source venv/bin/activate`

5.  **Install Library yang Dibutuhkan**
    ```bash
    pip install -r requirements.txt
    ```

6.  **Jalankan Aplikasi Streamlit**
    ```bash
    streamlit run app.py
    ```
    Aplikasi akan terbuka secara otomatis di browser Anda.

---

## Hasil Model

Berdasarkan evaluasi pada data uji, berikut adalah perbandingan performa antara model BERT dan RoBERTa. RoBERTa menunjukkan performa yang sedikit lebih unggul.

### **Tabel Hasil Model BERT (Akurasi: 94%)**

| Kelas | Precision | Recall | F1-Score |
| :--- | :---: | :---: | :---: |
| **Negatif** | 0.93 | 0.94 | 0.94 |
| **Positif** | 0.94 | 0.93 | 0.93 |

### **Tabel Hasil Model RoBERTa (Akurasi: 95%)**

| Kelas | Precision | Recall | F1-Score |
| :--- | :---: | :---: | :---: |
| **Negatif** | 0.95 | 0.96 | 0.95 |
| **Positif** | 0.96 | 0.95 | 0.95 |
