""" Login view """

# Django
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password )
        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request,'users/login.html',{'error':'Usuario o clave inválida. ¡Inténtalo de nuevo!'})
    return render(request,'users/login.html')