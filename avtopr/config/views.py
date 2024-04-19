from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render,redirect
from django.views import View

from config.forms import *


class HomeView(View):
    def get(self,request):
        return render(request,'home.html')

class AdminCheck(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class ZakazOlishView(View,AdminCheck):
    def get(self, request):
        zakaz_form = ZakazForm()
        return render(request, 'admin/zakaz.html', {'zakaz_form': zakaz_form})

    def post(self, request):
        zakaz_form = ZakazForm(request.POST)
        if zakaz_form.is_valid():
            zakaz_form.save()
            return redirect('servis')
        return render(request, 'admin/zakaz.html', {'zakaz_form': zakaz_form})

class ServisView(View,AdminCheck):
    def get(self,request):
        servis_form=DiagnostikalarForm()
        return render(request,'admin/servis.html',{'servis_form':servis_form})

    def post(self, request):
        servis_form = DiagnostikalarForm(request.POST)
        if servis_form.is_valid():
            servis_form.save()
            return redirect('zakazlar')
        return render(request, 'admin/.html', {'servis_form':servis_form })

class ZakazlarView(View,AdminCheck):
    def get(self,request):
        diagnostikalar=Diagnostikalar.objects.all()
        return render(request,'admin/zakazlar.html',{'diagnostikalar':diagnostikalar})




