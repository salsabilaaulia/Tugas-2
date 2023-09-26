#### Salsabila Aulia
#### 2206082190
#### PBP C

### 1.	Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah salah satu bentuk dari Django forms yang digunakan untuk membuat formulir pendaftaran atau registrasi pengguna dalam aplikasi web. Kelebihan dari penggunaan UserCreationForm adalah:
- Integrasi dengan Django User Model: Form ini sudah terintegrasi dengan model pengguna bawaan Django (User model) sehingga memudahkan pembuatan dan penyimpanan akun pengguna.
- Validasi Otomatis: Form ini melakukan validasi otomatis terhadap berbagai aspek seperti kata sandi yang cocok, email yang valid, dan lainnya.
- Fleksibilitas Kustomisasi: Meskipun form ini dapat digunakan sebagaimana adanya, Anda juga dapat menyesuaikannya sesuai dengan kebutuhan aplikasi Anda dengan mudah.
Kelemahannya adalah:
- Keterbatasan Desain: Secara default, UserCreationForm memiliki desain yang sederhana dan mungkin memerlukan penyesuaian tambahan untuk mencocokkan tampilan aplikasi Anda.
- Kustomisasi yang Rumit: Jika Anda perlu melakukan kustomisasi yang lebih kompleks, mungkin perlu penyesuaian yang lebih mendalam di luar form ini.

### 2.	Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi adalah proses verifikasi identitas pengguna. Dalam Django, ini sering terkait dengan login pengguna ke dalam aplikasi. Otorisasi adalah proses mengendalikan apa yang dapat dilakukan pengguna yang sudah diotentikasi dalam aplikasi, yaitu menentukan izin dan akses apa yang dimiliki oleh pengguna tersebut. Perbedaan utama adalah autentikasi mengidentifikasi siapa pengguna, sedangkan otorisasi mengidentifikasi apa yang diizinkan pengguna lakukan dalam aplikasi.

Keduanya penting karena autentikasi memastikan bahwa hanya pengguna yang sah yang dapat mengakses aplikasi, sementara otorisasi memastikan bahwa pengguna hanya dapat melakukan tindakan yang diizinkan sesuai peran dan izin mereka. Tanpa autentikasi, aplikasi rentan terhadap akses oleh pihak yang tidak berwenang. Tanpa otorisasi, pengguna mungkin mendapatkan akses lebih dari yang seharusnya mereka miliki.

### 3.	Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies dalam konteks aplikasi web adalah file teks kecil yang disimpan di komputer pengguna oleh browser saat berinteraksi dengan situs web. Cookies digunakan untuk menyimpan informasi sesi atau pengaturan pengguna, seperti informasi login, preferensi, atau riwayat pembelian. Django menggunakan cookies untuk mengelola data sesi pengguna dengan menyimpan token unik di cookie yang kemudian digunakan untuk mengidentifikasi sesi pengguna pada server.

### 4.	Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies secara default tidak sepenuhnya aman dalam pengembangan web. Ada beberapa risiko potensial yang harus diwaspadai:
- Cross-Site Scripting (XSS): Serangan XSS dapat memungkinkan penyerang untuk mencuri informasi dari cookies pengguna. Oleh karena itu, perlu tindakan pencegahan yang baik dalam aplikasi web untuk menghindari risiko ini.
- Cross-Site Request Forgery (CSRF): Penyerang dapat memanfaatkan cookies untuk melakukan serangan CSRF, yang dapat menyebabkan tindakan tidak diinginkan di akun pengguna tanpa izin mereka.
- Data Sensitif: Cookies dapat menyimpan data sensitif seperti token otentikasi. Penting untuk mengenkripsi data sensitif dalam cookies dan hanya menyimpan data yang benar-benar diperlukan.

### 5.	Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
#####   Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
1. membuat fungsi register pada "views.py" folder main agar formulir registrasi terbuat secara otomatis dan menghasilkan akun pengguna ketika membuat akun.
2. membuat page register di file baru "register.html" pada folder main/templates.
3. membuat fungsi login_user pada "views.py" folder main untuk mengautentikasi user yang ingin login.
4. membuat page login di file baru "login.html" pada folder main/templates.
5. membuat fungsi logout_user pada "views.py" folder main untuk menghapus sesi user yang saat ini masuk.
6. membuat page login di file baru "login.html" pada folder main/templates.
7. menambahkan path url ke dalam urlpatterns "urls.py" untuk mengakses fungsi register, login_user, logout_user.
8. merestriksi halaman main dengan menambahkan "@login_required(login_url='/login')" di atas fungsi show_main "views.py" pada folder main.

#####   Menghubungkan model Item dengan User.
1. konfigurasi "models.py" pada folder main untuk menghubungkan models nama dengan user agar tampilan menampilkan username yang sedang login.
2. konfigurasi "views.py" pada folder main agar menyimpan objek sesuai dengan user yang mensubmit item tersebut/
3. melakukan migrasi karena kita merubah model

#####   Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
1. konfigurasi fungsi login_user "views.py" pada folder main untuk menambahkan cookie bernama last_login untuk melihat kapan terakhir kali user melakukan login.
2. konfigurasi fungsi show_main "views.py" pada folder main untuk menambahkan informasi cookie last_login pada context
3. konfigurasi fungsi logout "views.py" pada folder main untuk menghapus cookies saat user logout
4. menambahkan teks sesi terakhir login pada "main.html" pada folder main/templates

#####   Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
[![Screenshot-2023-09-26-at-18-26-47.png](https://i.postimg.cc/jSTQ46XL/Screenshot-2023-09-26-at-18-26-47.png)](https://postimg.cc/crDnsnPS)
[![Screenshot-2023-09-26-at-18-26-54.png](https://i.postimg.cc/HnBHv9Md/Screenshot-2023-09-26-at-18-26-54.png)](https://postimg.cc/V0r3dM4V)
