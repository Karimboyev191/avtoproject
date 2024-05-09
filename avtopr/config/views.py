from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DeleteView
from pgapp.models import Diagnostikalar

from config.forms import *





class ZakazDeleteView(DeleteView):
    model = Diagnostikalar
    template_name = 'admin/zakaz_delete.html' 
    success_url = reverse_lazy('zakazlar')







class HomeView(View):
    def get(self,request):
        return render(request,'home.html')

class AdminCheck(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

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
        diagnostikalar=Diagnostikalar.objects.all()
        return render(request,'admin/zakazlar.html',{'diagnostikalar':diagnostikalar})

class ZakazlarDeleteAndYuborishView(View):
    def get(self, request):
        diagnostikalar = Diagnostikalar.objects.all()
        form = YuborishForm()
        return render(request, 'admin/zakazlar_delete_and_yuborish.html', {'diagnostikalar': diagnostikalar, 'form': form})

    def post(self, request):
        diagnostikalar_id_list = request.POST.getlist('delete_diagnostikalar')
        Diagnostikalar.objects.filter(id__in=diagnostikalar_id_list).delete()
        form = YuborishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('boshqa_jadvalga_yuborish')
        return render(request, 'admin/zakazlar_delete_and_yuborish.html', {'form': form})

class BoshqaJadvalgaYuborishView(View):
    def post(self, request):
        # Boshqa jadvalga yuborishni bajarish uchun kerakli logika
        return redirect('zakazlar_delete_and_yuborish')


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



