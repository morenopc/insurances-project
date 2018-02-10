# -*- coding: UTF-8 -*-
from rest_framework import viewsets
from risks.models import Risk
from risks.serializers import RiskModelSerializer


class RiskModelViewSet(viewsets.ModelViewSet):

    """Risk Resources"""

    queryset = Risk.objects.all()
    serializer_class = RiskModelSerializer
