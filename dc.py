# from django.db import models
# import requests
# memabng boleh di python deklarasi kelas didalam kelas ?
# Ya, dalam Python kita dapat mendeklarasikan kelas di dalam kelas. Ini disebut sebagai konsep nested class . Berikut adalah contoh kode sederhana yang menunjukkan bagaimana mendeklarasikan kelas di dalam kelas di Python:


# class KelasLuas:
#     def __init__(self, panjang, lebar):
#         self.panjang = panjang
#         self.lebar = lebar
#         self.luas = self.HitungLuas()

#     def HitungLuas(self):
#         class LuasKelasDalam:
#             def __init__(self):
#                 pass

#             def Hitung(self):
#                 return self.luas

#         return self.panjang * self.lebar

#     def PrintLuas(self):
#         print("Luas persegi panjang:", self.luas)


# # Membuat objek KelasLuas
# kl = KelasLuas(5, 10)
# kl.PrintLuas()
# Dalam contoh ini, terdapat kelas LuasKelasDalam yang dideklarasikan di dalam kelas KelasLuas. Pada bahasa pemrograman Python, kita dapat membuat kelas di dalam kelas dan mengaksesnya sesuai dengan aturan yang berlaku.

# lass Service(models.Model):
#     class ServiceObjects(models.Manager):
#         def get_queryset(self):
#             return super().get_queryset().filter(status='published')
#     options = (
#         ('draft', 'Draft'),
#         ('published', 'Published'),
#     )
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     image = models.ImageField(
#         _('Image'), upload_to=upload_services)
#     features = models.JSONField()
#     status = models.CharField(
#         max_length=10, choices=options, default='published')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     objects = models.Manager()  # The default manager.
#     ServiceObjects = ServiceObjects()  # The custom manager.

#     class Meta:
#         ordering = ['-created_at']

#     def __str__(self):
#         return self.name

#     def delete(self, *args, **kwargs):
#         self.image.delete()
#         super().delete(*args, **kwargs) kalo ini kok ada class meta dan class serviceobject ?
# Dalam contoh kode yang Anda berikan, terdapat definisi kelas Service yang merupakan model Django. Di dalam kelas Service, terdapat definisi kelas lain yang disebut ServiceObjects. Ini adalah contoh penggunaan nested class di Python.

# Kelas ServiceObjects adalah subclass dari models.Manager yang memiliki metode khusus get_queryset yang digunakan untuk mengatur query set agar hanya mengembalikan objek dengan status 'published'. Ini adalah contoh dari penggunaan custom manager di Django.

# Selain itu, di dalam kelas Service, terdapat definisi kelas Meta yang digunakan untuk mengatur metadata terkait model Service, seperti pengaturan pengurutan data dengan ordering = ['-created_at'].

# Jadi, penggunaan nested class di sini adalah untuk mendefinisikan custom manager(ServiceObjects) dan metadata(Meta) terkait model Service dalam Django.

# apakah bedanya django filter dengan django model manager, apakah django model manager ada dokumentasinya ?
# Django Filter dan Django Model Manager adalah dua konsep yang berbeda dalam framework Django.

# Django Model Manager:

# Django Model Manager adalah objek yang menyediakan antarmuka untuk melakukan kueri terhadap data dalam model Django.
# Model Manager digunakan untuk menentukan cara objek model diperoleh dari database, misalnya dengan metode .all(), .filter(), .get(), dan sebagainya.
# Model Manager memungkinkan Anda untuk menentukan operasi database yang khusus untuk model Anda, seperti membuat custom query sets.
# Model Manager biasanya didefinisikan di dalam kelas model Django.
# Contoh penggunaan Model Manager adalah dalam mengatur default objects dan custom queryset.
# Django Filter:

# Django Filter merupakan aplikasi pihak ketiga yang memungkinkan Anda membuat filter query secara dinamis pada data model Django.
# Django Filter memungkinkan Anda untuk membuat form filter yang menghasilkan query set sesuai dengan filter yang diberikan.
# Django Filter membantu mempermudah proses pencarian dan filterisasi data pada tampilan aplikasi web.
# Django Filter tidak sama dengan Model Manager karena fungsinya lebih ke arah filtering dan mempermudah proses pencarian data.
# Untuk dokumentasi resmi terkait dengan Model Manager, Anda dapat membacanya di bagian dokumentasi Django yang terkait dengan "Customizing QuerySets" pada tautan berikut: https: // docs.djangoproject.com/en/3.2/topics/db/managers/

# Sementara itu, untuk dokumentasi resmi terkait dengan Django Filter, Anda dapat membacanya di situs resmi Django Filter: https: // django-filter.readthedocs.io/en/stable/

# Dengan membaca dokumentasi resmi, Anda dapat memahami secara mendalam tentang perbedaan dan penggunaan Model Manager dan Django Filter dalam proyek Django Anda.

# coba berikan contoh model django manager yang di request datanya melalui api
# Berikut adalah contoh sederhana dari sebuah model Django yang menggunakan model manager untuk mengambil data melalui API. Dalam contoh ini, kita akan menggunakan library requests untuk melakukan HTTP request ke API eksternal dan mendapatkan data yang kemudian dapat disimpan dalam model Django:


# class APIManager(models.Manager):
#     def get_data_from_api(self):
#         api_url = 'http://example.com/api/data/'
#         response = requests.get(api_url)

#         if response.status_code == 200:
#             data = response.json()
#             return data
#         else:
#             return None


# class MyModel(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

#     objects = APIManager()  # Menggunakan custom manager

#     def populate_data_from_api(self):
#         data = self.objects.get_data_from_api()
#         if data:
#             self.name = data.get('name')
#             self.description = data.get('description')
#             self.save()


# Dalam contoh di atas, kita mendefinisikan sebuah model manager APIManager yang memiliki metode get_data_from_api yang akan melakukan HTTP GET request ke URL API tertentu dan mengembalikan data JSON yang diterima. Kemudian, kita memiliki model MyModel dengan dua bidang name dan description. Model ini menggunakan model manager custom APIManager.

# Metode populate_data_from_api pada model MyModel akan memanggil metode get_data_from_api dari model manager untuk mendapatkan data dari API, kemudian akan memperbarui bidang name dan description dengan data yang diterima sebelum menyimpannya ke database.

# Pastikan Anda menyesuaikan URL API, struktur data yang diterima, dan pemrosesan data sesuai dengan kebutuhan praktis yang Anda miliki.

# from .models import MyModel
# from django.shortcuts import render
# cadi bagaimana cara menggunakan model ini apakah harus seperti ini misal di dalam views Mymodel.papulate_data_from_api()
# Ya, Anda dapat menggunakan model dan model manager yang telah Anda definisikan dalam views Django untuk melakukan pemanggilan data dari API. Berikut contoh cara menggunakannya di dalam views:


# def my_view(request):
#     # Memanggil metode populate_data_from_api dari model MyModel
#     my_model_instance = MyModel()
#     my_model_instance.populate_data_from_api()

#     # Melakukan query untuk mengambil data dari model
#     my_data = MyModel.objects.all()

#     return render(request, 'my_template.html', {'my_data': my_data})


# Dalam contoh di atas, kita membuat sebuah view my_view yang akan dipanggil saat URL tertentu diakses. Di dalam view tersebut, kita membuat instance dari model MyModel dan kemudian memanggil metode populate_data_from_api untuk mengambil data dari API kemudian menyimpannya ke database.

# Setelah melakukan pemanggilan data dari API dan menyimpannya ke database, kita kemudian melakukan query untuk mengambil semua data dari model MyModel dan mengirimkannya ke template untuk ditampilkan.

# Pastikan untuk menyesuaikan contoh di atas dengan kebutuhan aplikasi Django Anda, termasuk menambahkan penanganan error dan validasi data yang diperoleh dari API.

# bukanya objects pada sintaks Mymodel.objects.all() tidak bisa lagi karena sudah objects telah tergantikan dengan Apimanager() pada sintaks  objects = APIManager()
# Maaf atas kekeliruan sebelumnya. Jika Anda telah menetapkan model manager kustom untuk model Anda seperti objects = APIManager(), maka Anda harus menggunakan model manager tersebut untuk melakukan query pada model tersebut. Berikut adalah contoh cara mengakses data model menggunakan model manager kustom:


# def my_view(request):
#     # Memanggil metode populate_data_from_api dari model MyModel
#     my_model_instance = MyModel()
#     my_model_instance.populate_data_from_api()

#     # Mengambil data menggunakan model manager APIManager
#     my_data = MyModel.objects.get_data_from_api()
#     # Atau jika menggunakan filter
#     # my_filtered_data = MyModel.objects.filter_data_from_api()

#     return render(request, 'my_template.html', {'my_data': my_data})


# Dalam contoh di atas, kita pemanggilan data dari API dilakukan dengan menggunakan metode get_data_from_api() dari model manager APIManager yang telah ditetapkan sebelumnya untuk model MyModel. Anda juga dapat menyesuaikan metode di model manager sesuai dengan kebutuhan Anda, misalnya menambahkan metode filter untuk melakukan filter pada data yang diperoleh dari API.

# Pastikan untuk menyesuaikan contoh di atas dengan model manager kustom dan implementasi lain yang Anda miliki dalam proyek Django Anda. Jika ada pertanyaan lebih lanjut, jangan ragu untuk bertanya.

# jadi sya tidak bisa menggunakan seperti method get, filter, dan all karna telah objects sebelumnya tela tergantikan
# Sebenarnya, Anda masih dapat menggunakan method get, filter, all, dan metode lainnya pada model manager kustom Anda. Anda dapat menentukan metode tersebut di dalam model manager Anda dan mereka akan tetap dapat digunakan seperti pada model manager bawaan Django.

# Berikut contoh bagaimana Anda bisa menggunakan method get dan all pada model manager kustom APIManager dalam views:


# def my_view(request):
#     # Menggunakan method get dari model manager untuk mendapatkan data dari API
#     my_model_instance = MyModel.objects.get(pk=1)

#     # Menyimpan data yang telah diterima dari API ke database
#     my_model_instance.populate_data_from_api()

#     # Menggunakan method all dari model manager untuk mendapatkan semua data dari model
#     my_data = MyModel.objects.all()

#     return render(request, 'my_template.html', {'my_data': my_data})


# Dalam contoh di atas, kita masih dapat menggunakan method get dan all pada model manager kustom APIManager untuk mendapatkan data dari API dan mengambil semua data dari model. Pastikan untuk menyesuaikan implementasi method-method dalam model manager sesuai dengan kebutuhan dan logika aplikasi Anda.

# Jika Anda memiliki kebutuhan khusus atau pertanyaan tambahan, jangan ragu untuk bertanya.

# Pastikan ini sesuai dengan nama serializer Anda
# from .serializers import AccountSerializer
# from django.http import JsonResponse
# from .forms import CustomUserCreationForm
# from .views import register_view, login_view, logout_view
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CustomUser
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from .views import login_view, logout_view, register_view
# from django.shortcuts import redirect
# from django.contrib.auth import logout
# from .forms import RegisterForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login as auth_login
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm
# from django import forms
# from django.contrib.auth.models import User
# from .views import ArticleListCreateAPIView
# from rest_framework import generics, pagination, status
# from .serializers import ArticleSerializer
# from .models import Article
# from rest_framework import generics, status
# from rest_framework import generics
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from django.urls import path, include
# from django.contrib import admin
# from .views import getlist
# from django.urls import path
# from .serializers import LoginSerializer
# from .models import Login
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.response import Response
# from rest_framework import generics, pagination
# Berikut adalah penjelasan detail sintaks model Django yang diberikan:

# Fungsi upload_services
# python
# Salin kode


# def upload_services(instance, filename):
#     ext = filename.split('.')[-1]
#     name = '{:%Y%m%d_%H%M%S}_{}'.format(datetime.now(), instance.name)
#     return 'services/{}.{}'.format(name, ext)


# Fungsi ini digunakan untuk menentukan path upload untuk file gambar yang diunggah ke model Service.

# ext = filename.split('.')[-1]: Mengambil ekstensi file dari filename.
# name = '{:%Y%m%d_%H%M%S}_{}'.format(datetime.now(), instance.name): Membuat nama file baru dengan format timestamp(tahun, bulan, tanggal, jam, menit, detik) yang diikuti oleh nama instance.
# return 'services/{}.{}'.format(name, ext): Mengembalikan path lengkap untuk penyimpanan file, yang akan berada di folder services dengan nama file yang baru dibentuk.
# Kelas Service
# python
# Salin kode
# class Service(models.Model):


# Kelas ini adalah model Django yang mendefinisikan tabel Service dalam database. Model ini memiliki beberapa atribut dan metode khusus.

# Subclass ServiceObjects
# python
# Salin kode


# class ServiceObjects(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(status='published')


# ServiceObjects adalah custom manager untuk model Service.
# get_queryset: Metode ini mengoverride get_queryset dari models.Manager dan mengembalikan queryset yang hanya berisi instance dengan status = 'published'.
# Atribut Model
# python
# Salin kode
# options = (
#     ('draft', 'Draft'),
#     ('published', 'Published'),
# )
# options adalah tuple yang mendefinisikan pilihan untuk status dari service.

# python
# Salin kode
# name = models.CharField(max_length=255)
# description = models.TextField()
# image = models.ImageField(_('Image'), upload_to=upload_services)
# features = models.JSONField()
# status = models.CharField(max_length=10, choices=options, default='published')
# created_at = models.DateTimeField(auto_now_add=True)
# updated_at = models.DateTimeField(auto_now=True)
# name: Field karakter dengan panjang maksimum 255 karakter.
# description: Field teks untuk deskripsi layanan.
# image: Field gambar yang menggunakan fungsi upload_services untuk menentukan path upload.
# features: Field JSON untuk menyimpan fitur-fitur dalam format JSON.
# status: Field karakter dengan panjang maksimum 10 karakter yang menggunakan pilihan dari options dan default published.
# created_at: Field datetime yang otomatis diisi dengan waktu saat instance dibuat.
# updated_at: Field datetime yang otomatis diupdate dengan waktu saat instance diupdate.
# Managers
# python
# Salin kode
# objects = models.Manager()  # The default manager.
# ServiceObjects = ServiceObjects()  # The custom manager.
# objects: Manager default untuk model Service.
# ServiceObjects: Custom manager yang hanya mengembalikan services dengan status published.
# Meta Class
# python
# Salin kode


# class Meta:
#     ordering = ['-created_at']


# ordering: Mengatur urutan default untuk queryset model ini, diurutkan berdasarkan created_at secara descending.
# Magic Methods
# python
# Salin kode


# def __str__(self):
#     return self.name


# __str__: Metode ini mengembalikan representasi string dari instance model, dalam hal ini nama dari service.
# Custom Delete Method
# python
# Salin kode


# def delete(self, *args, **kwargs):
#     self.image.delete()
#     super().delete(*args, **kwargs)


# delete: Metode ini mengoverride metode delete default untuk memastikan bahwa file gambar yang terkait juga dihapus dari sistem file ketika instance dihapus.
# Kesimpulan
# Model Service mendefinisikan struktur tabel layanan dalam database dengan beberapa field termasuk nama, deskripsi, gambar, fitur, status, waktu pembuatan, dan waktu pembaruan. Model ini juga memiliki custom manager ServiceObjects yang hanya menampilkan layanan dengan status published. Selain itu, model ini mengatur path upload untuk gambar menggunakan fungsi upload_services dan memastikan file gambar dihapus dari sistem file ketika instance dihapus.


# class getlist (generics.ListCreateAPIView):
#     queryset = Login.objects.all()
#     serializer_class = LoginSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     search_fields = ['name']
#     pagination_class = pagination.LimitOffsetPagination

#     def list(self, reuest):
#         get_all = self.get_queryset()
#         page = self.paginate_queryset(self.queryset)
#         ser = self.get_serializer(data=get_all, many=True)
#         if page is not None:
#             if ser.is_valid():
#                 return self.get_paginated_response(ser.data)
#         else:
#             return Response(ser.data) tolon perbaiki dan bagaimana saya menambahkan parameter limit offset url di api


# ChatGPT
# Untuk memperbaiki kode yang diberikan dan menambahkan parameter limit dan offset ke URL API, Anda perlu membuat beberapa perubahan pada metode list dan memastikan bahwa pagination diatur dengan benar.

# Berikut adalah versi yang diperbaiki dari kode Anda:

# python
# Salin kode


# class getlist(generics.ListCreateAPIView):
#     queryset = Login.objects.all()
#     serializer_class = LoginSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     search_fields = ['name']
#     pagination_class = pagination.LimitOffsetPagination

#     def list(self, request):
#         queryset = self.get_queryset()
#         page = self.paginate_queryset(queryset)

#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)


# Penjelasan
# Import Statements:

# Mengimpor Response dari rest_framework.response.
# Mengimpor filter SearchFilter dan OrderingFilter dari rest_framework.filters.
# Mengimpor DjangoFilterBackend dari django_filters.rest_framework.
# Mengimpor model Login dan serializer LoginSerializer dari modul lokal Anda.
# Class Definition:

# queryset: Mengatur queryset default untuk semua objek Login.
# serializer_class: Mengatur serializer yang digunakan untuk objek Login.
# filter_backends: Mengatur backend filter untuk pencarian, penyaringan, dan pengurutan.
# search_fields: Menentukan bidang yang bisa dicari.
# pagination_class: Mengatur kelas pagination yang digunakan(dalam hal ini LimitOffsetPagination).
# Method list:

# Mendapatkan queryset menggunakan self.get_queryset().
# Mencoba mempaginate queryset dengan self.paginate_queryset(queryset).
# Jika pagination berhasil(page is not None), serializer diterapkan pada halaman yang dipaginate dan respon paginated dikembalikan.
# Jika pagination tidak berhasil, serializer diterapkan pada seluruh queryset dan respon data dikembalikan.
# Menambahkan Parameter limit dan offset ke URL API
# Dengan menggunakan pagination.LimitOffsetPagination, parameter limit dan offset akan secara otomatis tersedia di URL API Anda. Contoh URL dengan parameter tersebut:

# bash
# Salin kode
# /api/login?limit = 10 & offset = 20
# limit: Menentukan jumlah maksimum objek yang dikembalikan dalam satu respon.
# offset: Menentukan jumlah objek yang dilewati sebelum mulai mengembalikan objek dari database.
# Tidak ada konfigurasi tambahan yang diperlukan untuk menambahkan parameter ini, karena kelas LimitOffsetPagination dari Django REST Framework sudah mendukungnya secara default.

# bagaimana cara saya mengatur dibagian url pathnya ?
# ChatGPT
# Untuk mengatur URL path di Django, Anda perlu menambahkan entri ke file urls.py proyek atau aplikasi Anda. Di sini, Anda akan menggunakan view getlist yang telah Anda buat. Berikut adalah langkah-langkah untuk melakukannya:

# 1. Buat atau Update urls.py di Aplikasi Anda
# Jika belum ada, buat file urls.py di direktori aplikasi Anda. Jika sudah ada, Anda cukup menambahkannya. Berikut adalah contohnya:

# urls.py di Aplikasi
# python
# Salin kode

# urlpatterns = [
#     path('login/', getlist.as_view(), name='login-list'),
# ]
# 2. Include URLconf Aplikasi di URLconf Proyek
# Anda juga perlu memastikan bahwa URLconf dari aplikasi Anda di-include di URLconf proyek utama. Buka file urls.py di direktori proyek utama Anda dan tambahkan include untuk URLconf aplikasi.

# urls.py di Proyek
# python
# Salin kode

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # Gantilah 'nama_aplikasi' dengan nama aplikasi Anda
#     path('api/', include('nama_aplikasi.urls')),
# ]
# 3. Pastikan View Anda Benar
# View getlist Anda sudah diatur dengan benar untuk mendukung pagination dan filter seperti yang sudah dijelaskan sebelumnya. Jadi tidak ada perubahan tambahan yang diperlukan pada view tersebut.

# Contoh Lengkap
# Berikut adalah contoh lengkap bagaimana file urls.py di proyek dan aplikasi Anda akan terlihat:

# urls.py di Aplikasi(nama_aplikasi/urls.py)
# python
# Salin kode

# urlpatterns = [
#     path('login/', getlist.as_view(), name='login-list'),
# ]
# urls.py di Proyek(proyek_utama/urls.py)
# python
# Salin kode

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # Pastikan nama aplikasi sesuai
#     path('api/', include('nama_aplikasi.urls')),
# ]
# Dengan konfigurasi ini, endpoint API Anda untuk mendapatkan daftar login akan tersedia di:

# perl
# Salin kode
# http: // <domain-anda > /api/login/
# Anda bisa menggunakan parameter limit dan offset untuk pagination, seperti:

# ruby
# Salin kode
# http: // <domain-anda > /api/login/?limit = 10 & offset = 20
# Ini akan mengambil 10 objek login dimulai dari objek ke-21.

# CSRF verification failed. Request aborted.

# You are seeing this message because this site requires a CSRF cookie when submitting forms. This cookie is required for security reasons, to ensure that your browser is not being hijacked by third parties. ini kenapaya di django
# ChatGPT
# Pesan "CSRF verification failed. Request aborted." muncul karena Django memiliki mekanisme keamanan yang disebut CSRF(Cross-Site Request Forgery) yang melindungi aplikasi web dari serangan CSRF. CSRF memastikan bahwa permintaan yang dikirim ke server berasal dari pengguna yang sah dan bukan dari pihak ketiga yang berbahaya.

# Untuk memperbaiki masalah ini, Anda perlu memastikan bahwa permintaan yang dikirim ke server menyertakan token CSRF yang valid. Berikut adalah beberapa solusi untuk masalah ini, tergantung pada jenis permintaan yang Anda kirim(formulir HTML, permintaan AJAX, dll.):

# 1. Menambahkan CSRF Token pada Formulir HTML
# Jika Anda menggunakan formulir HTML, pastikan Anda menyertakan token CSRF dalam formulir tersebut. Django menyediakan tag template { % csrf_token % } untuk tujuan ini.

# Contoh Template HTML:
# html
# Salin kode
# <form method = "post" action = "/your-url/" >
#     { % csrf_token % }
#     <!-- Fields form Anda - ->
#     <button type = "submit" > Submit < /button >
# </form >
# 2. Menambahkan CSRF Token pada Permintaan AJAX
# Jika Anda menggunakan permintaan AJAX(misalnya dengan jQuery), Anda perlu menyertakan token CSRF dalam header permintaan Anda. Berikut adalah contoh menggunakan jQuery:

# Contoh dengan jQuery:
# javascript
# Salin kode
# function getCookie(name) {
#     var cookieValue = null;
#     if (document.cookie & & document.cookie != = '') {
#         var cookies = document.cookie.split(';');
#         for (var i=0; i < cookies.length; i++) {
#             var cookie = cookies[i].trim();
#             if (cookie.substring(0, name.length + 1) === (name + '=')) {
#                 cookieValue = decodeURIComponent(
#                     cookie.substring(name.length + 1));
#                 break;
#             }
#         }
#     }
#     return cookieValue;
# }
# var csrftoken = getCookie('csrftoken');

# $.ajaxSetup({
#     beforeSend: function(xhr, settings) {
#         if (!/^(GET | HEAD | OPTIONS | TRACE)$/.test(settings.type) & & !this.crossDomain) {
#             xhr.setRequestHeader("X-CSRFToken", csrftoken);
#         }
#     }
# });

# // Contoh permintaan AJAX
# $.ajax({
#     url: "/your-url/",
#     type: "POST",
#     data: {
#         // data Anda di sini
#     },
#     success: function(response) {
#         // Tanggapan sukses
#     },
#     error: function(xhr, errmsg, err) {
#         // Tanggapan error
#     }
# });
# 3. Nonaktifkan CSRF untuk Endpoint Tertentu
# Jika Anda ingin menonaktifkan verifikasi CSRF untuk endpoint tertentu(misalnya, untuk endpoint API yang digunakan oleh aplikasi pihak ketiga), Anda dapat melakukannya dengan menambahkan dekorator @ csrf_exempt pada view tersebut. Namun, ini hanya disarankan jika Anda yakin bahwa endpoint tersebut aman tanpa perlindungan CSRF.

# Contoh View dengan @ csrf_exempt:
# python
# Salin kode


# @method_decorator(csrf_exempt, name='dispatch')
# class getlist(generics.ListCreateAPIView):
#     queryset = Login.objects.all()
#     serializer_class = LoginSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     search_fields = ['name']
#     pagination_class = pagination.LimitOffsetPagination

#     def list(self, request):
#         queryset = self.get_queryset()
#         page = self.paginate_queryset(queryset)

#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)


# 4. Menambahkan Middleware CSRF di Django Settings
# Pastikan middleware CSRF diaktifkan di pengaturan Django Anda. Middleware ini biasanya diaktifkan secara default, tetapi pastikan tidak ada yang menonaktifkannya.

# Contoh di settings.py:
# python
# Salin kode
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',  # Pastikan middleware ini aktif
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
# Dengan memastikan langkah-langkah di atas, Anda dapat mengatasi masalah verifikasi CSRF di aplikasi Django Anda.


# class article (generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     pagination_class = pagination.LimitOffsetPagination
#     serializer_class = ArticelSerelizer

#     def list(self, request):
#         objects = self.get_queryset()
#         serelizer = self.get_serializer(data=objects, many=True)
#         page = self.paginate_queryset(objects)
#         if page is not None:
#             return self.get_paginated_response(serelizer.data)
#         return Response(serelizer.data)

#     def create(self, request, *args, **kwargs):
#         try:
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             self.perform_create(serializer)
#             response = {
#                 "status": status.HTTP_200_OK,
#                 "message": "Article Created",
#                 "data": serializer.data
#             }
#             return Response(response)
#         except Exception as e:
#             response = {
#                 "status": status.HTTP_400_BAD_REQUEST,
#                 "message": "Article Created : Failer",
#                 "data": "Null"
#             }
#             return Response(response) bagaimana cara saya mengatasinya dibagian ini kenapa crsf token aborted padahal cors origin true pada bagian setting ?


# ChatGPT
# CSRF token yang gagal diverifikasi dapat terjadi meskipun pengaturan CORS sudah benar. Hal ini biasanya disebabkan oleh permintaan POST yang tidak menyertakan token CSRF atau token tersebut tidak sesuai. Untuk mengatasi masalah ini, pastikan bahwa token CSRF disertakan dalam setiap permintaan POST.

# Berikut adalah langkah-langkah untuk mengatasi masalah ini:

# 1. Pastikan CSRF Middleware Aktif
# Pastikan middleware CSRF aktif di pengaturan Django(settings.py):

# python
# Salin kode
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',  # Pastikan middleware ini aktif
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
# 2. Menambahkan CSRF Token pada Permintaan AJAX
# Jika Anda menggunakan AJAX untuk mengirim permintaan POST, pastikan bahwa token CSRF disertakan dalam header permintaan. Berikut adalah contoh menggunakan jQuery:

# Contoh dengan jQuery:
# javascript
# Salin kode
# function getCookie(name) {
#     var cookieValue = null;
#     if (document.cookie & & document.cookie != = '') {
#         var cookies = document.cookie.split(';');
#         for (var i=0; i < cookies.length; i++) {
#             var cookie = cookies[i].trim();
#             if (cookie.substring(0, name.length + 1) === (name + '=')) {
#                 cookieValue = decodeURIComponent(
#                     cookie.substring(name.length + 1));
#                 break;
#             }
#         }
#     }
#     return cookieValue;
# }
# var csrftoken = getCookie('csrftoken');

# $.ajaxSetup({
#     beforeSend: function(xhr, settings) {
#         if (!/^(GET | HEAD | OPTIONS | TRACE)$/.test(settings.type) & & !this.crossDomain) {
#             xhr.setRequestHeader("X-CSRFToken", csrftoken);
#         }
#     }
# });

# // Contoh permintaan AJAX
# $.ajax({
#     url: "/api/articles/",
#     type: "POST",
#     data: {
#         // data Anda di sini
#     },
#     success: function(response) {
#         // Tanggapan sukses
#     },
#     error: function(xhr, errmsg, err) {
#         // Tanggapan error
#     }
# });
# 3. Gunakan Dekorator @ csrf_exempt untuk View Tertentu
# Jika Anda yakin bahwa endpoint tertentu aman tanpa perlindungan CSRF, Anda dapat menonaktifkan verifikasi CSRF untuk endpoint tersebut menggunakan dekorator @ csrf_exempt. Namun, ini hanya disarankan jika Anda yakin bahwa endpoint tersebut aman tanpa perlindungan CSRF.

# Contoh View dengan @ csrf_exempt:
# python
# Salin kode


# @method_decorator(csrf_exempt, name='dispatch')
# class ArticleListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     pagination_class = pagination.LimitOffsetPagination

#     def list(self, request):
#         objects = self.get_queryset()
#         page = self.paginate_queryset(objects)
#         serializer = self.get_serializer(page, many=True)
#         if page is not None:
#             return self.get_paginated_response(serializer.data)
#         return Response(serializer.data)

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         try:
#             serializer.is_valid(raise_exception=True)
#             self.perform_create(serializer)
#             response = {
#                 "status": status.HTTP_201_CREATED,
#                 "message": "Article Created",
#                 "data": serializer.data
#             }
#             return Response(response)
#         except Exception as e:
#             response = {
#                 "status": status.HTTP_400_BAD_REQUEST,
#                 "message": "Article Creation Failed",
#                 "data": "Null"
#             }
#             return Response(response)


# 4. Pastikan Anda Mengirim Permintaan POST dengan CSRF Token
# Jika Anda mengirim permintaan POST dari klien lain(misalnya Postman atau aplikasi front-end lain), pastikan untuk menyertakan token CSRF di header permintaan.

# Contoh dengan Postman:
# Dapatkan token CSRF dari respons GET pada halaman atau endpoint yang memuat token CSRF.
# Tambahkan token CSRF ke header permintaan POST:
# makefile
# Salin kode
# X-CSRFToken: < token_csrf_anda >
# Dengan langkah-langkah ini, Anda seharusnya dapat mengatasi masalah CSRF verification failed. Pastikan token CSRF selalu disertakan dalam permintaan POST untuk memastikan permintaan Anda diverifikasi dengan benar oleh server.

# APIView.as_view() takes 1 positional argument but 2 were given
# ChatGPT
# Pesan error "APIView.as_view() takes 1 positional argument but 2 were given" biasanya terjadi ketika Anda mencoba mengoverride dispatch method atau menerapkan decorator seperti @ csrf_exempt dengan cara yang salah.

# Untuk memperbaiki masalah ini, Anda dapat menggunakan @ method_decorator dengan cara yang benar. Berikut adalah cara mengatasi masalah ini:

# 1. Gunakan @ method_decorator dengan Benar
# Pastikan Anda menggunakan @ method_decorator dengan csrf_exempt dengan benar pada view Anda.

# Berikut adalah contoh perbaikan untuk class view Anda:

# python
# Salin kode


# @method_decorator(csrf_exempt, name='dispatch')
# class ArticleListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     pagination_class = pagination.LimitOffsetPagination

#     def list(self, request):
#         queryset = self.get_queryset()
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         try:
#             serializer.is_valid(raise_exception=True)
#             self.perform_create(serializer)
#             response = {
#                 "status": status.HTTP_201_CREATED,
#                 "message": "Article Created",
#                 "data": serializer.data
#             }
#             return Response(response)
#         except Exception as e:
#             response = {
#                 "status": status.HTTP_400_BAD_REQUEST,
#                 "message": "Article Creation Failed",
#                 "data": "Null"
#             }
#             return Response(response)


# 2. Pastikan URL Path diatur dengan Benar
# Tambahkan endpoint untuk view Anda di urls.py dengan benar:

# python
# Salin kode

# urlpatterns = [
#     path('articles/', ArticleListCreateAPIView.as_view(),
#          name='article-list-create'),
# ]
# Penjelasan:
# Import Statements:

# Mengimpor csrf_exempt dari django.views.decorators.csrf.
# Mengimpor method_decorator dari django.utils.decorators.
# Mengimpor generics, pagination, dan status dari rest_framework.
# Mengimpor Response dari rest_framework.response.
# Mengimpor filter SearchFilter dan OrderingFilter dari rest_framework.filters.
# Mengimpor DjangoFilterBackend dari django_filters.rest_framework.
# Mengimpor model Article dan serializer ArticleSerializer dari modul lokal Anda.
# Class Definition:

# queryset: Mengatur queryset default untuk semua objek Article.
# serializer_class: Mengatur serializer yang digunakan untuk objek Article.
# filter_backends: Mengatur backend filter untuk pencarian, penyaringan, dan pengurutan.
# pagination_class: Mengatur kelas pagination yang digunakan(dalam hal ini LimitOffsetPagination).
# Method list:

# Mendapatkan queryset menggunakan self.get_queryset().
# Mencoba mempaginate queryset dengan self.paginate_queryset(queryset).
# Jika pagination berhasil(page is not None), serializer diterapkan pada halaman yang dipaginate dan respon paginated dikembalikan.
# Jika pagination tidak berhasil, serializer diterapkan pada seluruh queryset dan respon data dikembalikan.
# Method create:

# Menerima data dari request dan melakukan validasi menggunakan serializer.
# Jika validasi berhasil, data disimpan dan respon sukses dikembalikan.
# Jika terjadi kesalahan, respon error dikembalikan.
# Dengan langkah-langkah ini, Anda seharusnya dapat mengatasi error "APIView.as_view() takes 1 positional argument but 2 were given" dan memastikan CSRF token diverifikasi dengan benar.

# sintaks membuat django auth ?
# ChatGPT
# Membuat autentikasi di Django melibatkan beberapa langkah, termasuk konfigurasi dasar, pembuatan model pengguna, pembuatan tampilan untuk login, logout, dan registrasi, serta pengaturan URL dan template. Berikut adalah langkah-langkah umum untuk membuat autentikasi di Django:

# 1. Instalasi dan Konfigurasi Awal
# Pastikan Anda memiliki Django terinstal dan proyek Django yang siap digunakan. Jika belum, Anda dapat menginstalnya dengan:

# bash
# Salin kode
# pip install django
# Buat proyek baru jika belum ada:

# bash
# Salin kode
# django-admin startproject myproject
# cd myproject
# Buat aplikasi baru untuk mengelola autentikasi:

# bash
# Salin kode
# python manage.py startapp accounts
# Tambahkan aplikasi accounts ke dalam INSTALLED_APPS di settings.py:

# python
# Salin kode
# INSTALLED_APPS = [
#     ...
#     'accounts',
#     # Diperlukan jika menggunakan allauth atau autentikasi lain yang berbasis situs
#     'django.contrib.sites',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
# ]
# Tambahkan middleware yang diperlukan di settings.py:

# python
# Salin kode
# MIDDLEWARE = [
#     ...
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
# 2. Model Pengguna
# Gunakan model pengguna default yang disediakan oleh Django atau buat model pengguna kustom jika diperlukan. Untuk menggunakan model pengguna default:

# python
# Salin kode
# 3. Formulir Autentikasi
# Buat formulir untuk login dan registrasi pengguna. Misalnya, di accounts/forms.py:

# Formulir Login
# python
# Salin kode


# class LoginForm(AuthenticationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# Formulir Registrasi
# python
# Salin kode


# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True, widget=forms.EmailInput(
#         attrs={'class': 'form-control'}))
#     username = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')


# 4. Tampilan(Views)
# Buat tampilan untuk login, logout, dan registrasi di accounts/views.py:

# Login View
# python
# Salin kode


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'accounts/login.html', {'form': form})


# Register View
# python
# Salin kode


# def register_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             return redirect('home')
#     else:
#         form = RegisterForm()
#     return render(request, 'accounts/register.html', {'form': form})


# Logout View
# python
# Salin kode


# def logout_view(request):
#     logout(request)
#     return redirect('home')


# 5. URL Patterns
# Tambahkan URL patterns di accounts/urls.py:

# python
# Salin kode

# urlpatterns = [
#     path('login/', login_view, name='login'),
#     path('logout/', logout_view, name='logout'),
#     path('register/', register_view, name='register'),
# ]
# Tambahkan include untuk URL accounts di myproject/urls.py:

# python
# Salin kode

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/', include('accounts.urls')),
#     # Tambahkan untuk menggunakan tampilan autentikasi default Django
#     path('', include('django.contrib.auth.urls')),
# ]
# 6. Template
# Buat template untuk login dan registrasi. Misalnya, buat folder templates/accounts / dan tambahkan file login.html dan register.html:

# Template Login(login.html)
# html
# Salin kode
# <!DOCTYPE html >
# <html >
# <head >
#     <title > Login < /title >
# </head >
# <body >
#     <h2 > Login < /h2 >
#     <form method = "post" >
#         { % csrf_token % }
#         {{form.as_p}}
#         <button type = "submit" > Login < /button >
#     </form >
# </body >
# </html >
# Template Register(register.html)
# html
# Salin kode
# <!DOCTYPE html >
# <html >
# <head >
#     <title > Register < /title >
# </head >
# <body >
#     <h2 > Register < /h2 >
#     <form method = "post" >
#         { % csrf_token % }
#         {{form.as_p}}
#         <button type = "submit" > Register < /button >
#     </form >
# </body >
# </html >
# 7. Uji Aplikasi
# Jalankan server Django dan uji aplikasi autentikasi Anda:

# bash
# Salin kode
# python manage.py runserver
# Buka browser dan akses URL http: // 127.0.0.1: 8000/accounts/login / dan http: // 127.0.0.1: 8000/accounts/register / untuk menguji login dan registrasi.

# Dengan langkah-langkah ini, Anda telah membuat sistem autentikasi dasar di Django. Anda dapat menyesuaikan lebih lanjut sesuai kebutuhan aplikasi Anda.

# apakah kita bisa mengganti django auth model dengan model buatan kita sendiri ?
# ChatGPT
# Ya, Anda bisa mengganti model autentikasi bawaan Django dengan model pengguna kustom yang Anda buat sendiri. Ini dikenal sebagai penggunaan model pengguna kustom. Proses ini melibatkan beberapa langkah, termasuk mendefinisikan model pengguna kustom, memperbarui pengaturan, dan memastikan bahwa semua komponen aplikasi mengenali model pengguna baru ini.

# Berikut adalah langkah-langkah untuk mengganti model autentikasi bawaan Django dengan model pengguna kustom:

# 1. Buat Aplikasi Baru(opsional)
# Jika belum memiliki aplikasi untuk mengelola model pengguna, Anda bisa membuat aplikasi baru:

# bash
# Salin kode
# python manage.py startapp accounts
# 2. Definisikan Model Pengguna Kustom
# Buat model pengguna kustom di accounts/models.py. Anda dapat meng-extend AbstractBaseUser dan PermissionsMixin untuk membuat model pengguna kustom.

# python
# Salin kode


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email


# 3. Perbarui Pengaturan
# Tambahkan model pengguna kustom Anda ke pengaturan Django di settings.py:

# python
# Salin kode
# AUTH_USER_MODEL = 'accounts.CustomUser'
# 4. Buat dan Terapkan Migrasi
# Buat migrasi untuk model pengguna kustom dan terapkan:

# bash
# Salin kode
# python manage.py makemigrations accounts
# python manage.py migrate
# 5. Perbarui Formulir Autentikasi
# Buat formulir kustom untuk registrasi dan autentikasi pengguna di accounts/forms.py:

# Formulir Registrasi
# python
# Salin kode


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'first_name', 'last_name')


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'first_name', 'last_name')


# Formulir Login
# Anda bisa menggunakan AuthenticationForm bawaan Django atau membuat formulir kustom jika diperlukan.

# 6. Perbarui Admin
# Daftarkan model pengguna kustom di admin Django di accounts/admin.py:

# python
# Salin kode


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'first_name', 'last_name', 'is_staff']
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff',
#          'is_superuser', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)


# admin.site.register(CustomUser, CustomUserAdmin)
# 7. URL Patterns dan Views
# Tambahkan URL patterns untuk login dan registrasi di accounts/urls.py:

# python
# Salin kode

# urlpatterns = [
#     path('register/', register_view, name='register'),
#     path('login/', login_view, name='login'),
#     path('logout/', logout_view, name='logout'),
# ]
# Tambahkan include untuk URL accounts di myproject/urls.py:

# python
# Salin kode

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/', include('accounts.urls')),
#     # Tambahkan untuk menggunakan tampilan autentikasi default Django
#     path('', include('django.contrib.auth.urls')),
# ]
# 8. Views
# Buat views untuk login, logout, dan registrasi di accounts/views.py:

# Register View
# python
# Salin kode


# def register_view(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             return redirect('home')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'accounts/register.html', {'form': form})


# Login View
# python
# Salin kode


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'accounts/login.html', {'form': form})


# Logout View
# python
# Salin kode


# def logout_view(request):
#     logout(request)
#     return redirect('home')


# 9. Template
# Buat template untuk login dan registrasi. Misalnya, buat folder templates/accounts / dan tambahkan file login.html dan register.html:

# Template Login(login.html)
# html
# Salin kode
# <!DOCTYPE html >
# <html >
# <head >
#     <title > Login < /title >
# </head >
# <body >
#     <h2 > Login < /h2 >
#     <form method = "post" >
#         { % csrf_token % }
#         {{form.as_p}}
#         <button type = "submit" > Login < /button >
#     </form >
# </body >
# </html >
# Template Register(register.html)
# html
# Salin kode
# <!DOCTYPE html >
# <html >
# <head >
#     <title > Register < /title >
# </head >
# <body >
#     <h2 > Register < /h2 >
#     <form method = "post" >
#         { % csrf_token % }
#         {{form.as_p}}
#         <button type = "submit" > Register < /button >
#     </form >
# </body >
# </html >
# Dengan langkah-langkah ini, Anda telah mengganti model autentikasi bawaan Django dengan model pengguna kustom. Anda dapat menyesuaikan lebih lanjut sesuai kebutuhan aplikasi Anda.


# class register (generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = accountserelizers

#     def list(self, request, *args, **kwargs):
#         try:
#             query = self.get_queryset()
#             ser = self.get_serializer(data=query, many=True)
#             return Response(ser.data)
#         except:
#             return JsonResponse({'messsage': 'Failed Catch Data'})

#     def create(self, request, *args, **kwargs):
#         try:
#             account_serializer = self.get_serializer()
#             account_serializer(data=request.data)
#             if account_serializer.is_valid(raise_exception=True):
#                 self.perform_create(account_serializer)
#             return Response({'message': 'Succes Create Data'})
#         except:
#             return Response({'message': 'Failed Create Data'}) tolong beri tahu saya dimana errornya ?


# ChatGPT
# Ada beberapa kesalahan dalam kode Anda yang menyebabkan tampilan register tidak berfungsi sebagaimana mestinya. Berikut adalah perbaikan yang diperlukan:

# List Method: Anda tidak perlu memvalidasi data saat melakukan list view karena Anda hanya perlu mengambil dan menyerialisasi queryset. Selain itu, Anda perlu memanggil metode .data setelah membuat instance serializer dengan queryset.

# Create Method: Anda membuat instance serializer dengan data = request.data dengan cara yang salah. Anda harus menginisialisasi serializer dengan self.get_serializer(data=request.data). Juga, pastikan untuk memanggil .save() pada serializer yang valid untuk menyimpan data ke database.

# Berikut adalah versi yang diperbaiki dari kode Anda:

# python
# Salin kode


# class RegisterView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = AccountSerializer

#     def list(self, request, *args, **kwargs):
#         try:
#             query = self.get_queryset()
#             serializer = self.get_serializer(query, many=True)
#             return Response(serializer.data)
#         except Exception as e:
#             return JsonResponse({'message': 'Failed to fetch data', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def create(self, request, *args, **kwargs):
#         try:
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             self.perform_create(serializer)
#             return Response({'message': 'Success: Data created'}, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response({'message': 'Failed to create data', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Penjelasan:
# List Method:

# Line 8: Anda mengambil queryset dan menyerialisasinya dengan parameter many = True untuk mengindikasikan bahwa queryset berisi banyak objek.
# Line 10: Kembalikan data yang telah diserialisasi.
# Line 12: Tambahkan str(e) untuk menangkap pesan error yang lebih spesifik dan status 500_INTERNAL_SERVER_ERROR.
# Create Method:

# Line 16: Inisialisasi serializer dengan data=request.data.
# Line 17: Validasi data dan lempar exception jika tidak valid.
# Line 18: Panggil self.perform_create(serializer) untuk menyimpan data.
# Line 19: Kembalikan respon sukses dengan status 201_CREATED.
# Line 21: Tangkap exception dan kembalikan pesan error yang lebih spesifik dengan status 400_BAD_REQUEST.
# Catatan Tambahan:
# Penamaan: Sesuaikan nama view dan serializer dengan standar penamaan yang konsisten.
# Exception Handling: Menambahkan str(e) dalam response membantu debugging dengan memberikan pesan error yang lebih jelas.
# Dengan perbaikan ini, tampilan register seharusnya berfungsi dengan benar untuk operasi list dan create.

# from rest_framework import serializers
# from django.contrib.auth.models import User


# class accountserelizers (serializers.ModelSerializer):
#     class Meta:
#         model: User
#         fields = '__all__'
# tolong perbaiki ?
# ChatGPT
# Ada beberapa kesalahan dalam definisi serializer Anda, terutama terkait dengan penggunaan titik dua (:) alih-alih tanda sama dengan (=) dalam kelas Meta. Berikut adalah versi yang diperbaiki dari serializer Anda:

# python
# Salin kode
# from rest_framework import serializers
# from django.contrib.auth.models import User

# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
# Penjelasan:
# Penamaan Kelas: Gunakan CamelCase untuk nama kelas, jadi accountserelizers diubah menjadi AccountSerializer.

# Meta Class:

# model: Gunakan tanda sama dengan (=) alih-alih titik dua (:) untuk mendefinisikan model.
# fields: Tetapkan fields = '__all__' untuk menyertakan semua field dari model User.
# Kode Lengkap dengan Tampilan
# Untuk memastikan bahwa semuanya bekerja dengan baik, berikut adalah tampilan dan serializer yang sudah diperbaiki secara keseluruhan:

# serializers.py
# python
# Salin kode
# from rest_framework import serializers
# from django.contrib.auth.models import User

# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
# views.py
# python
# Salin kode
# from rest_framework import generics, status
# from rest_framework.response import Response
# from django.http import JsonResponse
# from django.contrib.auth.models import User
# from .serializers import AccountSerializer  # Pastikan nama file sesuai

# class RegisterView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = AccountSerializer

#     def list(self, request, *args, **kwargs):
#         try:
#             query = self.get_queryset()
#             serializer = self.get_serializer(query, many=True)
#             return Response(serializer.data)
#         except Exception as e:
#             return JsonResponse({'message': 'Failed to fetch data', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def create(self, request, *args, **kwargs):
#         try:
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             self.perform_create(serializer)
#             return Response({'message': 'Success: Data created'}, status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response({'message': 'Failed to create data', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
# Penjelasan
# Serializers:

# Definisikan AccountSerializer dengan benar menggunakan tanda sama dengan dalam kelas Meta.
# Views:

# Gunakan serializer yang telah diperbaiki untuk ListCreateAPIView.
# Pastikan penamaan yang konsisten dan exception handling yang baik.
# Dengan penyesuaian ini, serializer dan tampilan Anda seharusnya berfungsi dengan benar untuk operasi list dan create.

# bisakah kita login auth django melalui api rest framework ?
# ChatGPT
# Ya, Anda bisa melakukan login autentikasi Django melalui Django REST Framework (DRF). Ada beberapa cara untuk mengimplementasikan login melalui API dengan DRF. Salah satu cara yang paling umum adalah dengan menggunakan rest_framework.authtoken untuk token-based authentication atau dj-rest-auth untuk implementasi yang lebih lengkap.

# Metode 1: Menggunakan rest_framework.authtoken
# 1. Instal djangorestframework dan drf_yasg (opsional untuk dokumentasi API)
# bash
# Salin kode
# pip install djangorestframework
# pip install djangorestframework.authtoken
# pip install drf-yasg
# 2. Tambahkan ke INSTALLED_APPS di settings.py
# python
# Salin kode
# INSTALLED_APPS = [
#     ...
#     'rest_framework',
#     'rest_framework.authtoken',
#     'drf_yasg',
# ]
# 3. Tambahkan konfigurasi REST framework di settings.py
# python
# Salin kode
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.TokenAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#     ],
# }
# 4. Buat endpoint untuk mendapatkan token
# Buat file baru accounts/views.py:

# python
# Salin kode
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response

# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })
# 5. Tambahkan URL untuk endpoint login di accounts/urls.py
# python
# Salin kode
# from django.urls import path
# from .views import CustomAuthToken

# urlpatterns = [
#     path('login/', CustomAuthToken.as_view(), name='api_token_auth'),
# ]
# Tambahkan include untuk URL accounts di myproject/urls.py:

# python
# Salin kode
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/', include('accounts.urls')),
# ]
# 6. Migrasi database
# Jalankan migrasi untuk membuat tabel token:

# bash
# Salin kode
# python manage.py migrate
# 7. Gunakan token untuk autentikasi
# Setelah mendapatkan token melalui endpoint /accounts/login/, Anda dapat menggunakan token tersebut untuk autentikasi di header setiap permintaan:

# http
# Salin kode
# Authorization: Token your_token_here
# Metode 2: Menggunakan dj-rest-auth
# dj-rest-auth menyediakan implementasi autentikasi yang lebih lengkap, termasuk login, logout, registrasi, dan reset password.

# 1. Instal dj-rest-auth
# bash
# Salin kode
# pip install dj-rest-auth
# pip install django-allauth
# 2. Tambahkan ke INSTALLED_APPS di settings.py
# python
# Salin kode
# INSTALLED_APPS = [
#     ...
#     'rest_framework',
#     'rest_framework.authtoken',
#     'dj_rest_auth',
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',  # optional
#     'dj_rest_auth.registration',  # optional
# ]
# 3. Tambahkan konfigurasi REST framework di settings.py
# python
# Salin kode
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.TokenAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#     ],
# }
# 4. Tambahkan URL untuk dj-rest-auth di myproject/urls.py
# python
# Salin kode
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('auth/', include('dj_rest_auth.urls')),
#     path('auth/registration/', include('dj_rest_auth.registration.urls')),  # optional
# ]
# 5. Migrasi database
# Jalankan migrasi untuk membuat tabel yang diperlukan:

# bash
# Salin kode
# python manage.py migrate
# Dengan dj-rest-auth, Anda sekarang memiliki endpoint siap pakai untuk login (/auth/login/), logout (/auth/logout/), registrasi (/auth/registration/), dan lain-lain.

# Contoh Penggunaan API Login
# Untuk melakukan login melalui API, Anda dapat mengirim permintaan POST ke endpoint login dengan username dan password sebagai data:

# http
# Salin kode
# POST /auth/login/
# Content-Type: application/json

# {
#   "username": "your_username",
#   "password": "your_password"
# }
# Jika login berhasil, Anda akan mendapatkan token yang dapat digunakan untuk autentikasi di permintaan berikutnya.

# Dengan langkah-langkah di atas, Anda dapat mengatur autentikasi pengguna melalui API di Django menggunakan Django REST Framework.

# No module named 'requests'
# ChatGPT
# Kesalahan No module named 'requests' terjadi karena Python tidak dapat menemukan modul requests yang Anda coba import di proyek Anda. Modul requests adalah pustaka yang tidak termasuk dalam instalasi Python standar dan perlu diinstal terpisah.

# Cara Mengatasi Kesalahan
# Berikut langkah-langkah untuk mengatasi kesalahan No module named 'requests':

# 1. Instalasi Modul requests
# Pastikan Anda telah menginstal modul requests di lingkungan Python yang sedang Anda gunakan. Anda bisa melakukan instalasi menggunakan pip, manajer paket Python yang umum digunakan:

# bash
# Salin kode
# pip install requests
# Pastikan bahwa Anda menjalankan perintah ini di dalam lingkungan virtual environment (venv/conda) yang digunakan oleh proyek Anda. Jika tidak, tambahkan opsi --user untuk instalasi global:

# bash
# Salin kode
# pip install --user requests
# 2. Verifikasi Instalasi
# Setelah Anda menginstal requests, verifikasi apakah instalasi berhasil dengan menjalankan Python di terminal dan coba import requests:

# python
# Salin kode
# python
# >>> import requests
# >>>
# Jika tidak ada pesan kesalahan, artinya requests telah berhasil diinstal dan dapat diimpor dengan benar.

# 3. Pastikan Lingkungan Virtual Environment Teraktif (Opsional)
# Jika Anda menggunakan lingkungan virtual environment, pastikan Anda telah mengaktifkannya sebelum menjalankan pip install requests. Hal ini memastikan bahwa modul requests terinstal di lingkungan virtual environment yang sedang digunakan.

# 4. Restart IDE atau Terminal
# Setelah melakukan instalasi, pastikan untuk memulai ulang Integrated Development Environment (IDE) atau terminal tempat Anda mengembangkan proyek Python. Hal ini membantu memastikan bahwa lingkungan Python yang digunakan mengenali perubahan instalasi modul.

# Dengan mengikuti langkah-langkah di atas, Anda seharusnya bisa mengatasi kesalahan No module named 'requests' dan menggunakan modul requests dalam proyek Python Anda tanpa masalah.

# apakah dj-rest-auth bisa digunakan untuk login pada front end react ?
# ChatGPT
# Ya, dj-rest-auth dapat digunakan untuk mengimplementasikan login pada frontend yang menggunakan React atau teknologi frontend lainnya. dj-rest-auth menyediakan endpoint API yang memungkinkan aplikasi frontend untuk berinteraksi dengan Django backend untuk operasi autentikasi seperti login, logout, registrasi, dan pengaturan sandi.

# Berikut adalah langkah-langkah umum untuk menggunakan dj-rest-auth dengan frontend React:

# 1. Instalasi dan Konfigurasi Django
# Instalasi Package
# Pastikan Anda telah menginstal dj-rest-auth dan dependensinya di Django:

# bash
# Salin kode
# pip install dj-rest-auth
# pip install django-allauth  # Membutuhkan allauth untuk beberapa fitur dj-rest-auth
# Tambahkan dj-rest-auth dan allauth ke INSTALLED_APPS di settings.py:

# python
# Salin kode
# INSTALLED_APPS = [
#     ...
#     'rest_framework',
#     'rest_framework.authtoken',
#     'dj_rest_auth',
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',  # Opsional, untuk autentikasi sosial
# ]
# Tambahkan konfigurasi REST framework di settings.py:

# python
# Salin kode
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.TokenAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#     ),
# }
# Jalankan migrasi untuk menerapkan perubahan ke database:

# bash
# Salin kode
# python manage.py migrate
# 2. Pengaturan URL dan Views
# Tambahkan URL untuk dj-rest-auth di urls.py proyek Django:

# python
# Salin kode
# from django.urls import path, include

# urlpatterns = [
#     ...
#     path('auth/', include('dj_rest_auth.urls')),
# ]
# 3. Frontend dengan React
# Pada sisi frontend, Anda dapat menggunakan fetch atau library HTTP seperti Axios untuk berkomunikasi dengan endpoint dj-rest-auth yang disediakan oleh Django backend.

# Contoh Penggunaan Login dengan React dan Axios
# Berikut adalah contoh sederhana penggunaan Axios untuk melakukan login dari frontend React ke backend Django menggunakan dj-rest-auth:

# jsx
# Salin kode
# import React, { useState } from 'react';
# import axios from 'axios';

# const Login = () => {
#   const [username, setUsername] = useState('');
#   const [password, setPassword] = useState('');

#   const handleSubmit = async (e) => {
#     e.preventDefault();

#     try {
#       const response = await axios.post('http://localhost:8000/auth/login/', {
#         username: username,
#         password: password
#       });

#       console.log(response.data);  // Token dan data pengguna lainnya

#       // Simpan token ke localStorage atau session storage untuk digunakan di permintaan selanjutnya
#       localStorage.setItem('token', response.data.token);

#       // Redirect atau lakukan tindakan lain setelah berhasil login
#     } catch (error) {
#       console.error('Error logging in:', error);
#     }
#   };

#   return (
#     <form onSubmit={handleSubmit}>
#       <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
#       <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
#       <button type="submit">Login</button>
#     </form>
#   );
# };

# export default Login;
# Catatan Penting:
# Pastikan URL yang digunakan dalam axios.post sesuai dengan endpoint dj-rest-auth/login/ dari backend Django Anda.
# Setelah mendapatkan token dari respons, simpan token tersebut di localStorage atau sessionStorage agar dapat digunakan dalam permintaan API berikutnya.
# Anda dapat menyesuaikan komponen React di atas sesuai dengan kebutuhan dan logika aplikasi Anda.
# Dengan menggunakan dj-rest-auth dan mengimplementasikan API login seperti contoh di atas, Anda dapat menghubungkan frontend React dengan backend Django untuk operasi autentikasi dengan mudah dan aman.


# apakah bisa response yang di berikan dari respon api berupa token jwt PYjwt ?
# ChatGPT
# Ya, Anda bisa mengonfigurasi Django REST Framework (DRF) agar menggunakan JSON Web Token (JWT) sebagai metode autentikasi, dan kemudian mengirimkan token JWT sebagai respons dari API setelah proses autentikasi berhasil.

# Cara Menggunakan JWT di Django REST Framework
# Berikut adalah langkah-langkah umum untuk menggunakan JWT di Django REST Framework dan mengirimkan token JWT sebagai respons dari API:

# 1. Instalasi Paket
# Pastikan Anda telah menginstal paket-paket yang diperlukan:

# bash
# Salin kode
# pip install djangorestframework djangorestframework-jwt
# 2. Konfigurasi Settings Django
# Tambahkan konfigurasi JWT di settings.py Anda:

# python
# Salin kode
# # settings.py

# INSTALLED_APPS = [
#     ...
#     'rest_framework',
#     'rest_framework_jwt',  # Menambahkan JWT ke installed apps
# ]

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
#         'rest_framework.authentication.SessionAuthentication',  # Opsional, jika Anda ingin menggunakan session authentication juga
#         'rest_framework.authentication.BasicAuthentication',     # Opsional, jika Anda ingin menggunakan basic authentication juga
#     ),
# }

# JWT_AUTH = {
#     'JWT_SECRET_KEY': 'your_secret_key_here',  # Ganti dengan secret key yang aman
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),  # Durasi token JWT berlaku
#     'JWT_ALLOW_REFRESH': True,  # Izinkan refresh token
#     'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),  # Durasi refresh token berlaku
# }
# 3. Views untuk Login dengan JWT
# Buat view untuk login yang akan menghasilkan token JWT setelah autentikasi berhasil:

# python
# Salin kode
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
# from django.contrib.auth import authenticate

# class CustomAuthToken(APIView):
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = authenticate(username=username, password=password)

#         if user:
#             payload = jwt_payload_handler(user)
#             token = jwt_encode_handler(payload)
#             return Response({'token': token, 'user_id': user.id})
#         else:
#             return Response({'error': 'Invalid credentials'}, status=400)
# 4. Konfigurasi URL
# Tambahkan URL untuk endpoint login dengan JWT di urls.py Anda:

# python
# Salin kode
# from django.urls import path
# from .views import CustomAuthToken

# urlpatterns = [
#     path('api/token/', CustomAuthToken.as_view(), name='api_token_auth'),
#     # Tambahkan URL lainnya sesuai kebutuhan aplikasi Anda
# ]
# 5. Frontend React
# Setelah menyiapkan backend dengan Django dan DRF menggunakan JWT, Anda dapat menggunakan React untuk melakukan permintaan POST ke endpoint /api/token/ dan menangani token yang diterima.

# Berikut adalah contoh sederhana penggunaan Axios di React untuk melakukan login dengan JWT:

# jsx
# Salin kode
# import React, { useState } from 'react';
# import axios from 'axios';

# const Login = () => {
#   const [username, setUsername] = useState('');
#   const [password, setPassword] = useState('');

#   const handleSubmit = async (e) => {
#     e.preventDefault();

#     try {
#       const response = await axios.post('http://localhost:8000/api/token/', {
#         username: username,
#         password: password
#       });

#       console.log(response.data);  // Token JWT dan data pengguna lainnya

#       // Simpan token JWT ke localStorage atau sessionStorage untuk digunakan di permintaan selanjutnya
#       localStorage.setItem('token', response.data.token);

#       // Redirect atau lakukan tindakan lain setelah berhasil login
#     } catch (error) {
#       console.error('Error logging in:', error);
#     }
#   };

#   return (
#     <form onSubmit={handleSubmit}>
#       <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
#       <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
#       <button type="submit">Login</button>
#     </form>
#   );
# };

# export default Login;
# Penjelasan
# Instalasi dan Konfigurasi: Pastikan untuk menginstal djangorestframework dan djangorestframework-jwt, kemudian tambahkan konfigurasi JWT di settings.py.
# Views untuk JWT: Buat view CustomAuthToken yang akan menghasilkan token JWT setelah autentikasi berhasil.
# URL dan Endpoint: Tambahkan URL untuk endpoint api/token/ di urls.py Django Anda.
# Frontend React: Gunakan Axios untuk melakukan permintaan POST ke endpoint api/token/ dari frontend React dan simpan token JWT yang diterima.
# Dengan langkah-langkah di atas, Anda dapat menggunakan JWT sebagai metode autentikasi di Django REST Framework dan mengirimkan token JWT sebagai respons dari API setelah proses autentikasi berhasil.

# bagaimana cara kita menggunakan permission class  di class ip generic list create ?
# ChatGPT
# Untuk menggunakan permission class di dalam sebuah class view generik seperti ListCreateAPIView pada Django REST Framework, Anda dapat mengikuti langkah-langkah berikut:

# Langkah-langkah
# 1. Membuat Permission Class
# Pertama, Anda perlu membuat sebuah kelas yang mewarisi dari permissions.BasePermission atau salah satu dari subclassnya seperti permissions.IsAuthenticated, permissions.AllowAny, atau permissions.IsAdminUser. Misalnya, mari kita buat CustomPermission yang hanya mengizinkan akses kepada pengguna yang telah terautentikasi:

# python
# Salin kode
# from rest_framework import permissions

# class CustomPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         # Hanya izinkan jika pengguna telah terautentikasi
#         return request.user and request.user.is_authenticated
# Anda dapat menyesuaikan logika dalam metode has_permission sesuai dengan kebutuhan aplikasi Anda.

# 2. Menentukan Permission di ListCreateAPIView
# Setelah membuat Permission Class, sekarang Anda dapat menggunakannya di ListCreateAPIView di views.py Anda. Berikut contoh penggunaan CustomPermission:

# python
# Salin kode
# from rest_framework import generics
# from .models import MyModel
# from .serializers import MyModelSerializer
# from .permissions import CustomPermission  # Sesuaikan dengan lokasi file Anda

# class MyModelListCreateAPIView(generics.ListCreateAPIView):
#     queryset = MyModel.objects.all()
#     serializer_class = MyModelSerializer
#     permission_classes = [CustomPermission]  # Tambahkan permission class di sini
# Dalam contoh di atas:

# MyModelListCreateAPIView adalah subclass dari generics.ListCreateAPIView.
# permission_classes adalah daftar kelas permission yang akan diterapkan pada view ini.
# CustomPermission adalah kelas permission yang telah Anda buat sebelumnya.
# Dengan menambahkan permission_classes seperti di atas, setiap kali permintaan API diterima oleh MyModelListCreateAPIView, Django REST Framework akan memeriksa apakah pengguna yang membuat permintaan memiliki izin sesuai dengan yang diatur dalam CustomPermission.

# Catatan Penting
# Pastikan Anda telah mengimpor CustomPermission atau kelas permission lain yang Anda gunakan dari modul yang sesuai.
# Anda dapat menggunakan lebih dari satu permission_classes dengan menambahkannya ke dalam list.
# Setiap kelas permission memiliki metode has_permission dan/atau has_object_permission yang dapat Anda override untuk mengatur logika izin yang lebih spesifik.
# Semua permintaan ke MyModelListCreateAPIView akan sekarang diberi izin atau ditolak berdasarkan logika yang didefinisikan di dalam CustomPermission atau kelas permission lain yang Anda tentukan.
# Dengan mengikuti langkah-langkah ini, Anda dapat menggunakan permission class di dalam ListCreateAPIView atau kelas view generik lainnya dalam Django REST Framework untuk mengontrol akses ke operasi Create dan List.

# bagaimana cara menghubungkanya dengan login disisi react ?
# ChatGPT
# Untuk menghubungkan login dari sisi React dengan Django REST Framework (DRF) menggunakan JWT (JSON Web Token), Anda perlu melakukan beberapa langkah integrasi antara frontend React dan backend Django. Berikut adalah langkah-langkah umum yang dapat Anda ikuti:

# Langkah-langkah Integrasi Login dengan React dan Django REST Framework JWT
# 1. Backend Django
# 1.1 Instalasi Paket yang Diperlukan

# Pastikan Anda telah menginstal djangorestframework dan djangorestframework-jwt di proyek Django Anda:

# bash
# Salin kode
# pip install djangorestframework djangorestframework-jwt
# 1.2 Konfigurasi settings.py

# Tambahkan rest_framework dan rest_framework_jwt ke INSTALLED_APPS di settings.py:

# python
# Salin kode
# INSTALLED_APPS = [
#     ...
#     'rest_framework',
#     'rest_framework_jwt',
#     ...
# ]

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.BasicAuthentication',
#     ),
# }


# JWT_AUTH = {
#     'JWT_SECRET_KEY': 'your_secret_key_here',  # Ganti dengan secret key yang aman
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),  # Durasi token JWT berlaku
#     'JWT_ALLOW_REFRESH': True,  # Izinkan refresh token
#     'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),  # Durasi refresh token berlaku
# }
# Pastikan untuk mengganti 'your_secret_key_here' dengan kunci rahasia yang aman untuk produksi.

# 1.3 Buat View untuk Mendapatkan Token

# Buat view di Django untuk mendapatkan token JWT setelah pengguna berhasil login:

# python
# Salin kode
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
# from django.contrib.auth import authenticate

# class CustomAuthToken(APIView):
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = authenticate(username=username, password=password)

#         if user:
#             payload = jwt_payload_handler(user)
#             token = jwt_encode_handler(payload)
#             return Response({'token': token, 'user_id': user.id})
#         else:
#             return Response({'error': 'Invalid credentials'}, status=400)
# Pastikan untuk menyesuaikan URL dan endpoint yang akan digunakan di frontend React Anda.

# 2. Frontend React
# 2.1 Implementasi Form Login

# Buat komponen atau halaman di React untuk form login:

# jsx
# Salin kode
# import React, { useState } from 'react';
# import axios from 'axios';

# const Login = () => {
#   const [username, setUsername] = useState('');
#   const [password, setPassword] = useState('');

#   const handleSubmit = async (e) => {
#     e.preventDefault();

#     try {
#       const response = await axios.post('http://localhost:8000/api/token/', {
#         username: username,
#         password: password
#       });

#       console.log(response.data);  // Token JWT dan data pengguna lainnya

#       // Simpan token JWT ke localStorage atau sessionStorage untuk digunakan di permintaan selanjutnya
#       localStorage.setItem('token', response.data.token);

#       // Redirect atau lakukan tindakan lain setelah berhasil login
#     } catch (error) {
#       console.error('Error logging in:', error);
#     }
#   };

#   return (
#     <form onSubmit={handleSubmit}>
#       <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
#       <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
#       <button type="submit">Login</button>
#     </form>
#   );
# };

# export default Login;
# Pastikan URL 'http://localhost:8000/api/token/' sesuai dengan endpoint yang Anda tentukan di view Django untuk mendapatkan token JWT.

# 2.2 Menggunakan Token JWT di Permintaan API Selanjutnya

# Setelah berhasil mendapatkan token JWT dari server, simpan token tersebut di localStorage atau sessionStorage. Kemudian, gunakan token tersebut di header setiap permintaan API yang memerlukan autentikasi:

# jsx
# Salin kode
# import axios from 'axios';

# const token = localStorage.getItem('token');

# axios.defaults.headers.common['Authorization'] = `JWT ${token}`;

# // Lakukan permintaan API menggunakan axios seperti biasa
# axios.get('http://localhost:8000/api/some-resource/')
#   .then(response => {
#     console.log(response.data);
#   })
#   .catch(error => {
#     console.error('Error fetching data:', error);
#   });
# Pastikan untuk menyesuaikan URL 'http://localhost:8000/api/some-resource/' dengan endpoint yang ada di backend Django Anda.

# Catatan Penting
# Pastikan frontend dan backend berjalan pada domain dan port yang sama atau telah dikonfigurasi untuk mengatasi masalah CORS jika berbeda.
# Amankan kunci rahasia JWT Anda dengan baik dan jangan menyimpannya secara terbuka di kode sumber.
# Selalu lakukan validasi dan sanitasi input dari pengguna baik di sisi frontend maupun backend untuk mencegah serangan keamanan seperti XSS (Cross-Site Scripting) dan SQL injection.
# Pastikan untuk menangani manajemen token dengan baik, termasuk penyimpanan, pembaruan (refresh), dan pencabutan (logout) token jika diperlukan.
# Dengan mengikuti langkah-langkah di atas, Anda dapat mengimplementasikan login dari sisi React dengan Django REST Framework menggunakan JWT untuk mengamankan API dan akses pengguna.
