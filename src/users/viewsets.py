from django.contrib.auth.models import User

from rest_framework import viewsets

from .serializers import UserSerializer

class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer