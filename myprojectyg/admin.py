# -*- coding: utf-8 -*-

from django.contrib import admin

class CustomAdminSite(admin.AdminSite):
    title_header = 'Custom Admin'
    site_header = 'Administration'
    index_title = 'custom site admin'

