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

