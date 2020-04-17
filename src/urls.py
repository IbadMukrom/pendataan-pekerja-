from . import views
from django.urls import path, include
from src.views import Tambah_Posisi, Simpan_posisi, Editposisi

urlpatterns = [
    path ('', views.pekerja_list, name='pekerja_list'),
    path ('pekerja_form/', views.pekerja_form, name='pekerja_form'),
    path ('<int:id>/', views.pekerja_form, name='pekerja_update'),
    path ('hapus/<int:id>/', views.pekerja_hapus, name='pekerja hapus'),
    
    path ('posisi_list/', views.posisi_list, name='posisi_list'),
    path ('tambah/', Tambah_Posisi.as_view(), name='tambah_posisi'),
    path ('simpan/', Simpan_posisi.as_view(), name='simpan_posisi'),
    path ('hapus_posisi/<int:id>/', views.hapus_posisi, name='hapus_posisi'),
    # path ('edit_posisi/<int:id>/', views.edit_posisi, name='edit_posisi'),
    path ('edit/<int:id>/',Editposisi.as_view(), name='edit'),

    path ('accounts/', include('django.contrib.auth.urls')),
    path ('signup/', views.signup, name='signup')
    
]