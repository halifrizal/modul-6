# MODUL 6 - Web Deployment

## Overview Project

> **NOTE!** Project ini bertujuan untuk mengembangkan model machine learning untuk mengenali citra tangan dalam permainan batu-gunting-kertas (Rock-Paper-Scissors/RPS). Model ini dapat digunakan untuk membuat aplikasi atau game yang memanfaatkan pengenalan gestur tangan.

#### Ketentuan Project
1. Peserta praktikum diminta untuk melakukan pengembangan AI Web Deployment berdasarkan
modul sebelumnya. Jenis data yang dapat dipilih meliputi:
a. Data Citra
b. Data Tabular
c. Data Teks
2. Dataset yang digunakan merupakan dataset yang telah diaplikasikan pada modul-modul sebelumnya.
3. Praktikan diminta untuk memperkaya pengembangan AI Web sebelumnya yang telah di-deploy
dengan kreativitas individu masing-masing. Upaya kreatifitas dapat mencakup peningkatan estetika
tampilan, detail informasi AI Web, peningkatan akurasi model, atau peningkatan aspek lainnya
4. Lakukan deploy model yang telah disimpan ke dalam bentuk web basis. Pilihan library seperti Flask,
Tensorflow-js, atau teknologi lainnya dapat disesuaikan dengan tingkat kemampuan peserta.
5. Setelah model berhasil di-deploy dalam bentuk web dan berjalan dengan baik, peserta diminta untuk
membuat repository GitHub. Selanjutnya, lakukan commit terhadap keseluruhan project, dan
buatlah README.md yang memuat laporan hasil pengembangan proyek. Contoh README.md yang
baik dapat dilihat pada [link berikut](https://github.com/muhfadh/Tugas_Praktikum_ML_A_297-233) 
6. Setelah seluruh tahapan selesai, peserta diminta untuk mengumpulkan link GitHub beserta demo
kepada asisten yang telah ditentukan.


## Dataset
#### Pre-Processing dataset
Pada tahap ini meliputi tahap-tahap berikut:
1. Ekstraksi Dataset:
Mengunduh dan mengekstrak dataset RPS dalam format zip.

2. Pembagian Dataset:
Memisahkan dataset menjadi set pelatihan, validasi, dan pengujian menggunakan proporsi 70:25:5.

3. Augmentasi Data:
Menggunakan augmentasi data pada set pelatihan untuk meningkatkan variasi dan mencegah overfitting.
Augmentasi mencakup zoom range sebesar 20%, rotasi hingga 20 derajat, dan flip horizontal.

4. Normalisasi Citra:
Merescale nilai pixel citra agar berada dalam rentang 0 hingga 1.

> **NOTE!** Dataset dapat dilihat pada [link berikut](https://drive.google.com/file/d/1X9jFokn9AXMMVTmlBQ7XZpBsLKVFnp-d/view?usp=drive_link) 



![image](assets/mobilenetv2.png)

ResNet50

![image](assets/resnet.png)

**Akurasi** yang didapatkan dengan menggunakan model CNN adalah : **97.22%**

Sedangkan dengan tambahan method pre-trained yaitu model MobileNetV2 dan Resnet50 adalah : **92.85%** dan **90.47%**

## Overview Dataset

**_Link Dataset yang digunakan :_** [rps dataset](https://drive.google.com/drive/folders/1kgyN9Ah_w6MvxsRxANh3TfB9S-bCVZMv).
Gambar yang digunakan adalah Rock, Paper dan Scissors dengan total gambar 2.520 gambar. Terdiri dari 840 gambar jenis Rock, 840 gambar jenis Paper dan 840 gambar jenis Scissors

Splitting Dataset : Training = 70%, Validation = 20%, Testing = 10%.

## Preprocessing dan Modelling

- **Preprocessing Model** : resize(150,150), rescale=1./255, rotation_range=40, width_shift_range=0.2, height_shift_range=0.2, shear_range=0.2, zoom_range=0.2, horizontal_flip=True, fill_mode='nearest'
- Modelling Model CNN :

  Summary Model CNN :

  ![image](assets/summary_cnn.png)

  Graph Loss dan Accuracy Model CNN :

  ![image](assets/graph_acc_cnn.png)
  ![image](assets/graph_loss_cnn.png)

  Evaluation Matrix Model CNN :

  ![image](assets/eva_cnn.png)

  - Modelling Model MobileNetV2 :

  Summary Model MobileNetV2 :

  ![image](assets/summary_mobilenetv2.png)

  Graph Loss dan Accuracy MobileNetV2 :

  ![image](assets/graph_acc_net.png)
  ![image](assets/graph_loss_net.png)

  Evaluation Matrix Model MobileNetV2 :

  ![image](assets/eva_net.png)

  - Modelling Model ResNet50 :

  Summary Model ResNet50 :

  ![image](assets/summary_resnet50.png)

  Graph Loss dan Accuracy ResNet50 :

  ![image](assets/graph_acc_resnet.png)
  ![image](assets/graph_loss_resnet.png)

  Evaluation Matrix Model ResNet50 :

  ![image](assets/eva_resnet.png)

  ## Predict Data

- Predict Data dengan Model CNN :

1. ![image](assets/predict_cnn.png)

2. ![image](assets/predict_cnn_2.png)

3. ![image](assets/predict_cnn_3.png)

- Predict Data dengan Model MobileNetV2 :

1. ![image](assets/predict_net.png)

2. ![image](assets/predict_net_2.png)

3. ![image](assets/predict_net_3.png)

- Predict Data dengan Model ResNet50 :

1. ![image](assets/predict_resnet.png)

2. ![image](assets/predict_resnet_2.png)

3. ![image](assets/predict_resnet_3.png)

## Local Development

![image](assets/page_1.png)

![image](assets/page_2.png)
