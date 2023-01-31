from django.contrib import admin

# Register your models here.
from .models import indikator, hasil_no, rute, pondok, ciri_ciri, evaluasi_pondok,file_evaluasi

# Register your models here.
admin.site.register(indikator)
admin.site.register(hasil_no)
admin.site.register(rute)
admin.site.register(pondok)
admin.site.register(ciri_ciri)
admin.site.register(evaluasi_pondok)
admin.site.register(file_evaluasi)
