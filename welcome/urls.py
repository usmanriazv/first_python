# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:41:09 2017

@author: Usman
"""

from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^hello',views.index)
]


