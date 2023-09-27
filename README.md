##TUGAS 4
Nama    : Marchelina Anjani Saputri
NPM     : 2206082770
Kelas   : B

Jawab:
1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Jawaban:
Django UserCreationForm adalah kelas form bawaan Django yang digunakan untuk membuat pengguna baru. Form ini memiliki tiga bidang:

username: Nama pengguna yang akan digunakan untuk masuk ke sistem.
password1: Kata sandi yang akan digunakan untuk masuk ke sistem.
password2: Konfirmasi kata sandi.
- Kelebihan Django UserCreationForm:
a. Mudah digunakan: Form ini memiliki tiga bidang yang cukup untuk membuat pengguna baru.
b. Validasi yang kuat: Form ini memvalidasi kata sandi untuk memastikan bahwa kata sandi tersebut cukup kuat.
c. Dukungan untuk model pengguna kustom: Form ini dapat digunakan dengan model pengguna kustom.
- Kekurangan Django UserCreationForm:

a. Tidak dapat disesuaikan: Form ini tidak dapat disesuaikan dengan mudah.
b. Hanya dapat digunakan untuk membuat pengguna baru: Form ini tidak dapat digunakan untuk memperbarui pengguna yang sudah ada.
sumber : https://www.javatpoint.com/django-usercreationform

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Jawaban:
autentikasi merupakan suatu sistem untuk memastikan siapa saja yang berhak masuk untuk menggunakan sistem informasi elektronik. Otentikasi bisa berupa password, kartu akses login, atau biometrik seperti sidik jari, retina, telapak tangan, dan suara. Sedangkan, otorisasi merupakan suatu batasan untuk mengakses bagian menu tertentu pada sistem informasi elektronik, proses ini terjadi setelah proses otentikasi. Yang mana identitas pengguna akan terjamin sebelum daftar akses pengguna dengan mencari entri pada tabel serta database. 

Perbedaan autentikasi dan otorisasi sebagai berikut:

- autentikasi berguna sebagai alat untuk melakukan verifikasi data pengguna dalam memberikan perizinan kepada sistem. Namun dari sisi lain, otorisasi adalah penentuan tentang siapa saja yang harus mengakses apa saja;
- Proses autentikasi, pengguna yang diverifikasi, sedangkan pada proses otorisasi daftar pada akses penggunalah yang divalidasi, proses ini berbeda antara satu dengan lainnya;
- Proses pertama adalah autentikasi kemudian yang selanjutnya adalah otorisasi;
- Pada proses autentikasi identitas seseorang ditentukan dari data menggunakan bantuan ID pengguna serta kata sandi. Sedangkan dalam sistem otorisasilah yang memutuskan hak akses yang dimiliki oleh setiap pengguna.

Autentikasi dan otorisasi penting dalam konsep pemrograman Django karena:

- Untuk melindungi data dan sumber daya dari akses yang tidak sah. Autentikasi dan otorisasi membantu memastikan bahwa hanya pengguna yang sah yang dapat mengakses data dan sumber daya. Hal ini penting untuk melindungi data sensitif, seperti informasi keuangan atau data pribadi.
- Untuk memastikan bahwa pengguna hanya dapat mengakses data dan sumber daya yang mereka izinkan untuk diakses. Otorisasi membantu mencegah pengguna mengakses data atau sumber daya yang tidak relevan atau berbahaya bagi mereka. Hal ini dapat membantu melindungi pengguna dari diri mereka sendiri, seperti mencegah pengguna menghapus data mereka sendiri yang penting.
- Untuk mematuhi peraturan. Beberapa peraturan, seperti peraturan perlindungan data, mengharuskan organisasi untuk menerapkan kontrol keamanan yang tepat untuk melindungi data pribadi. Autentikasi dan otorisasi dapat membantu organisasi mematuhi peraturan ini.

sumber: https://diginews.id/apa-perbedaan-antara-otentikasi-dan-otorisasi/

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Jawaban:
Cookie adalah istilah untuk kumpulan informasi yang berisi rekam jejak dan aktivitas ketika menelusuri sebuah website. Secara sederhana pengertian cookies adalah kumpulan data yang diterima komputer dari sebuah situs dan mengirimkan kembali ke situs yang dikunjungi.

- Django menggunakan cookie untuk mengelola data sesi pengguna. Sesi adalah periode waktu di mana pengguna berinteraksi dengan situs web. Selama sesi, Django menyimpan informasi tentang pengguna, seperti nama pengguna, peran, dan pengaturan.

- Django menggunakan cookie untuk menyimpan ID sesi. ID sesi adalah nilai unik yang digunakan Django untuk mengidentifikasi sesi pengguna. ID sesi disimpan di cookie pengguna dan dikirim kembali ke server Django setiap kali pengguna membuat permintaan ke situs web.

Django menggunakan ID sesi untuk:

- Memverifikasi identitas pengguna saat mereka masuk ke sistem.
- Menentukan apakah pengguna telah masuk ke sistem.
- Menyimpan data pengguna selama sesi.

Berikut adalah cara Django menggunakan cookie untuk mengelola data sesi pengguna:

a. Saat pengguna masuk ke sistem, Django menghasilkan ID sesi baru.
b. Django menyimpan ID sesi di cookie pengguna.
c. Django mengirimkan cookie pengguna kembali ke browser pengguna.
d. Browser pengguna menyimpan cookie di komputer pengguna.
e. Setiap kali pengguna membuat permintaan ke situs web, browser pengguna mengirimkan cookie kembali ke server Django.
f. Django menggunakan ID sesi untuk memverifikasi identitas pengguna dan menentukan apakah pengguna telah masuk ke sistem.
g. Django menggunakan cookie untuk menyimpan data pengguna selama sesi.

sumber: https://www.cnbcindonesia.com/tech/20220325141305-37-326052/mengenal-apa-itu-cookie-browser-dan-cara-mengelolanya

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Jawaban: 

Penggunaan cookie secara default tidak sepenuhnya aman dalam pengembangan web. Ada beberapa risiko potensial yang harus diwaspadai, seperti:

- Kerentanan keamanan: Cookie dapat diretas oleh penyerang untuk mencuri informasi sensitif, seperti kata sandi atau data keuangan.
- Pelacakan pengguna: Cookie dapat digunakan untuk melacak pengguna di seluruh situs web atau bahkan di seluruh web.
- Ketidaknyamanan pengguna: Cookie dapat mengganggu pengalaman pengguna, terutama jika cookie tersebut sering digunakan atau berukuran besar.

Untuk mengurangi risiko-risiko ini, pengembang web dapat mengambil langkah-langkah berikut:

- Gunakan cookie secara bijaksana: Hanya gunakan cookie untuk menyimpan informasi yang diperlukan.
- Enkripsi cookie: Enkripsi cookie dapat membantu melindungi informasi sensitif dari peretasan.
- Setel cookie dengan benar: Setel cookie dengan nilai yang benar, seperti nama domain dan jalur yang sesuai.
- Gunakan cookie dengan aman: Hindari menyimpan informasi sensitif di cookie.

sumber: https://appmaster.io/id/blog/peran-cookie-dalam-pengembangan-web

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat Fungsi Register
Pertama buat fungsi baru di views.py dengan nama `register`.Kemudian render Fungsi tersebut pada sebuah file template html.
        
2. Membuat Fungsi Login
Setelah fungsi 'register' di render pada template html. Selanjutnya buat fungsi baru di views.py dengan nama `login_user'. Kemudian render Fungsi tersebut pada sebuah file template html 
     
3. Membuat Fungsi Logout
Selanjutnya membuat fungsi baru di views.py dengan nama `logout_user`. Kemudian render Fungsi tersebut pada sebuah file template html 
          
4. Menghubungkan product dengan user
Setelah membuat semua fungsi di atas, tambahkan URL path untuk setiap fungsi di urls.py:. Kita perlu menghubungkan model dengan user (dalam konteks ini models dengan nama Item) . Untuk menghubungkan model dengan user kita harus menambahkan model baru bernama user menggunakan foreign key  
 python
        user = models.ForeignKey(User, on_delete=models.CASCADE)
     
Setelah itu lakukan filter terhadap products pada views.py untuk memfilter product yang muncul pada aplikasi sesuai dengan user yang melakukan login   
 python
        products = Item.objects.filter(user=request.user)
     
5.  Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di local.
Buat dua akun pengguna di page register terlebih dahulu. Kemudian buat tiga dummy data untuk masing-masing akun pengguna, Data akan tersimpan di database local.

6. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
Untuk menampilkan informasi pengguna, kita perlu menambahkan sebuah fungsi untuk menambah cookie pada login_user ketika kondisi tidak none
     
python
     response.set_cookie('last_login', str(datetime.datetime.now()))
     
Selanjutnya tambahkan context baru di fungsi show main untuk melihat data last_login pada template main.html

Terakhir lakukan migrasi


//Pengimplementasian bonus
- Menambahkan Fungsi add_item:

1. Membuat fungsi add_item dalam views.py untuk menangani tindakan "Tambah" item.
2. Selanjutnya, dalam fungsi tersebut, akan diambil objek produk berdasarkan ID yang diberikan.
3. Jika ditekan button 'Tambah' , maka akan ditambahkan satu ke jumlah stok produk dan simpan perubahan tersebut di database.
4. Kemudia user akan diredirect kembali ke halaman utama (show_main) setelah tindakan selesai.

2. Membuat fungsi subtract_item:
Mirip dengan tindakan yg dilakukan pada fungsi add_item, yg membedakan hanyalah jika button "kurangi" ditekan maka akan mengurangi item sebanyak 1.

3. Membuat fungsi delete_item dalam views.py untuk menangani tindakan "Hapus" item.
Mirip dengan tindakan yg dilakukan pada fungsi add_item dan substract_item, yg membedakan hanyalah jika button "Hapus" ditekan maka akan Menghapus item secara keseluruhan dari database.

Setelah fungsi-fungsi ini didefinisikan, kemudian akan ditambahkan URL pattern yang sesuai untuk masing-masing fungsi di dalam file urls.py. Selanjutnya, dalam template HTML, ditambahkan juga  tombol "Tambah," "Kurangi," dan "Hapus" dengan tautan ke URL yang sesuai dengan menggunakan ID produk sebagai parameter.


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
Langkah-langkah : 

a. Membuat File forms.py:
   - Pertama buat file forms.py dalam direktori main.
   - kemudian definisikan sebuah form dengan menggunakan field yang berasal dari model Product yang telah dideklarasikan dalam file item.py

b. Membuat Fungsi create_product pada filei views.py:
   - Kedua buat sebuah fungsi baru di file views.py dengan nama fungsi create_product yang akan merender tampilan form dari file forms.py ke dalam template HTML.

c. Membuat File HTML Sebagai Template:
   - Ketiga buat file HTML yang akan digunakan sebagai template untuk form yang dirender oleh fungsi create_product di langkah sebelumnya.

d. Membuat Button di Halaman Utama:
   - Keempat, pada halaman utama HTML, saya menambahkan sebuah button atau link yang akan mengarahkan user ke halaman dengan form untuk menambahkan produk.

e. Membuat Fungsi untuk Tampilan HTML/XML/JSON:
   - Selanjutnya, saya membuat empat fungsi tambahan untuk menampilkan data produk dalam format HTML, XML, JSON, dan juga format khusus per ID. 
   - Untuk menghasilkan format XML dan JSON, perlu membuat fungsi serializer yang akan mengonversi data dari database ke dalam format yang sesuai.

f. Membuat Fungsi untuk Tampilan XML/JSON per ID:
   - Keenam, buat fungsi yang serupa dengan langkah sebelumnya untuk tampilan XML dan JSON per ID produk. Namun, perlu menerapkan filter berdasarkan primary key (pk) untuk mengambil data yang sesuai.

g. Routing:
   - Ketujuh, saya menambahkan URL routing untuk semua fungsi yang telah dibuat pada file urls.py. Ini akan menentukan bagaimana setiap fungsi dapat diakses melalui URL.
   - Setelah melakukan routing, kita dapat menguji atau melihat setiap fungsi yang telah dibuat dengan mengaksesnya melalui localhost 

5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

![2ab6127b8fd0364fd27ea67c2d36dfc206ea6a3f](https://github.com/marchelinaanjani2/sayurbox_inventory/assets/119769840/e1dfb204-211e-4eb7-8c9e-9aef8bed4e72)
![09f5eead3fe61ab41875b14fa9394362e6b275ad](https://github.com/marchelinaanjani2/sayurbox_inventory/assets/119769840/3e59d83c-839a-40b1-a731-fc96f8179ebd)
![56c9c3a409fbcf05857b54e0b921b1274d0b2330](https://github.com/marchelinaanjani2/sayurbox_inventory/assets/119769840/189d394c-3aae-4b7a-beea-087fa8e39c2f)
![0118afcfab6cea70afae5a66cb8b18abb89e9e18](https://github.com/marchelinaanjani2/sayurbox_inventory/assets/119769840/f11e559a-8528-4462-bd9a-00f5187ba8e5)
![519f3958f6f86ddeacb6c2b1bee8785e8445185e](https://github.com/marchelinaanjani2/sayurbox_inventory/assets/119769840/87abbd2f-e9b9-4dd7-8721-297268780d96)

![57621e5f9b23a60dac77a39aff5876f53ad7f99a
![3500601390636b00c810797260e996010be6725e](https://github.com/marchelinaanjani2/sayurbox_inventory/assets/119769840/5fecdf47-a16e-4fc0-bf98-dd082c5ba121)
](https://github.com/marchelinaanjani2/sayurbox_inventory/assets/11
![af2fa182c44cc93254ca153076a98835b41b52b3](https://github.com/marchelinaanjani2/sayurbox_inventory/assets/119769840/f8266ccd-a919-4522-8912-46904abd6aa1)
9769840/ebd83b7e-c5a8-4480-b4cd-dbd5c0ded220)
![ea15125472166b23567efc152580a5235078179c](https://github.com/marchelinaanjani2/sayurbox_inventory/assets/119769840/52571447-8552-4541-8733-ded17f484c86)






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
![bagan pbp mvt](https://github.com/marchelinaanjani2/sayurbox_inventory/assets/119769840/76699548-d55d-4efc-b146-a59ef2afeb02)


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

