# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from teacher.models import Teacher



admin.site.register(Teacher)
admin.site.site_header = 'Teacher'



