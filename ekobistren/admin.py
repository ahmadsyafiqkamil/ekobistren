from django.contrib import admin

# Register your models here.
from .models import indikator, hasil_no, rute, pondok

# Register your models here.
admin.site.register(indikator)
admin.site.register(hasil_no)
admin.site.register(rute)
admin.site.register(pondok)
