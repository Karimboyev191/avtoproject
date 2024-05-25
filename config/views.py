from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DeleteView
from pgapp.models import Zakaz

from config.forms import *

class HomeView(View):
    def get(self,request):
        return render(request,'home.html')

class AdminCheck(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser



class ZakazDeleteView(AdminCheck,View):
    def get(self,request,id):
        stat = Diagnostikalar.objects.filter(id=id).first()
        diagnostika = Diagnostikalar.objects.filter(id=id).update(status= not stat.status)
        diagnostika = Diagnostikalar.objects.filter(id=id).update(t_vaqti=timezone.now())

        return redirect('zakazlar')




class ZakazOlishView(AdminCheck,View):
    def get(self, request):
        zakaz_form = ZakazForm()
        return render(request, 'admin/zakaz.html', {'zakaz_form': zakaz_form})

    def post(self, request):
        zakaz_form = ZakazForm(request.POST)
        if zakaz_form.is_valid():
            zakaz_form.save()
            return redirect('servis')
        return render(request, 'admin/zakaz.html', {'zakaz_form': zakaz_form})

class ServisView(AdminCheck,View):
    def get(self,request):
        servis_form=DiagnostikalarForm()
        return render(request,'admin/servis.html',{'servis_form':servis_form})

    def post(self, request):
        servis_form = DiagnostikalarForm(request.POST)
        if servis_form.is_valid():
            servis_form.save()
            return redirect('zakazlar')
        return render(request, 'admin/.html', {'servis_form':servis_form })

class ZakazlarView(AdminCheck,View):
    def get(self,request):
        diagnostikalar=Diagnostikalar.objects.all().order_by('-id')
        malumot=[]
        mijoz=set(i.zakaz_id.mijoz_fio for i in diagnostikalar)
        for i in mijoz:
            a=[]
            for j in diagnostikalar:
                if j.zakaz_id.mijoz_fio==i:
                    a.append(j)
            malumot.append({'diagnostikalar' : a, 'summa':sum(j.usta_haqqi for j in a)})
        print(malumot)
        return render(request,'admin/zakazlar.html',{'malumot':malumot})




class EditXizmatView(AdminCheck,View):
    def get(self, request, id):
        diagnostika = Diagnostikalar.objects.get(id=id)
        form = DiagnostikalarForm(instance=diagnostika)
        form1 = ZakazForm(instance=diagnostika)
        return render(request, "admin/zakazedit.html", {"form": form, "form1": form1})

    def post(self, request, id):
        diagnostika = Diagnostikalar.objects.get(id=id)
        form = DiagnostikalarForm(data=request.POST, instance=diagnostika)
        form1 = ZakazForm(data=request.POST, instance=diagnostika)

        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            return redirect(reverse("zakazlar"))
        return render(request, "admin/zakazedit.html", {'form': form, 'form1': form1})



