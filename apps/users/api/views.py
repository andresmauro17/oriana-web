""" users views. """

# Django Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Django
from django.contrib.auth import authenticate, login

@api_view(["POST"])
def login_view(request):
    email=request.data['email']
    password=request.data['password']
    user = authenticate(request, email=email, password=password )
    if user:
        login(request, user)
        data = {"respuesta":"satisfactoria"}
        return Response(data,status=status.HTTP_201_CREATED)
    else:
        # return render(request,'users/login.html',{'error':'invalid username or password'})
        return Response({'error':'usuario o clave invalida'}, status=status.HTTP_401_UNAUTHORIZED)


