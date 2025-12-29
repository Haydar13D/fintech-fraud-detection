# 🛡️ Real-Time Fintech Anomaly Detection System

## 📌 Deskripsi Proyek
Proyek ini membangun sistem deteksi anomali transaksi keuangan secara *real-time* menggunakan ekosistem **Google Cloud Platform (GCP)**. Masalah utama yang diselesaikan adalah tingginya latensi pada metode analitik *batch* tradisional yang sering memberikan celah bagi pelaku penipuan (*fraud window*). Sistem ini mampu memproses data dan memberikan skor probabilitas fraud dalam hitungan detik.

## 🚀 Arsitektur Sistem
Sistem ini menggunakan arsitektur *Serverless* untuk menjamin skalabilitas:
1. **Python Publisher**: Simulator transaksi yang mengirimkan payload JSON ke Cloud Pub/Sub.
2. **Google Cloud Pub/Sub**: Message broker untuk menangani aliran data *streaming*.
3. **Google BigQuery**: Data warehouse untuk penyimpanan, proses ETL (SQL View), dan Machine Learning.
4. **BigQuery ML (BQML)**: Menggunakan algoritma *Logistic Regression* untuk prediksi risiko transaksi.
5. **Looker Studio**: Dashboard interaktif untuk pemantauan *real-time* dan sistem peringatan dini (Red Alert).

## 🛠️ Tech Stack
- **Language**: Python 3.13
- **Cloud**: Google Cloud Platform (Pub/Sub, BigQuery)
- **ML Algorithm**: Logistic Regression (via BQML)
- **Visualization**: Looker Studio
- **Data Format**: JSON Streaming

## 📁 Struktur Folder
- `/src`: Berisi skrip Python `publisher.py` (simulator transaksi).
- `/sql`: Berisi skrip SQL untuk pembuatan tabel, ETL View, dan ML Model.
- `README.md`: Dokumentasi proyek.

## 💡 Fitur Utama
- **Real-time Ingestion**: Menyerap ribuan data transaksi tanpa delay.
- **Automated ETL**: Mengurai data JSON mentah dan memperbaiki format *timestamp* secara otomatis menggunakan SQL.
- **Predictive Scoring**: Memberikan kolom `probability_of_fraud` (0.0 - 1.0) pada setiap transaksi yang masuk.
- **Visual Alerting**: Dashboard akan berubah warna menjadi MERAH jika ditemukan transaksi dengan probabilitas anomali tinggi.

## 📊 Hasil Analisa
- Transaksi normal secara konsisten mendapatkan skor probabilitas rendah (< 0.05).
- Transaksi yang sengaja disimulasikan sebagai anomali (nominal tinggi/lokasi tidak biasa) mendapatkan skor tinggi (> 0.90).
- Memangkas waktu deteksi dari hitungan jam (batch) menjadi kurang dari 5 detik (streaming).

## 📝 Kesimpulan
Proyek ini membuktikan bahwa integrasi antara *Data Streaming* dan *Cloud Machine Learning* dapat menciptakan sistem keamanan finansial yang proaktif, mengurangi potensi kerugian nasabah dengan konfirmasi instan saat transaksi mencurigakan terjadi.

---
*Proyek ini dikembangkan sebagai bagian dari tugas akhir sistem pemrosesan data streaming.*