""" users views. """

# Django Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Django
from django.contrib.auth import authenticate, login

#local imports
from app_users.api.serializers import CurrentUserSerializer
from app_users.models import User
from app_organizations.models import Site

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


@api_view(["GET"])
def user_current_view(request):
    # current_user = User.objects.filter(id=request.user.id)
    current_user = request.user
    user_organizations = request.user.organizations.all()

    update_user=False
    if not current_user.current_organization or not current_user.current_site:
        first_org = current_user.organizations.first()
        current_user.current_organization = first_org
        sites = Site.objects.filter(organization=first_org)
        if sites:
            current_user.current_site = sites.first()
        current_user.save()
    serializer = CurrentUserSerializer(current_user)
    return Response(serializer.data,status=status.HTTP_200_OK)