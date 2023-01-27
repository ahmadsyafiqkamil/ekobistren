from builtins import print

from django import forms
from .models import pondok
from django.utils.translation import gettext_lazy as _


class PondokForm(forms.ModelForm):
    class Meta:
        model = pondok
        fields = [
            'nama_pondok',
            'kepala_pondok',
            'alamat'
        ]

        widgets = {
            'nama_pondok': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "isi nama pondok"}),
            'kepala_pondok': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "isi nama pengurus pondok"}),
            'alamat': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "isi alamat pondok"}),
        }
        labels = {
            'nama_pondok': _('Nama Pondok'),
            'kepala_pondok': _('Pengasuh Pondok'),
            'alamat': _('Alamat Pondok'),
        }

    # def __init__(self, *args, **kwargs):
    #     super(PondokForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'
