from django import forms
from pgapp.models import *


class ZakazForm(forms.ModelForm):
    class Meta:
        model = Zakaz
        fields = ['mijoz_fio', 'avtosi', 'rangi', 'diagnostika']
        labels={
            'mijoz_fio': 'ФИО клиента',
            'avtosi':'Aвтомобиль',
            'rangi':'Цвет',
            'diagnostika':'Диагностика',

        }



class DiagnostikalarForm(forms.ModelForm):
    class Meta:
        model = Diagnostikalar
        fields = ('zakaz_id','usta_id', 'usta_haqqi','servis')
        labels={
            'zakaz_id':'Заказ ИД',
            'usta_id':'Рабочий',
            'usta_haqqi':'Деньги сотрудника',
            'servis':'Служба',
        }






