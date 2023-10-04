#### Salsabila Aulia
#### 2206082190
#### PBP C
#### Tugas 5

### 1.	Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
Element selector adalah salah satu jenis selector dalam CSS yang digunakan untuk memilih elemen-elemen HTML berdasarkan jenis atau nama elemennya. 
Dengan menggunakan selector ini, kita dapat dengan mudah mengaplikasikan gaya ke semua elemen dengan jenis yang sama dalam dokumen HTML. Misalnya, jika kita ingin mengubah warna teks pada semua elemen p menjadi biru, kita dapat menggunakan selector p.


### 2.	Jelaskan HTML5 Tag yang kamu ketahui.
- header: Digunakan untuk mengelompokkan elemen-elemen yang merupakan bagian atas (header) dari sebuah dokumen atau bagian dari dokumen. Biasanya digunakan untuk judul, logo, navigasi, dan elemen header lainnya.
- nav: Menandakan elemen yang berisi navigasi situs web, seperti menu atau tautan ke berbagai halaman atau bagian dalam situs.
- div: Mengelompokkan dan mengatur elemen-elemen HTML lainnya di dalamnya.
- button: Membuat tombol interaktif yang dapat digunakan oleh pengguna untuk berbagai tujuan dalam halaman web.
- table: Menggambarkan struktur dasar tabel. 

### 3.	Jelaskan perbedaan antara margin dan padding.
Margin:
- Margin adalah ruang di luar elemen: Margin adalah jarak antara tepi luar elemen HTML dengan elemen-elemen lain di sekitarnya.
- Memengaruhi tata letak elemen: Margin memengaruhi tata letak elemen terhadap elemen-elemen tetangga. Jika Anda memberikan elemen margin atas, maka elemen tersebut akan diberi jarak di atas elemen tetangganya.
- Tidak memiliki latar belakang atau warna: Margin adalah area transparan dan biasanya tidak memiliki latar belakang atau warna.

Padding:
- Padding adalah ruang di dalam elemen: Padding adalah jarak antara batas elemen dan kontennya. Dalam kata lain, itu adalah ruang di dalam elemen tersebut.
- Memengaruhi tampilan konten: Padding memengaruhi penampilan konten di dalam elemen. Jika Anda memberikan elemen padding atas, maka konten di dalam elemen tersebut akan diberi jarak dari tepi atas elemen tersebut.
- Dapat memiliki latar belakang atau warna: Padding dapat memiliki latar belakang atau warna yang berbeda daripada elemen itu sendiri, sehingga memungkinkan untuk memberi elemen efek visual.

### 4.	Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

Tailwind CSS:
- Utility-First Approach: Tailwind CSS adalah pendekatan "Utility-First," yang berarti menggabungkan kelas utilitas ke elemen HTML. Ini memungkinkan membuat tampilan yang sangat disesuaikan dan efisien.
- Konfigurasi Lebih Fleksibel: Tailwind CSS memungkinkan Anda untuk menyesuaikan konfigurasi dan gaya tampilan secara ekstensif melalui file konfigurasi JavaScript.
- Ringan: Tailwind CSS memiliki ukuran yang lebih kecil daripada Bootstrap, sehingga dapat menghasilkan halaman web yang lebih cepat.
- Tidak Memiliki Desain Bawaan: Tailwind CSS tidak memiliki desain bawaan seperti Bootstrap, sehingga perlu merancang tampilan sendiri dari awal.

Bootstrap:
- Component-Based: Bootstrap adalah framework yang berbasis komponen. Dapat dengan mudah menggunakan komponen-komponen siap pakai seperti navigasi, kartu, formulir, dll.
- Desain Bawaan: Bootstrap memiliki desain bawaan yang sangat baik dan estetis. Jadi, jika Anda membutuhkan tampilan yang terlihat bagus dengan sedikit usaha, Bootstrap bisa menjadi pilihan yang baik.
- Lebih Mudah untuk Pemula: Bootstrap lebih mudah digunakan untuk pemula karena banyak komponennya sudah ada, dan Anda hanya perlu menggabungkannya.
- Lebih Tidak Fleksibel: Bootstrap kurang fleksibel daripada Tailwind CSS dalam hal penyesuaian tampilan.

Kapan Menggunakan Bootstrap atau Tailwind CSS:

- Bootstrap: Jika membutuhkan prototipe cepat, tidak memiliki banyak waktu untuk merancang tampilan dari awal, atau ingin tampilan yang sudah estetis, Bootstrap bisa menjadi pilihan yang baik. Juga, jika kita pemula dalam pengembangan web, Bootstrap menyediakan banyak komponen siap pakai.
- Menggunakan Tailwind CSS: Jika ingin kontrol yang lebih besar atas tampilan, ingin membangun tampilan yang sangat disesuaikan, atau jika lebih berpengalaman dalam CSS, Tailwind CSS bisa menjadi pilihan yang lebih baik.Memberikan fleksibilitas yang lebih besar dalam mendesain tampilan.

### 5.	Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Di dalam bagian <head> dari base.html, menambahkan link referensi CSS Bootstrap dan JavaScript Bootstrap
2. Konfigurasi pengaturan STATIC_URL dan STATICFILES_DIRS untuk mengonfigurasi penanganan file statis (CSS, JS, gambar, dll.) pada settings.py
3. Buka template HTML untuk halaman Login, Register, Main, dan Create Product dan menambahkan kelas CSS Bootstrap ke elemen HTML