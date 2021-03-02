from django.contrib.auth.models import User,Group
from django.core import serializers
from rest_framework import viewsets
from .serializers import UserSerializer,FillTypeSerializer,FillTypeAttributeSerializer,AreaSerializer,GroupSerializer
from rest_framework.decorators import api_view
from .models import areas,fill_types,fill_type_attributes,area_type_attributes
from rest_framework import viewsets, status
from rest_framework.response import Response





class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FillTypeViewSet(viewsets.ModelViewSet):

    queryset = fill_types.objects.all()
    serializer_class = FillTypeSerializer

class FillTypeAttributeViewSet(viewsets.ModelViewSet):

    queryset = fill_type_attributes.objects.all()
    serializer_class = FillTypeAttributeSerializer


class AreaViewSet(viewsets.ModelViewSet):

    queryset = areas.objects.all()
    serializer_class = AreaSerializer
    http_method_names = ['get']



@api_view(['GET'])
def areass(request):

    ar = areas.objects.all()

    data = []
    for ad in ar:
        ft = fill_types.objects.filter(id = ad.fill_type_id).get()
        obj = {
            "id": ad.id,
            "name": ad.name,
            "description": ad.description,
            "points": ad.points,
            "fill_type": ft.name

        }
        attr = list(area_type_attributes.objects.filter(area_id = ad.id))
        for at in attr:
            fta = fill_type_attributes.objects.filter(id = at.fill_type_attribute_id).get()
            obj[str(fta.name)] = at.value

        data.append(obj)

    return Response(data)