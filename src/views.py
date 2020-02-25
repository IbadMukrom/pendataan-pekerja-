from django.shortcuts import render, redirect
from .models import Pegawai
from .forms import PegawaiForm
from django.contrib.auth.decorators import login_required
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
            pegawai = Pegawai.objects.get (pk=id)
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