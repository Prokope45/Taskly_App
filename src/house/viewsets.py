from rest_framework import viewsets

from .models import House
from .serializers import HouseSerializer

from .permissions import IsHouseManagerOrNone


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    permission_classes = [IsHouseManagerOrNone]
    serializer_class = HouseSerializer