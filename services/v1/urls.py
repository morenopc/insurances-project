# -*- coding: UTF-8 -*-
from django.conf.urls import url, include
from rest_framework import routers
from services.v1.endpoints import risk, eav_endpoint


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'risks', risk.RiskModelViewSet)
router.register(r'values', eav_endpoint.ValueModelViewSet)
router.register(r'attributes', eav_endpoint.AttributeModelViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
