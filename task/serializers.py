import json

from django.contrib.auth.models import User,Group
from .models import areas,fill_types,fill_type_attributes,area_type_attributes
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class FillTypeAttributeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = fill_type_attributes
        fields = ['name']

class FillTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = fill_types
        fields = ['name']


class AreaTypeAttributeSerializer(serializers.ModelSerializer):
    fill_type_attribute = FillTypeAttributeSerializer(many=False, read_only=True)

    class Meta:
        model = area_type_attributes
        fields = ['value','fill_type_attribute']

class AreaSerializer(serializers.ModelSerializer):
    attributes = AreaTypeAttributeSerializer(many=True, read_only=True)


    class Meta():
        model = areas
        fields = ['id','name','fill_type','description','points','attributes']

    fill_type = serializers.SerializerMethodField()

    def get_fill_type(self, obj):

        ft =  fill_types.objects.filter(id = obj.fill_type.id).get()
        return ft.name


