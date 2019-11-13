from django.contrib.auth.models import User, Group
from ubiwhere_app.models import DataFromSensor
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class DataFromSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataFromSensor
        fields = ('id', 'description', 'geo_location', 'created_by', 'state', 'category', 'created_at', 'updated_at')
