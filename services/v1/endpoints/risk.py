# -*- coding: UTF-8 -*-
from risks.models import Risk
from risks.serializers import RiskModelSerializer
from rest_framework import viewsets


class RiskModelViewSet(viewsets.ModelViewSet):

    """Risk Resources"""

    queryset = Risk.objects.all()
    serializer_class = RiskModelSerializer
