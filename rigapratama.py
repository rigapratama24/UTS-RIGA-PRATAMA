Essay. 
1. Machine learning adalah bidang yang berkembang pesat dengan potensi besar untuk mengubah berbagai aspek kehidupan kita. Dengan kemampuannya untuk belajar dari data dan membuat keputusan yang cerdas, machine learning memiliki potensi untuk merevolusi cara kita bekerja, hidup, dan berinteraksi dengan dunia di sekitar kita. Tujuannya adalah untuk memungkinkan komputer untuk belajar dari pengalaman atau data yang diberikan, dan kemudian menggunakan pembelajaran tersebut untuk membuat prediksi atau mengambil keputusan dalam situasi yang belum pernah dilihat sebelumnya.



2. Deteksi Penipuan Kartu Kredit:
Implementasi: Algoritma machine learning menganalisis pola transaksi kartu kredit Anda untuk mendeteksi aktivitas yang mencurigakan dan mencegah penipuan.
Mengapa Dibutuhkan: Melindungi Anda dari penipuan kartu kredit dan pencurian identitas.
Manfaat: Meningkatkan keamanan keuangan, Menjaga uang Anda tetap aman dan terlindungi, Memberikan ketenangan pikiran,  Mengetahui bahwa Anda terlindungi dari penipuan. Mengurangi kerugian finansial, Mencegah Anda kehilangan uang akibat penipuan.


3. Taksonomi dalam Pengerapan Machine Learning
Taksonomi dalam machine learning mengklasifikasikan algoritma dan model machine learning berdasarkan berbagai kriteria, seperti tugas yang mereka lakukan, jenis data yang mereka gunakan, dan cara mereka belajar. Klasifikasi ini membantu praktisi machine learning untuk memilih algoritma atau model yang tepat untuk masalah yang ingin mereka pecahkan.
Berikut adalah beberapa taksonomi umum dalam machine learning:
1. Berdasarkan Tugas:
•	Supervised learning: Algoritma dilatih dengan data berlabel, di mana setiap data memiliki contoh input dan output yang diinginkan. Contohnya, klasifikasi email spam dan prediksi harga saham.
•	Unsupervised learning: Algoritma belajar dari data tidak berlabel, mencari pola dan struktur yang tersembunyi dalam data. Contohnya, pengelompokan pelanggan dan analisis jaringan sosial.
•	Reinforcement learning: Algoritma belajar melalui interaksi dengan lingkungan, menerima hadiah atau hukuman atas tindakannya. Contohnya, bermain game dan pelatihan robot.

Studi Kasus. 
1)
a) Berapa rata-rata mahasiswa datang pada minggu ini?
Rata-rata mahasiswa datang pada minggu ini adalah 3.2 orang per hari. Rata-rata = Total datang / Total hari = 19 / 7 = 3.2 orang per hari
b) Kapan biaya tertinggi terjadi?
Biaya tertinggi terjadi pada hari Sabtu, dengan total biaya Rp 150.000.
c) Hari apa biaya lebih dari 110000?
Biaya lebih dari 110.000 terjadi pada hari Selasa dan Sabtu.
d) Siapa yang paling banyak datang ke kampus?
Ani paling banyak datang ke kampus, dengan total 11 hari.
e) Siapa yang datang pada hari Minggu?
Ani dan Budi datang pada hari Minggu.
f) Berapa biaya tertinggi dan terendah?
Biaya tertinggi adalah Rp 150.000 pada hari Sabtu, dan biaya terendah adalah Rp 15.000 pada hari Kamis.
g) Berapa frekuensi datang tertinggi dan terendah?
Frekuensi datang tertinggi adalah 5 kali, terjadi pada Ani pada hari Sabtu.
Frekuensi datang terendah adalah 1 kali, terjadi pada Lono pada hari Kamis.

import matplotlib.pyplot as plt
import pandas as pd

# Data
fakultas = ["Bisnis", "D3 Perhotelan", "ICT", "Ilmu Komunikasi", "Seni dan Desain"]
jumlah_mahasiswa = [260, 28, 284, 465, 735]
akreditasi = ["A", "A", "B", "A", "A"]

# Create DataFrame
info_mahasiswa = pd.DataFrame({
    'fakultas': fakultas,
    'jumlah_mahasiswa': jumlah_mahasiswa,
    'akreditasi': akreditasi
})

# Plot
plt.figure(figsize=(10, 6))
bars = plt.bar(info_mahasiswa['fakultas'], info_mahasiswa['jumlah_mahasiswa'], color=['red', 'green', 'blue', 'cyan', 'magenta'])
plt.xlabel('Fakultas')
plt.ylabel('Jumlah Mahasiswa')
plt.title('Jumlah Mahasiswa per Fakultas')
plt.show()
