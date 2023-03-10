from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.

class indikator(models.Model):
    indikator = models.CharField(max_length=200, verbose_name='Nama Indikator')
    keterangan = models.TextField(verbose_name='Keterangan')
    kode = models.IntegerField(verbose_name="kode_indikator")

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
    id = models.UUIDField('id', default=uuid.uuid4, primary_key=True, unique=True, null=False, blank=False,
                          editable=False)
    nama_pondok = models.CharField(max_length=200, verbose_name='Nama Pondok')
    kepala_pondok = models.CharField(max_length=200, verbose_name="Pengasuh Pondok")
    alamat = models.TextField(verbose_name="Alamat Pondok")
    status = models.IntegerField(verbose_name="Status Pondok", null=True, blank=True, default=0)

    def __str__(self):
        return self.nama_pondok


class evaluasi_pondok(models.Model):
    pondok = models.ForeignKey(pondok, models.CASCADE, related_name="pondok")
    nama_pondok = models.CharField(max_length=200, verbose_name='Nama Pondok')
    hasil_evaluasi = models.JSONField(verbose_name="Hasil Evaluasi")
    status_evaluasi = models.IntegerField(verbose_name="Status Evaluasi", null=True, blank=True, default=0)

class file_evaluasi(models.Model):
    evaluasi = models.ForeignKey(evaluasi_pondok, models.CASCADE, related_name="id_evaluasi")
    file = models.FileField()