from django.shortcuts import render,redirect
from django.views.generic import (TemplateView,ListView,DetailView,
                                    CreateView,UpdateView,DeleteView,View)
from .models import *
from django.shortcuts import render,redirect



class XizmatView(View):
    def get(self,request):
        xizmatlar=Yonalishlar.objects.all()
        return render(request,"hizmat.html",{'xizmatlar':xizmatlar})


class XizDetailView(View):
    def get(self,request,a):
        xizmat=Yonalishlar.objects.get(id=a)
        return render(request,"hizdetail.html",{"xizmat":xizmat})


class ContactView(TemplateView):
    template_name = 'contact.html'

class AboutView(TemplateView):
    template_name = 'about.html'

