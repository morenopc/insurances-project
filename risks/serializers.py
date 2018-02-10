# -*- coding: UTF-8 -*-
from collections import OrderedDict
from rest_framework import serializers
from eav.models import Value, Attribute, EnumValue, EnumGroup
from risks.models import Risk


class EnumValueModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnumValue
        fields = ('value', )


class EnumGroupModelSerializer(serializers.ModelSerializer):

    enums = EnumValueModelSerializer(many=True, read_only=True)

    class Meta:
        model = EnumGroup
        fields = ('__all__')


class AttributeModelSerializer(serializers.ModelSerializer):

    enum_group = EnumGroupModelSerializer(read_only=True)

    class Meta:
        model = Attribute
        fields = ('name', 'slug', 'datatype', 'enum_group')

    def to_representation(self, instance):
        ret = super(AttributeModelSerializer, self).to_representation(instance)
        # filter the null values and creates a new dictionary
        ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
        return ret


class ValueModelSerializer(serializers.ModelSerializer):

    attribute = AttributeModelSerializer(read_only=True)
    value_enum = EnumValueModelSerializer(read_only=True)

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
