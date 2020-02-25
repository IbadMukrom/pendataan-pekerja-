from django.db import models


# Create your models here.

class Posisi(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Pegawai(models.Model):
    nama = models.CharField(max_length=50)
    umur = models.IntegerField()
    nomor_hp = models.IntegerField()
    posisi = models.ForeignKey(Posisi, on_delete=models.CASCADE)
