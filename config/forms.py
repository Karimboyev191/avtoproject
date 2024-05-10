from django import forms
from pgapp.models import *


class ZakazForm(forms.ModelForm):
    class Meta:
        model = Zakaz
        fields = ('mijoz_fio', 'avtosi', 'rangi', 'diagnostika')


class DiagnostikalarForm(forms.ModelForm):
    class Meta:
        model = Diagnostikalar
        fields = ('zakaz_id','usta_id', 'usta_haqqi','servis')






