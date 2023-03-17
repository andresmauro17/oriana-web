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
            return render(request,'users/login.html',{'error':'invalid username or password'})
    return render(request,'users/login.html')