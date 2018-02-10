# -*- coding: UTF-8 -*-
from rest_framework import viewsets
from risks.serializers import ValueModelSerializer, AttributeModelSerializer
from eav.models import Value, Attribute


class AttributeModelViewSet(viewsets.ModelViewSet):

    """Attribute Resources"""

    queryset = Attribute.objects.all()
    serializer_class = AttributeModelSerializer

class ValueModelViewSet(viewsets.ModelViewSet):

    """Value Resources"""

    queryset = Value.objects.all()
    serializer_class = ValueModelSerializer
