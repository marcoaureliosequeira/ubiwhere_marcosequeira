# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models


# Create your models here.
class DataFromSensor(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    geo_location = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.TextField(blank=True, null=True)  # I MADE THIS DECISION TO SIMPLIFY, BUT THIS FIELD CAN BE A USER OF USER'S TABLE
    state = models.IntegerField(default=0, blank=True, null=True)  # 0-not validated; 1-validated; 2-resolved -> I MADE THIS DECISION TO SIMPLIFY, BUT ANOTHER SOLUTION COULD BE  CREATE A TABLE
    category = models.CharField(max_length=255, blank=True, null=True)  # CONSTRUCTION, SPECIAL_EVENT, INCIDENT, WEATHER_CONDITION, ROAD_CONDITION -> I MADE THIS DECISION TO SIMPLIFY, BUT ANOTHER SOLUTION COULD BE  CREATE A TABLE
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True, null=True)

    class Meta:
        db_table = "data_from_sensors"
