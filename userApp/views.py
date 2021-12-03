from django.http import HttpResponse

from .forms import Userauth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as loginauth, logout as logoutsite,authenticate
from django.shortcuts import render, redirect
from .forms  import SignUpForm,User

# Create your views here.


def home(request):

    # return HttpResponse('this is home page')
    return render(request,'base.html')

def logOut(request):
    logoutsite(request)

    # return render(request,'demo/login.html')
    return redirect('login')




def viewuser(request):

    return render(request, 'demo/viewuser.html')




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            loginauth(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'demo/signup.html', {'form': form})


def loginbase(request):
    form = Userauth
    if (request.method == 'GET'):
        return render(request, 'demo/login.html', {'form': form})
    else:
       user = authenticate(username=request.POST['username'],password=request.POST['password'])
       print(user)
       if (user):
           loginauth(request,user)
           return render(request, 'base.html')
