from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class indikator(models.Model):
    indikator = models.CharField(max_length=200, verbose_name='Nama Indikator')
    keterangan = models.TextField(verbose_name='Keterangan')

    def __str__(self):
        return self.indikator


class ciri_ciri(models.Model):
    indikator = models.ForeignKey(indikator, models.CASCADE, related_name='id_indikator_ciri')
    ciri = models.CharField(max_length=200, verbose_name="Ciri Ciri")

    def __str__(self):
        return self.ciri


class hasil_no(models.Model):
    indikator = models.ForeignKey(indikator, models.CASCADE, related_name="id_indikator")
    # hasil_no = models.CharField(max_length=200, verbose_name='Hasil No')
    keterangan = models.TextField(verbose_name='Keterangan')

    def __str__(self):
        return self.indikator.indikator


class rute(models.Model):
    indikator1 = models.ForeignKey(indikator, models.CASCADE, related_name="Indikator_1")
    indikator2 = models.ForeignKey(indikator, models.CASCADE, related_name="Indikator_2")


class pondok(models.Model):
    nama_pondok = models.CharField(max_length=200, verbose_name='Nama Pondok')
    kepala_pondok = models.CharField(max_length=200, verbose_name="Pengasuh Pondok")
    alamat = models.TextField(verbose_name="Alamat Pondok")
    status = models.IntegerField(verbose_name="Status Pondok", null=True, blank=True, default=0)

    def __str__(self):
        return self.nama_pondok


class evaluasi_pondok(models.Model):
    pondok = models.ForeignKey(pondok, models.CASCADE, related_name="pondok")
