from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def autenticar(request):
    if request.method=='POST':
     username = request.POST['username']
     password = request.POST['password']
     user = authenticate(username=username, password=password)
     if user is not None:
        login(request, user)
        return redirect('inicio')
     else:
        return render(request,'index.html',context={'error':'error'})
    return render(request,'index.html')

def inicio(request):
    if request.user.is_authenticated:
       return render(request,'persona/index.html')  
    return render(request,'index.html')

def logoutView(request):
   logout(request)
   return redirect('inicio')        