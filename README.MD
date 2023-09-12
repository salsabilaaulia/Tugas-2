Salsabila Aulia
2206082190
PBP C

https://salsa-tugas-2.adaptable.app/main/

###1.	Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
#####	Membuat sebuah proyek Django baru.
1.	Membuat folder dengan nama “Tugas 2”
2.	Klik “New Terminal at Folder”
3.	Membuat virtual environment dengan dengan menjalankan perintah “source env/bin/activate”
4.	Pada folder “Tugas 2”, membuat berkas “requirements.txt” dan menambahkan beberapa dependencies
5.	Pasang dependencies dengan perintah “pip install -r requirements.txt”
6.	Membuat projek Django Bernama tugas_2 dengan perintah “django-admin startproject tugas_2 .”
7.	Menambahkan * pada ALLOWED_HOSTS di “settings.py”
8.	Menambahkan berkas “.gitignore”

#####Membuat aplikasi dengan nama main pada proyek tersebut.
1.	Menjalankan perintah berikut “python3 manage.py startapp main”

#####Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
1.	Membuka “settings.py” dalam folder “tugas_2” dan menambahkan ‘main’ ke INSTALLED_APPS

#####Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib.
1.	Membuat “main.html” pada folder “templates” di dalam folder “main”
2.	Mengisi kode “main.html”
3.	Mengisi kode “models.py” sesuai dengan atribut yang diinginkan
4.	Migrasi model dengan menjalankan perintah “python3 manage.py makemigrations”
5.	Migrasi ke database lokal dengan perintah “python3 manage.py migrate”
6.	Memodifikasi “views.py” dan mengisi dictionary sesuai data yang ingin ditampilkan
7.	Mengubah kode “main.html” yang statis menjadi kode Django

#####Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
1.	membuat dan mengisi kode “urls.py” untuk mengatur rute URL aplikasi main dalam folder “tugas_2”
2.	membuat dan mengisi kode “urls.py” untuk mengatur rute URL proyek dalam folder “Tugas 2”

#####Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1.	Membuat repositori baru pada github Bernama “Tugas-2”
2.	Inisiasi git dengan perintah “git init” dan buat branch baru bernama main “git branch -M main”  pada folder “Tugas 2”
3.	Menghubungkan repository lokal dan github dengan perintah “git remote add origin https://github.com/salsabilaaulia/Tugas-2.git“
4.	Melakukan penyimpanan dengan perintah “git push -u origin main”
5.	Login pada Adaptable dan mebuat aplikasi baruu dengan connect ke repository “Tugas-2”
6.	Memilih Python App Template sebagai template deployment
7.	Memilih PostgreSQL sebagai tipe database
8.	Memasukkan perintah “python manage.py migrate && gunicorn tugas_2.wsgi”pada Start Command
9.	Mencentang HTTP Listener on PORT dan Deploy App untuk deployment aplikasi
10.	Aplikasi main dapat diakses pada link https://salsa-tugas-2.adaptable.app/main/

###2.	Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
[![Mind-Map-1.jpg](https://i.postimg.cc/Y2gfrLr7/Mind-Map-1.jpg)](https://postimg.cc/bdy2LJSV)

###3.	Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
- Virtual environment merupakan alat yang membantu memisahkan dependensi yang dibutuhkan oleh proyek berbeda dengan membuat environment virtual python terisolasi untuk proyek tersebut. Dengan ini, kita dapat memiliki versi yang berbeda dari pustaka yang sama di berbagai proyek tanpa konflik. Hal ini berguna karena beberapa proyek mungkin memerlukan versi pustaka yang berbeda.

- Memungkinkan untuk membuat aplikasi web berbasis Django tanpa virtual environment, tetapi ada risiko konflik antara pustaka proyek Django dengan pustaka global yang terinstal di sistem.

###4.	Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
#####MVC (Model-View-Controller)
Model: Komponen yang bertanggung jawab untuk mengelola data dan logika bisnis aplikasi. Ini adalah bagian yang mengatur bagaimana data diolah dan disimpan.
View: Komponen yang mengatur tampilan atau antarmuka pengguna. View menampilkan data dari Model dan berinteraksi dengan pengguna.
Controller: Mengelola detail yang melibatkan komunikasi antara Model dan View. Ini menangani permintaan pengguna, memprosesnya dengan Model, dan memperbarui tampilan yang sesuai.
Perbedaan utama dengan MVT dan MVVM adalah Controller berperan sebagai perantara yang mengatur komunikasi antara Model dan View.

#####MVT (Model-View-Template)
Model: Bertanggung jawab untuk mengelola data. Struktur data logis di balik keseluruhan aplikasi dan diwakili oleh database.
View: Menampilkan data dari Model kepada pengguna. View juga dapat mengatur logika bisnis tertentu seperti fungsi callback Python untuk URL tertentu yang menjelaskan data mana yang disajikan.
Template: Template adalah komponen yang mengatur tampilan HTML. Ini berbeda dengan View dalam hal bahwa Template hanya bertanggung jawab untuk tampilan, sedangkan View mengatur logika bisnis.
Perbedaan utama dengan MVC adalah penggunaan Template sebagai komponen terpisah yang mengatur tampilan HTML, sementara dalam MVC, View mengatur tampilan dan logika bisnis.

#####MVVM (Model-View-ViewModel)
Model: Seperti pada MVC dan MVT, Model mengelola data dan logika bisnis.
View: Tampilan yang diperlihatkan kepada pengguna. Bertanggung jawab untuk menampilkan data dan mengirim tindakan pengguna ke ViewModel.
ViewModel: Perantara antara Model dan View. Mengubah data dari Model menjadi format yang mudah diakses oleh View dan mengatur logika tampilan.
Perbedaan utama dengan MVC dan MVT adalah penggunaan ViewModel sebagai lapisan antara Model dan View, yang membantu memisahkan dengan jelas tampilan dan logika bisnis.

####Refrensi
https://www.geeksforgeeks.org/python-virtual-environment/
https://docs.djangoproject.com/en/3.2/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names
https://www.codeproject.com/Articles/25057/Simple-Example-of-MVC-Model-View-Controller-Design
https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel
