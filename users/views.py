from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.

def register_view(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()

            return redirect('login')
    else:
        initial_data={'username':'','password1':'','password2':''}
        form=UserCreationForm(initial=initial_data)
    return render(request,'register.html',{'form':form})


def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    else:
        initial_data={'username':'','password':''}
        form=AuthenticationForm(initial=initial_data)
    return render(request,'login.html',{'form':form})



def logout_view(request):
    logout(request)
    return redirect('login')

