# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Risk(models.Model):
    """Risk static fields"""
    name = models.CharField(max_length=32, blank=False, default="automobile")
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
