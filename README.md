# Sentiment Analysis Singapore Airline Reviews with BERT and RoBERTa

![Streamlit App](https://github.com/user-attachments/assets/2d2b4a44-1adf-4f3f-ad47-411e55abcf02)

## Table of Content

1. [Deskripsi](#Deskripsi)
2. [Tujuan](#Tujuan)
3. [Dataset](#Dataset)
4. [Data Dictionary](#Data-Dictionary)
5. [Library](#library-yang-diperlukan)
6. [Cloning Project](#Cara-Cloning-Repositori)
7. [BERT Model](#BERT-Model)
8. [RoBERTa Model](#RoBERTa-Model)
9. [Profil Pembuat](#Profil-Pembuat)

## Deskripsi

Project ini bertujuan untuk melakukan analisis sentimen pada ulasan Singapore Airlines menggunakan model BERT dan RoBERTa. Analisis ini memberikan wawasan apakah ulasan yang diberikan oleh pelanggan terhadap maskapai penerbangan bersifat positif atau negatif.

## Tujuan

Tujuan dari proyek ini adalah:
- Mengembangkan model untuk menganalisis sentimen dari teks ulasan penerbangan
- Memanfaatkan model BERT dan RoBERTa untuk meningkatkan akurasi analisis sentimen
- Membantu perusahaan penerbangan memahami sentimen pelanggan mereka

## Dataset
Dataset yang digunakan dalam project ini adalah [Singapore Airline Reviews](https://www.kaggle.com/datasets/kanchana1990/singapore-airlines-reviews)

## Data Dictionary
![image](https://github.com/user-attachments/assets/13a1b8af-6388-4ee8-ac4a-3ae1c2324f9f)

## Library yang diperlukan
Berikut adalah daftar library yang diperlukan dalam proyek ini, yang dapat diinstal melalui file `requirements.txt`:

- **tensorflow-cpu==2.13.0**
- **transformers==4.31.0**
- **scikit-learn==1.3.1**
- **joblib==1.3.0**
- **pandas==2.1.3**
- **streamlit==1.25.0**
- **altair==4.2.2**
- **streamlit-extras==0.5.0**
- **streamlit-lottie**

## Cara Cloning Repositori

1. Clone repositori dengan menggunakan Git
    ```bash
    git clone https://github.com/haaahabib/Sentiment-Analysis.git
    ```

2. Masuk ke direktori project
    ```bash
    cd Sentiment-Analysis
    ```

3. Buat **virtual environment** menggunakan **Python 3.9.0** 
    ```bash
    python -m venv venv
    ```

4. Aktivasi virtual environment
    - **Windows**:
      ```bash
      .\venv\Scripts\activate
      ```
    - **Mac/Linux**:
      ```bash
      source venv/bin/activate
      ```

5. Install semua **library yang diperlukan**
    ```bash
    pip install -r requirements.txt
    ```

6. Jalankan aplikasi **Streamlit**
    ```bash
    streamlit run app.py
    ```
## BERT Model
![image](https://github.com/user-attachments/assets/c1423f7e-9d61-438b-92ab-778a8fda9399)
![image](https://github.com/user-attachments/assets/0eb9fefd-142a-41a3-b1f4-6f1c4112fab6)

## RoBERTa Model
![image](https://github.com/user-attachments/assets/c076b3aa-385f-4b1d-bdfb-08c954d7447d)
![image](https://github.com/user-attachments/assets/5e9fa807-3668-416d-bb26-2a2b26d6cd6c)

## Profil Pembuat
- **Nama**: [Muhammad Habibulloh](https://github.com/haaahabib)
- **NIM**: 202110370311259
- **Kelas**: Machine Learning (C)
- [**LinkedIn**](https://www.linkedin.com/in/mhabibulloh/)

