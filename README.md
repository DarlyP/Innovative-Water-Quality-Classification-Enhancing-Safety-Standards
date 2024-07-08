![Water](https://github.com/DarlyP/Water-Quality-Analysis-Using-Machine-Learning/blob/main/Notebook/water.jpg)

# Water Quality Analysis Using Machine Learning

---


## Data Source

Kaggle: [Water Quality](https://www.kaggle.com/datasets/mssmartypants/water-quality).

---

## Introduction

Dalam rangka meningkatkan kualitas air dan mendukung pertumbuhan perusahaan secara berkelanjutan, diadakan upaya untuk mengidentifikasi, menganalisis, dan mengatasi pencemaran air. Dengan pendekatan berbasis data, fokus terletak pada menghasilkan solusi yang tidak hanya menguntungkan perusahaan, tetapi juga memberikan dampak positif yang signifikan pada kesehatan masyarakat dan kelestarian lingkungan. Dengan upaya holistik dan strategis, tujuannya adalah membentuk masa depan yang lebih bersih dan lebih berkelanjutan bagi semua pihak yang terlibat.

---

## Conclusion

Kesimpulan yang diperoleh dari analisis data ini adalah sebagai berikut:

1. **Industri Berat dan Pertambangan Logam:**

    - Daerah ini kemungkinan merupakan area industri berat yang terkait dengan aktivitas pertambangan logam seperti seng, timah, atau tembaga.

    - Kegiatan industri berat seperti manufaktur logam, pengolahan limbah, atau produksi bahan kimia dapat menyebabkan pelepasan berbagai logam berat ke lingkungan sekitarnya.

2. **Infrastruktur Sanitasi yang Buruk:**

    - Infrastruktur sanitasi yang tidak memadai atau kurangnya fasilitas sanitasi yang layak dapat menyebabkan pencemaran air dengan bakteri, virus, dan senyawa kimia berbahaya.

    - Sistem pengolahan air limbah yang tidak efektif dapat mencemari sumber air permukaan dan air tanah.

3.  **Aktivitas Geologis Tinggi:**

    - Kemungkinan adanya aktivitas geologis yang tinggi seperti vulkanisme atau pembentukan batuan yang kaya akan mineral tertentu dapat menyebabkan air mengandung senyawa-senyawa beracun seperti arsenik, uranium, dan radium.

4.  **Dampak Limbah Pertambangan:**

    - Limbah pertambangan yang tidak terkelola dengan baik dapat mencemari air permukaan dan air tanah dengan logam-logam berat seperti cadmium, aluminium, dan selenium.

    - Proses pencucian atau limbah tailing dari pertambangan logam dapat meningkatkan risiko kontaminasi air di daerah sekitar.

5. **Kesehatan Masyarakat:**

    - Air yang tercemar dengan bakteri, virus, dan logam berat dapat menjadi sumber penyakit yang serius bagi masyarakat setempat.

    - Masalah pencemaran air yang ada memerlukan tindakan remediasi dan pengelolaan lingkungan yang ketat untuk melindungi kesehatan masyarakat dan menjaga keberlanjutan lingkungan.

---

## Model Evaluation

Berdasarkan performa model yang digunakan yakni Support Vector Machine (SVM) ada beberapa masukan yang bisa diberikan:

1. Kelebihan:

    - Kemampuan menangani data non-linear saat menghadapi masalah kualitas air yang mungkin memiliki pola yang kompleks dan tidak linear.

    - Kemampuan menangani data berdimensi tinggiyang sering terjadi dalam analisis kualitas air di mana data dapat berasal dari berbagai sumber dan parameter yang berbeda.

    - Resisten terhadap *overfitting*

2. Kekurangan:

    - Membutuhkan waktu yang lama terlebih jika menggunakan kernel yang lebih kompleks

    - Tidak efisien untuk data yang besar 

    - Cenderung menangkap nilai 0 (Dangerous)

3. Saran untuk peningkatan:

    - Disarankan untuk menggunakan parameter C yang optimal

    - Gunakaan kernel yang lain seperti RBF, polynominal atau sigmoid

    - Jika menghadapi data yang besar, disarankan menggunakan PCA

    - Lebih memperbanyak data 
    
    - Melakukan *data balancing*

---

**Disclaimer**: Notebook ini dibuat semata-mata untuk tujuan pembelajaran dan eksplorasi. Tidak ada maksud untuk menyinggung atau merugikan pihak mana pun. Segala konten dan analisis yang disajikan didasarkan pada data publik yang tersedia secara online. Saya melakukan proses ini untuk meningkatkan pemahaman tentang teknik dan metodologi analisis data, serta untuk mengasah keterampilan dalam mengimplementasikan algoritma dan model yang relevan dalam konteks pembelajaran data science.

Dalam melakukan analisis ini, saya berusaha menjaga objektivitas dan profesionalitas dalam menginterpretasikan data yang ada. Segala kesimpulan atau rekomendasi yang disampaikan merupakan hasil dari analisis pribadi dan tidak bermaksud sebagai saran profesional dalam kapasitas tertentu. Saya berharap informasi yang diperoleh dari notebook ini dapat bermanfaat bagi siapa pun yang membacanya untuk kepentingan belajar dan pengembangan keterampilan analisis data.
