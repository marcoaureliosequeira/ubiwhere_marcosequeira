# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view, action

from ubiwhere_app.models import DataFromSensor
from rest_framework import viewsets, generics
from ubiwhere_app.serializers import UserSerializer, GroupSerializer, DataFromSensorSerializer
from datetime import datetime



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DataFromSensorViewSet(viewsets.ModelViewSet):
    queryset = DataFromSensor.objects.all()
    serializer_class = DataFromSensorSerializer

    #LIST SENSOR DATA BY AUTHOR
    #RECEIVE: AUTHOR NAME
    #RETURN: DataFromSensor SERIALIZER
    @action(detail=True, methods=['get'], name='listByAuthor')
    def listByAuthor(self, request, author):
        try:
            sensorData = DataFromSensor.objects.all().filter(created_by=author)
        except:
            pass

        page = self.paginate_queryset(sensorData)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(sensorData, many=True)
        return serializer.data

    # LIST SENSOR DATA BY CATEGORY
    # RECEIVE: CATEGORY NAME
    # RETURN: DataFromSensor SERIALIZER
    @action(detail=True, methods=['get'], name='listByCategory')
    def listByCategory(self, request, category):
        try:
            sensorData = DataFromSensor.objects.all().filter(category=category)
        except:
            pass

        page = self.paginate_queryset(sensorData)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(sensorData, many=True)
        return serializer.data

    # LIST SENSOR DATA BY LOCATION
    # RECEIVE: LOCATION VALUE
    # RETURN: DataFromSensor SERIALIZER
    @action(detail=True, methods=['get'], name='listByLocation')
    def listByLocation(self, request, location):
        try:
            sensorData = DataFromSensor.objects.all().filter(geo_location=location)
        except:
            pass

        page = self.paginate_queryset(sensorData)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(sensorData, many=True)
        return serializer.data

    # VALIDATE SENSOR DATA
    # RECEIVE: ID OF DATA RECORD
    # RETURN: DataFromSensor SERIALIZER
    @action(detail=True, methods=['put'], name='validate')
    def validate(self, request, dataId):
        try:
            DataFromSensor.objects.all().filter(id=dataId).update(state=1, updated_at=datetime.now())
        except:
            pass

        sensorData = DataFromSensor.objects.all().filter(id=dataId)

        page = self.paginate_queryset(sensorData)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(sensorData, many=True)
        return serializer.data