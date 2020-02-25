from . import views
from django.urls import path, include

urlpatterns = [
    path ('', views.pekerja_list, name='pekerja_list'),
    path ('pekerja_form/', views.pekerja_form, name='pekerja_form'),
    path ('<int:id>/', views.pekerja_form, name='pekerja_update'),
    path ('hapus/<int:id>/', views.pekerja_hapus, name='pekerja hapus'),
    path ('accounts/', include('django.contrib.auth.urls'))

]