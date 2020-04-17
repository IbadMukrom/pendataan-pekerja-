from django.shortcuts import render, redirect
from .models import Pegawai, Posisi
from .forms import PegawaiForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


# @login_required
def login(request):
    return redirect('login')

@login_required
def pekerja_list(request):
    context = {'pegawai_list': Pegawai.objects.all()} 
    return render(request, 'daftar_pegawai/pegawai_list.html', context)
@login_required
def pekerja_form (request, id=0):
    if request.method =="GET":
        if id ==0:
            form = PegawaiForm()
        else:
            pegawai = Pegawai.objects.get(pk=id)
            form = PegawaiForm (instance=pegawai)
        return render (request, 'daftar_pegawai/pegawai_form.html', {'form': form })
    else:
        if id ==0:
            form = PegawaiForm(request.POST)
        else:
            pegawai = Pegawai.objects.get(pk=id)
            form = PegawaiForm(request.POST, instance=pegawai)
        if form.is_valid():
            form.save()
        return redirect('/pekerja/')

@login_required
def pekerja_hapus(request, id):
    pegawai = Pegawai.objects.get(pk=id)
    pegawai.delete()
    return redirect('/pekerja/')

@login_required
def posisi_list (request):
    context = {'posisi_list': Posisi.objects.all()}
    return render (request,'daftar_pegawai/posisilist.html', context)


class Tambah_Posisi(View):
    template_name = 'tambahposisi.html'
    def get (self, request):
        return render(request,'daftar_pegawai/tambahposisi.html')

class Simpan_posisi(View):
    def post (self, request):
        posisi = Posisi()
        posisi.title = request.POST['title']
        posisi.save()
        return redirect ('/pekerja/posisi_list/')

@login_required
def hapus_posisi (request, id):
    posisi = Posisi.objects.get (pk=id)
    posisi.delete()
    return redirect ('/pekerja/posisi_list/')

# def edit_posisi (request, id):
    # template_name = 'tambahposisi.html'
    # if request.method=="GET": 
        # posisi = Posisi()
        # posisi = Posisi.objects.get(id=id)
        # if request.method=="POST":
            # posisi.title = request.POST.get('title')
            # posisi.save()
            # return redirect ( request,'/pekerja/posisi_list/')
    # return render (request,'/pekerja/posisi_list/')


class Editposisi (View):
    template_name = 'editposisi.html'

    def get (self, request, id):
        data = {
            'posisi': Posisi.objects.get(id=id)
        }
        return render (request, 'daftar_pegawai/editposisi.html', data)
    def post (self, request, id):
        posisi = Posisi.objects.get (id=id)
        posisi.title = request.POST.get ('title')
        posisi.save()
        return redirect ('/pekerja/posisi_list/')


def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            # login (request)
            return redirect ('login')
    else:
        form = UserCreationForm()
    return render (request, 'registration/signup.html', {'form': form})
