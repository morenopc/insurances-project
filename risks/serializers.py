# -*- coding: UTF-8 -*-
from collections import OrderedDict
from rest_framework import serializers
from eav.models import Value, Attribute
from risks.models import Risk


class AttributeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attribute
        fields = ('slug', 'datatype')


class ValueModelSerializer(serializers.ModelSerializer):

    attribute = AttributeModelSerializer(read_only=True)

    class Meta:
        model = Value
        exclude = ('id', 'entity_id', 'created', 'modified', 'entity_ct')

    def to_representation(self, instance):
        ret = super(ValueModelSerializer, self).to_representation(instance)
        # filter the null values and creates a new dictionary
        ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
        return ret


class RiskModelSerializer(serializers.ModelSerializer):

    eav = ValueModelSerializer(many=True, read_only=True)

    class Meta:
        model = Risk
        fields = ('__all__')
