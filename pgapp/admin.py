from django.contrib import admin

from .models import *

class YonalishlarAdmin(admin.ModelAdmin):
    search_fields = ['nomi','xizmatlar','picture']
    list_display = ['nomi','xizmatlar','picture']

class UstalarAdmin(admin.ModelAdmin):
    search_fields = ['fio','tel']
    list_display = ['fio','tel']

class Usta_YonalishiAdmin(admin.ModelAdmin):
    search_fields = ['usta_id','yonalish_id']
    list_display = ['usta_id','yonalish_id']

class ZakazAdmin(admin.ModelAdmin):
    search_fields = ['mijoz_fio','avtosi','rangi','diagnostika','vaqti']
    list_display = ['mijoz_fio','avtosi','rangi','diagnostika','vaqti']

class DiagnostikalarAdmin(admin.ModelAdmin):
    search_fields = ['zakaz_id','usta_id','usta_haqqi','servis','status','t_vaqti']
    list_display = ['zakaz_id','usta_id','usta_haqqi','servis','status','t_vaqti']

admin.site.register(Yonalishlar,YonalishlarAdmin)
admin.site.register(Ustalar,UstalarAdmin)
admin.site.register(Usta_yonalishi,Usta_YonalishiAdmin)
admin.site.register(Zakaz,ZakazAdmin)
admin.site.register(Diagnostikalar,DiagnostikalarAdmin)