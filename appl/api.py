#views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import dht
from .serializer import Dhser

@api_view(['GET'])
def Dlist(request):
    all_data = dht.objects.all()
    data = Dhser(all_data, many=True).data
    return Response({'data': data})
class Dhtviews(generics.CreateAPIView):
    queryset = dht.objects.all()
    serializer_class = Dhser