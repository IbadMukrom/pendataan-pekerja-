from django import forms
from .models import Pegawai


class PegawaiForm(forms.ModelForm):
    class Meta:
        model = Pegawai
        fields = ('nama','umur', 'nomor_hp', 'posisi')
        labels = {
            'nama ': 'Nama',
            'umur': 'Umur',
            'nomor_hp': 'Nomor Hp',     
        } 

        def __init__(self, *args, **kwargs):
            super(PegawaiForm,self).__init__(*args, **kwargs)
            self.fields['posisi'].empty.labels = "Select"
            self.fields['umur'].required = True

