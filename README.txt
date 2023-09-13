Tautan menuju web adaptable : https://achell-box.adaptable.app/main/

Jawaban :
1. Deskripsi singkat web sayurbox_inventory : sayurbox_inventory merupakan sebuah web dari aplikasi mobile SayurBox yang menyediakan database untuk melakukan pengecekan stok barang untuk keperluan online shopping kebutuhan pokok sehari-hari, seperti sayuran, buah-buahan hingga makanan ringan. Melalui web ini, seller dapat mengecek rincian stock, deskripsi, serta pengelolaan inventory barang mereka.


Implementasi checklist secara step-by-step:
a. Membuat sebuah proyek Django baru
Sebelum membuat proyek Django baru, saya harus melakukan beberapa hal, seperti membuat direktori baru yang saya inginkan sebagai tempat penyimpanan dan penghubung antara web dengan repository, selanjutnya menambahkan inisiasi git pada repositori tersebut. Kemudian saya membuka Command Prompt dengan alamat direktori yang sudah saya buat sebelumnya dengan nama direktorinya sayurbox_inventory. Setelah itu, saya harus membuat virtual environtment dengan perintah "python -m venv env" serta mengaktikannya dengan menggunakan perintah "env\Scripts\activate.bat". Selanjutnya, saya akan menambahkan requirements.txt beserta beberapa dependencies. Setelah dependencies tersebut terpasang, maka selanjutnya saya menjalankan perintah  "pip install -r requirements.txt" dan membuat proyek Django bernama sayurbox_inventory dengan "django-admin startproject sayurbox_inventory .".

b. Pembuatan Aplikasi main
Sebelum membuat aplikasi main dalam proyek django tersebut, saya akan menjalankan perintah "python manage.py startapp main", pada tahapan ini saya harus memastikan bahwa enviroment dalam keadaan aktif. Selanjutnya, pada file settings.py saya tambahkan'main' pada Variabel INSTALLED_APPS, sehingga akan membentuk sebuah direktori baru dengan nama main dalam sayurbox_inventory, selanjutnya di dalam direktori main tersebut saya akan membuat folder/ direktori baru dengan nama template.Di dalamnya direktori tersebut, saya akan membuat file main.html yang memuat representasi visual yang terdiri atas item yg akan ditampilkan pada web nantinya, setiap Item yang kita definisikan yang mencakup atribut name, amount, dan description serta beberapa tambahan variabel atau attribute lain yg saya tambahakan, seperti price contohnya. 

c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main
Beberapa fungsi dan modul perlu diimpor untuk proses routing di urls.py, kemudian rute baru ditambahkan pada variabel 'url patterns' yang langsung meredirect ke aplikasi 'main' yang telah dibuat. Dan pada akhirnya pengguna akan mengakses nedpoint'/items/'.

d. Membuat model Item
Dengan memanfaatkan pola desain MVT, "model" merepresentasikan struktur atau susunan data.Seperti contoh potongan kode di bawah ini yang mendefinisikan model Product dengan beberapa atribut, seperti nama, kategori, tanggal ditambahkan, harga, jumlah, dan deskripsi. Model ini akan menciptakan tabel dalam database yang sesuai dengan struktur yang didefinisikan di dalamnya. Dengan menggunakan model ini, nantinya dapat melakukan operasi database seperti penyimpanan, pengambilan, dan pembaruan data produk dalam aplikasi Django.

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    amount = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


e. Membuat model Item
Mendefinisikan Fungsi Tampilan:
Di dalam file views.py aplikasi main, saya mendefinisikan sebuah fungsi dengan nama show_main.

Integrasi dengan Model Item:
Di dalam fungsi tersebut, saya menggunakan perintah Django untuk mengambil semua entri yang ada di model Item. Ini memungkinkan kita untuk mengakses setiap item yang ada di dalam database kita.Selanjutnya, saya akan mengirimkan data item tersebut ke sebuah template HTML dengan menggunakan konteks. Konteks ini akan memudahkan kita dalam menampilkan setiap entri item pada halaman web kita.

f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
pertama-tama saya akan menambahkan URL baru. Pada file urls.py yang berada di aplikasi main, saya menambahkan sebuah path baru (path('main/', include('main.urls')),)  yang nantinya akan merespons permintaan dari pengguna untuk menampilkan daftar item.Selanjutnya, saya akan menghubungkan dengan fungsi yang terdapat di file views.py.Path ini akan mengacu pada fungsi show_main yang telah saya buat sebelumnya di views.py. Ini berarti saat URL tersebut diakses, Django akan langsung memanggil fungsi tersebut untuk mendapatkan respons yang tepat.

g. Proses Deployment di Adaptable
Untuk proses deployment, saya melakukan prosedur berdasarkan guideline dari Tutorial 0 dan melakukan setting pada perintah python manage.py migrate && gunicorn sayurbox_inventory.wsgi

2. Bagan yang berisi request client ke web aplikasi berbasis Django: 


3. Dengan menggunakan virtual environment kita dapat  mengisolasi proyek Python kita dari proyek Python lainnya. Hal ini berguna untuk mencegah timbulnya konflik antara versi modul dan pustaka yang berbeda.

Virtual environment adalah lingkungan Python terpisah yang berisi versi modul dan pustaka tertentu. Ketika kita membuat proyek Python baru, kita dapat membuat virtual environment khusus untuk proyek tersebut. Virtual environment ini akan berisi versi modul dan pustaka yang diperlukan oleh proyek.

Jika kita tidak menggunakan virtual environment, maka proyek Python kita akan menggunakan modul dan pustaka yang sama dengan sistem operasi. Hal ini dapat menyebabkan konflik jika proyek kita menggunakan versi modul dan pustaka yang berbeda dari sistem operasi.

Misalnya, jika kita memiliki proyek Python yang menggunakan Django 2.2 dan proyek Python lain yang menggunakan Django 3.0, maka proyek-proyek ini tidak akan dapat bekerja sama dengan benar jika kita tidak menggunakan virtual environment.

Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, hal ini tidak disarankan karena dapat meningkatkan risiko konflik dan masalah lainnya.

Berikut adalah beberapa manfaat menggunakan virtual environment:

- Mencegah konflik antara versi modul dan pustaka
- Menjaga keteraturan proyek Python
- Meningkatkan portabilitas proyek Python
Dengan kesimpulannya, Jika kita ingin membuat aplikasi web berbasis Django yang berkualitas, maka kita disarankan untuk menggunakan virtual environment.

4. MVC, MVT, dan MVVM adalah tiga arsitektur desain yang umum digunakan dalam pengembangan aplikasi web.

- MVC (Model-View-Controller) adalah arsitektur desain yang membagi aplikasi menjadi tiga komponen utama:
    Model: adalah komponen yang bertanggung jawab untuk menyimpan data dan logika bisnis.
    View: adalah komponen yang bertanggung jawab untuk menampilkan data kepada pengguna.
    Controller: adalah komponen yang bertanggung jawab untuk menerima input dari pengguna dan memperbarui model dan view.

- MVT (Model-View-Template) adalah arsitektur desain yang mirip dengan MVC, tetapi menggunakan template untuk menampilkan data. Template adalah file HTML yang berisi konten yang dapat ditampilkan oleh view.

- MVVM (Model-View-ViewModel) adalah arsitektur desain yang mirip dengan MVC, tetapi menggunakan view model untuk mewakili data yang ditampilkan oleh view. View model adalah kelas yang berisi data dan logika yang diperlukan untuk menampilkan data di view.

Perbedaan antara MVC, MVT, dan MVVM

Perbedaan utama antara ketiga arsitektur desain ini terletak pada cara mereka menangani data dan tampilan.

- MVC menggunakan model untuk menyimpan data dan view untuk menampilkan data. Controller bertanggung jawab untuk memperbarui model dan view.
- MVT menggunakan model untuk menyimpan data dan template untuk menampilkan data. View tidak memiliki logika apa pun.
- MVVM menggunakan model untuk menyimpan data dan view model untuk mewakili data yang ditampilkan oleh view. View model bertanggung jawab untuk memperbarui view.

Keunggulan dan kekurangan masing-masing arsitektur desain

- MVC adalah arsitektur desain yang paling umum digunakan. MVC mudah dipahami dan diterapkan, dan dapat digunakan untuk mengembangkan aplikasi web dari berbagai skala.
MVT adalah arsitektur desain yang lebih sederhana daripada MVC. MVT lebih mudah dikembangkan dan diuji, tetapi kurang fleksibel daripada MVC.
MVVM adalah arsitektur desain yang lebih kompleks daripada MVC dan MVT. MVVM dapat digunakan untuk mengembangkan aplikasi web yang lebih responsif dan efisien, tetapi lebih sulit dipelajari dan diterapkan.

