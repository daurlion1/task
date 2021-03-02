from django.contrib.auth.models import User,Group
from django.core import serializers
from rest_framework import viewsets
from .serializers import UserSerializer,FillTypeSerializer,FillTypeAttributeSerializer,AreaSerializer,GroupSerializer
from rest_framework.decorators import api_view
from .models import areas,fill_types,fill_type_attributes,area_type_attributes
from rest_framework import viewsets, status
from rest_framework.response import Response
import json






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

    return Response({"areas":data})

@api_view(['GET', 'POST'])
def area(request):
    if request.method == "POST":

        area = (request.data['area'])
        fill_type = (request.data['fill_type'])
        attributes = (request.data['attributes'])
        # print(fill_type['name'])
        return Response(add_area(area, fill_type, attributes), status=status.HTTP_200_OK)
        # return Response("ok", status=status.HTTP_200_OK)


def add_area(area, fill_type, attributes):
        new_fill_type = fill_types.objects.create(name = fill_type['name'])
        new_area = areas.objects.create(
            name = area['name'],
            description = area['description'],
            points = area['points'],
            fill_type_id = new_fill_type.id
        )
        add_attributes(attributes, new_fill_type.id, new_area.id)
        return 'Successfully added'

def add_attributes(attributes,fill_type_id,area_id):
    for atrr in attributes:
        new_attr = fill_type_attributes.objects.create(name = atrr['name'],fill_type_id = fill_type_id)
        area_attr = area_type_attributes.objects.create(
            value = atrr['value'],
            fill_type_attribute_id = new_attr.id,
            area_id = area_id )