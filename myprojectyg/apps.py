# -*- coding: utf-8 -*-

#https://code.djangoproject.com/ticket/32642
from django.contrib.admin.apps import AdminConfig
class myCustomAdminConfig(AdminConfig):
    default_site = 'admin.CustomAdminSite'