from django.shortcuts import render, redirect
from.models import Feature
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request):
    features= Feature.objects.all()

    return render(request, 'index.html',{'features': features})
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'EmailAlready Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('register')  
            else:
                user = User.objects.create_user(username = username, email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'password not same')
            return redirect('rigester')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login')
    else:
        return render(request,'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')

def count(request):
    word_count = None
    if request.method == 'POST':
        text = request.POST.get('text')
        word_count = len(text.split()) if text else 0
    return render(request, 'count.html', {'word_count': word_count})
