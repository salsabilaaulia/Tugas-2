#### Salsabila Aulia
#### 2206082190
#### PBP C

### 1.	Apa perbedaan antara form POST dan form GET dalam Django?
#####   Pengiriman Data
POST    : Digunakan untuk mengirim data ke server. Biasanya untuk data penting seperti password. Jika berhasil akan mereturn kode status HTTP 201.
GET     : Digunakan untuk membaca/mengambil data dari server web. Jika berhasil akan mereturn HTTP
kode status 200.

#####   Visibilitas
POST    : Data dapat dilihat oleh semua orang di URL.
GET     : Data tidak ditampilkan di URL.

#####   Caching
POST    : Tidak dapat di-cache.
GET     : Dapat di-cache.

#####   Restriksi
POST    : Tidak ada. Data biner juga diperbolehkan.
GET     : Saat menambahkan data ke URL, panjang URL dibatasi (panjang URL maksimum adalah 2048 karakter). Hanya karakter ASCII yang diperbolehkan.

#####   Sekuritas
POST: Kurang aman dibandingkan POST karena data yang dikirimkan merupakan bagian dari URL.
GET: Sedikit lebih aman daripada GET karena parameternya tidak disimpan dalam history browser atau log server web.

### 2.	Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
HTML    : HTML digunakan untuk memformat dan menampilkan data, lebih fokus pada tampilan dan interaksi dengan pengguna.
XML     : XML adalah bahasa markup dan format file untuk menyimpan, mentransmisikan, dan merekonstruksi data arbitrer. Elemen data diberi tanda kurung dapat ditentukan pengguna agar sesuai dengan struktur data yang disimpan dan dikirimkan. Hal ini memberikan fleksibilitas yang besar dalam desain aplikasi penanganan data. XML umum digunakan untuk pertukaran data melalui Internet.
JSON    : JSON adalah format file format pertukaran data yang menggunakan teks yang mudah dibaca untuk menyimpan dan mengirimkan objek data yang terdiri dari "kunci-nilai". Digunakan terutama untuk mengirimkan data antara server dan aplikasi web seperti dalam pertukaran data antara aplikasi web dan sebagai format respons API.

### 3.	Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- memiliki format yang ringan dan mudah dibaca
- memiliki jumlah karakter yang jauh lebih rendah sehingga mengurangi overhead dalam transfer data.
- format yang umum digunakan dalam respons API yang digunakan oleh aplikasi web modern. 
- tidak memerlukan definisi tipe data yang membuatnya lebih fleksibel dalam merepresentasikan data yang beragam.
- menyimpan semua data dalam array sehingga transfer data menjadi lebih mudah.
- memiliki jangkauan luas untuk kompatibilitas browser dengan sistem operasi.

### 4.	Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
#####   Membuat input form untuk menambahkan objek model pada app sebelumnya.
1. membuat kerangka umum "base.html" pada folder baru "Tugas 2"/templates
2. konfigurasi "settings.py" pada folder tugas_2 dan mengubah variabel TEMPLATES agar berkas "base.html" terdeteksi sebagai berkas template
3. konfigurasi "main.html" pada folder main
4. membuat form input data "forms.py" pada folder main dan menambahkan model dan field dari model tersebut
5. konfigurasi urls.py dan menambahkan path url
6. buat "create_product.html" pada folder templates/main untuk membuat input form
7. konfigurasi main.html untuk menampilkan data dalam format html

#####   Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
1. membuat fungsi create_product, show_xml, show_json yang memiliki parameter request dan show_xml_by_id, show_json_by_id memiliki parameter request dan id dan mereturn HTTPResponse yang berisi parameter data hasil query yang sudah diserialisasi setiap format

#####   Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
1. konfigurasi "urls.py" pada folder main dan mengimport 5 fungsi tersebut
2. menambahkan path url ke dalam urlpatterns agar dapat mengakses 5 fungsi tersebut

### 5.	Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
######create-product (html)
[![Screenshot-2023-09-19-at-11-07-32.png](https://i.postimg.cc/ZR2t6hVL/Screenshot-2023-09-19-at-11-07-32.png)](https://postimg.cc/zbCc14mL)

######xml
[![Screenshot-2023-09-19-at-11-07-48.png](https://i.postimg.cc/05KqPbyX/Screenshot-2023-09-19-at-11-07-48.png)](https://postimg.cc/9z2kBXTy)

######json
[![Screenshot-2023-09-19-at-11-07-56.png](https://i.postimg.cc/ZKkzR49b/Screenshot-2023-09-19-at-11-07-56.png)](https://postimg.cc/JtQ2Ywcv)

######xml by id
[![Screenshot-2023-09-19-at-11-08-02.png](https://i.postimg.cc/FzStZn6X/Screenshot-2023-09-19-at-11-08-02.png)](https://postimg.cc/PvdFfKhS)

######json by id
[![Screenshot-2023-09-19-at-11-08-08.png](https://i.postimg.cc/Bn4WTpcR/Screenshot-2023-09-19-at-11-08-08.png)](https://postimg.cc/F7Wnmj6x)

##### Referensi
https://www.w3schools.com/tags/ref_httpmethods.asp
https://www.deltaxml.com/blog/xml/whats-the-relationship-between-xml-json-html-and-the-internet/
https://www.geeksforgeeks.org/json/