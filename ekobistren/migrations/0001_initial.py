# Generated by Django 4.1.5 on 2023-02-02 01:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="evaluasi_pondok",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nama_pondok",
                    models.CharField(max_length=200, verbose_name="Nama Pondok"),
                ),
                ("hasil_evaluasi", models.JSONField(verbose_name="Hasil Evaluasi")),
                (
                    "status_evaluasi",
                    models.IntegerField(
                        blank=True, default=0, null=True, verbose_name="Status Evaluasi"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="indikator",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "indikator",
                    models.CharField(max_length=200, verbose_name="Nama Indikator"),
                ),
                ("keterangan", models.TextField(verbose_name="Keterangan")),
                ("kode", models.IntegerField(verbose_name="kode_indikator")),
            ],
        ),
        migrations.CreateModel(
            name="pondok",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="id",
                    ),
                ),
                (
                    "nama_pondok",
                    models.CharField(max_length=200, verbose_name="Nama Pondok"),
                ),
                (
                    "kepala_pondok",
                    models.CharField(max_length=200, verbose_name="Pengasuh Pondok"),
                ),
                ("alamat", models.TextField(verbose_name="Alamat Pondok")),
                (
                    "status",
                    models.IntegerField(
                        blank=True, default=0, null=True, verbose_name="Status Pondok"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="rute",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "indikator1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Indikator_1",
                        to="ekobistren.indikator",
                    ),
                ),
                (
                    "indikator2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Indikator_2",
                        to="ekobistren.indikator",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="hasil_no",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("keterangan", models.TextField(verbose_name="Keterangan")),
                (
                    "indikator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="id_indikator",
                        to="ekobistren.indikator",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="file_evaluasi",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="")),
                (
                    "evaluasi",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="id_evaluasi",
                        to="ekobistren.evaluasi_pondok",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="evaluasi_pondok",
            name="pondok",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pondok",
                to="ekobistren.pondok",
            ),
        ),
        migrations.CreateModel(
            name="ciri_ciri",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ciri", models.CharField(max_length=200, verbose_name="Ciri Ciri")),
                (
                    "indikator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="id_indikator_ciri",
                        to="ekobistren.indikator",
                    ),
                ),
            ],
        ),
    ]
