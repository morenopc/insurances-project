# -*- coding: UTF-8 -*-
from risks.models import Risk
from rest_framework import serializers


class RiskModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Risk
        fields = ('id', 'name', 'created_at')
