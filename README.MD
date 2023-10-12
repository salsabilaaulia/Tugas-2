#### Salsabila Aulia
#### 2206082190
#### PBP C
#### Tugas 6

### 1.	Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
- Synchronous Programming (Blocking): Tugas-tugas dieksekusi satu per satu dalam urutan yang ditentukan. Ketika satu tugas dijalankan, program akan menunggu sampai tugas tersebut selesai sebelum melanjutkan ke tugas berikutnya. Ini berarti tugas-tugas dalam mode sinkron memblokir eksekusi program sampai tugas saat ini selesai.

- Asynchronous Programming (Non-blocking): Tugas-tugas dieksekusi secara bersamaan tanpa harus menunggu tugas sebelumnya selesai. sehingga program tidak diblokir dan bisa melanjutkan eksekusi tugas-tugas lain sementara menunggu operasi asinkron selesai. Berguna dalam situasi di mana operasi yang memerlukan waktu seperti mengambil data dari jaringan atau sistem file dapat memperlambat aplikasi jika dilakukan secara sinkron.

### 2.	Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Paradigma event-driven programming adalah pendekatan pemrograman di mana program merespon kejadian (events) yang terjadi. Di JavaScript, ini berarti Anda menentukan tindakan atau fungsi yang harus dijalankan ketika suatu event terjadi. 
''document.getElementById("button_add").onclick = addProduct;''
Dalam kode ini, kita menghubungkan fungsi addProduct untuk dijalankan ketika tombol dengan ID "button_add" diklik. Merupakan contoh dari paradigma event-driven, di mana tindakan dijalankan dalam respons terhadap event tertentu.

### 3.	Jelaskan penerapan asynchronous programming pada AJAX.
Operasi AJAX, seperti pengambilan data dari server, memerlukan waktu yang tidak dapat diprediksi. Kita ingin mencegah aplikasi dari pemblokiran saat menunggu respons dari server. Dengan menggunakan JavaScript's fetch API, Anda melakukan permintaan AJAX secara asinkron dan menentukan fungsi yang akan dijalankan ketika permintaan selesai.

### 4.	Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
Fetch API: API standar dalam JavaScript modern untuk membuat permintaan jaringan asinkron. Memiliki sintaksis yang bersih dan merupakan bagian dari spesifikasi JavaScript sehingga tidak perlu mengunduh atau memasang library tambahan. Ini memungkinkan lebih banyak kontrol dan fleksibilitas dalam mengelola permintaan jaringan. Namun, penggunaan yang lebih rendah dari Fetch API mungkin memerlukan penulisan kode lebih banyak.

jQuery: jQuery adalah library JavaScript yang telah ada selama beberapa waktu. Menyederhanakan banyak tugas pemrograman JavaScript dengan metode yang mudah digunakan. Dalam konteks AJAX, jQuery memiliki metode AJAX yang dapat digunakan dengan mudah, sehingga mengurangi jumlah kode yang harus ditulis. Namun, karena sekarang ada alternatif bawaan seperti Fetch API, beberapa pengembang lebih memilih untuk tidak lagi menggunakan jQuery, terutama jika hanya untuk operasi AJAX.

Jika kita memerlukan banyak fitur atau ingin lebih banyak kontrol, Fetch API adalah pilihan yang baik. Jika ingin kesederhanaan dan kecepatan pengembangan, jQuery mungkin cocok.

### 5.	Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. membuat function get product dengan AJAX pada views.py dan menyesuaikan variable sesuai models
2. membuat get product json untuk mengembalikan data input user ajax pada views.py
3. membuat routing url get product json dan create ajax pada urls.py
4. mengubah card pada main.html dengan script
5. menambahkan modal form create product
6. modifikasi script agar data yg diinput dari modal form dapat tersimpan