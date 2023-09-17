##TUGAS 3

Nama    : Marchelina Anjani Saputri
NPM     : 2206082770
Kelas   : B

Jawab :
1. Apa perbedaan antara form POST dan form GET dalam Django?
Jawaban : 
Perbedaan utama antara keduanya adalah cara data dikirim dan bagaimana data tersebut diolah di server. Berikut adalah perbedaan antara form POST dan form GET dalam Django:

- Metode Pengiriman Data:

POST: Dalam form POST, data formulir dikirim sebagai bagian dari permintaan HTTP yang tersembunyi dari pandangan pengguna. Data dikirimkan dalam body permintaan HTTP. Ini membuatnya lebih aman dan sesuai untuk mengirim data sensitif atau data yang berpotensi besar.
GET: Dalam form GET, data formulir dikirim sebagai parameter dalam URL. Ini berarti data akan terlihat di URL, yang membuatnya kurang aman dan tidak sesuai untuk data sensitif atau data besar. Namun, URL dengan parameter dapat dengan mudah dibookmark atau dibagikan.

- Keamanan:

POST: Form POST lebih aman karena data tidak terlihat di URL. Ini cocok untuk mengirim kata sandi, informasi pribadi, atau data lain yang sensitif.
GET: Form GET kurang aman karena data terlihat di URL, yang dapat dilihat oleh siapa saja yang memiliki akses ke histori peramban atau log server. Data sensitif tidak boleh dikirim menggunakan metode GET.

- Batas Kapasitas Data:

POST: Form POST dapat mengirimkan jumlah data yang lebih besar karena data dikirim dalam body permintaan HTTP.
GET: Form GET memiliki batasan kapasitas data yang lebih kecil karena data dikirim sebagai parameter URL. Sebagian besar peramban memiliki batasan panjang URL.

- Caching:

POST: Permintaan POST tidak akan dicache oleh peramban atau server proxy secara default. Ini berarti hasilnya selalu segar.
GET: Permintaan GET cenderung dicache oleh peramban dan server proxy, yang dapat menyebabkan hasil yang diperbarui tidak terlihat jika Anda mengakses URL yang sama dengan parameter yang sama.

- Idempoten:

POST: Permintaan POST tidak idempoten, artinya mengirim permintaan yang sama beberapa kali dapat menghasilkan perubahan atau aksi yang berbeda setiap kali.
GET: Permintaan GET idempoten, artinya mengirim permintaan yang sama beberapa kali tidak akan mengubah status atau data di server.

sumber : https://makinrajin.com/blog/perbedaan-post-dan-get/

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
Jawaban : 
XML (eXtensible Markup Language), JSON (JavaScript Object Notation), dan HTML (Hypertext Markup Language) adalah tiga format yang berbeda yang digunakan untuk mengirim dan menyimpan data di berbagai konteks. Berikut adalah perbedaan utama antara ketiganya dalam konteks pengiriman data:

- Tujuan Utama :
   - XML : XML dirancang untuk mendefinisikan, mengirim, dan menyimpan data struktural. Ini digunakan dalam berbagai konteks, termasuk konfigurasi, pertukaran data, penyimpanan data, dan lebih banyak lagi.
   - JSON : JSON adalah format yang digunakan untuk pertukaran data antara aplikasi web dan server, serta untuk menyimpan dan menerjemahkan data dalam bahasa pemrograman. JSON sangat terkait dengan JavaScript, tetapi juga dapat digunakan dengan berbagai bahasa pemrograman lainnya.
   - HTML : HTML adalah bahasa markup yang digunakan untuk membuat halaman web. Tujuan utamanya adalah untuk menampilkan konten dan struktur halaman web, termasuk teks, gambar, tautan, dan lebih banyak elemen tampilan.

- Sintaks :
   - XML : XML menggunakan sintaksis yang ketat dan hierarkis dengan elemen yang dibungkus dalam tag. Setiap elemen memiliki tag pembuka dan penutup, dan data sering disusun dalam struktur pohon.
   - JSON : JSON menggunakan sintaksis yang lebih ringkas dan sederhana. Data disusun dalam bentuk pasangan "kunci-nilai" (key-value pairs), dan tipe data yang umum seperti objek, array, string, angka, boolean, dan null didukung.
   - HTML : HTML memiliki sintaksis yang mirip dengan XML, tetapi tujuannya berbeda. HTML digunakan untuk membuat tampilan halaman web, dengan elemen yang diatur dalam struktur berbasis tag.

- Pengunaan :
   - XML : XML umumnya digunakan untuk pertukaran data terstruktur antara aplikasi yang berbeda, konfigurasi, penyimpanan data, dan format data yang rumit. Contoh penggunaannya termasuk SOAP (Simple Object Access Protocol) dalam layanan web, konfigurasi berkas, dan RSS/Atom feeds.
   - JSON : JSON digunakan untuk pertukaran data antara browser dan server dalam pengembangan web (AJAX), penyimpanan data dalam berkas konfigurasi, API REST, serta dalam pemrograman JavaScript.
   - HTML : HTML digunakan untuk membuat halaman web yang dapat dilihat dan diakses oleh pengguna melalui peramban web.

- Ekosistem :
   - XML : XML memiliki berbagai macam spesifikasi dan teknologi terkait seperti XSLT (Extensible Stylesheet Language Transformations) dan XML Schema. Ini digunakan dalam berbagai aplikasi seperti SOAP, RSS, dan banyak lagi.
   - JSON : JSON memiliki dukungan kuat dalam pengembangan web, terutama dalam konteks penggunaan JavaScript. Banyak bahasa pemrograman modern memiliki dukungan bawaan atau pustaka untuk parsing dan menghasilkan data JSON.
   - HTML : HTML adalah bagian utama dari ekosistem web dan digunakan bersama CSS (Cascading Style Sheets) dan JavaScript untuk membuat dan mengelola halaman web interaktif.

Sumber : https://aws.amazon.com/id/compare the-difference-between-json-xml/

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Jawaban : 
JSON (JavaScript Object Notation) sering digunakan dalam pertukaran data antara aplikasi web modern karena memiliki beberapa keunggulan seperti berikut : 

- Sintaks sederhana : JSON memiliki sintaksis yang ringkas dan sederhana. Data disusun dalam bentuk pasangan "kunci-nilai" (key-value pairs), yang membuatnya mudah dibaca dan ditulis oleh manusia. Ini juga membuatnya efisien dalam hal ukuran data yang dikirimkan melalui jaringan.

-Partial Parsing : JSON mendukung pembacaan parsial atau bagian-bagian dari data. Ini berarti aplikasi dapat mengambil hanya bagian yang diperlukan dari respons JSON tanpa perlu mengambil seluruh dokumen, menghemat bandwidth dan waktu.

- Pemahaman dalam berbagai bahas : JSON adalah format data independen bahasa, yang berarti itu tidak terkait dengan bahasa pemrograman tertentu. Ini mendukung berbagai bahasa pemrograman dan mudah digunakan dalam pengembangan web, terutama dengan JavaScript.

- Interoperabilitas : JSON bekerja dengan baik dalam konteks pertukaran data antara berbagai platform dan sistem. Ini berarti kita dapat menggunakan JSON untuk menghubungkan aplikasi web dengan berbagai layanan, bahkan jika mereka ditulis dalam bahasa yang berbeda.

- Dukungan untuk tipe data dasar : JSON mendukung tipe data dasar seperti objek (object), array, string, angka, boolean, dan null. Ini cukup fleksibel untuk menggambarkan berbagai jenis data.

- Dukungan dalam javascript : JSON secara alami terintegrasi dengan JavaScript, yang menjadikannya pilihan yang sangat kuat untuk pertukaran data antara peramban web dan server. Objek JavaScript dapat dikonversi menjadi JSON dan sebaliknya dengan mudah.

- Penggunaan dalam API REST : Banyak layanan web modern yang menggunakan arsitektur REST menggunakan JSON sebagai format data untuk permintaan dan respons. Ini telah menjadi standar de facto dalam pengembangan API web.

JSON efisien, mudah digunakan, dan sangat cocok untuk lingkungan web yang terus berkembang.

Sumber : https://midtrans.com/id/blog/json-format

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban : 
... 

5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.






---------------------------------------------------------------------------------------------------------------------------------------------
##TUGAS 2

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
![bagan pbp](https://github.com/marchelinaanjani2/sayurbox_inventory/assets/119769840/9629d4d0-fe41-4110-aa85-a86812a335eb)

Penjelasan : 
Bagan tersebut menggambarkan aliran proses request-response dalam aplikasi web berbasis Django. Proses dimulai dengan interaksi pengguna di browser, yang mengirimkan permintaan HTTP ke server Django melalui URL routing yang telah didefinisikan. Server Django kemudian mengarahkan permintaan ke view yang sesuai, di mana logika aplikasi, interaksi dengan model data, dan rendering template HTML terjadi. Setelah rendering, halaman web HTML yang telah dibuat dikirimkan sebagai respons HTTP kembali ke browser, yang akhirnya menampilkan halaman web yang dihasilkan kepada pengguna.

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

