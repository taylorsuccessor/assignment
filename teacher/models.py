# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from teacher.validation import subjects_taught_validator

from settings.upload import get_upload_path


class Teacher(models.Model):



    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50, unique=True)
    phone_number=models.CharField(max_length=17)
    room_number = models.CharField(max_length=2,  null=True, blank=True)
    subjects_taught = models.CharField(max_length=200,validators=[subjects_taught_validator])
    profile_picture = models.FileField(upload_to=get_upload_path,  null=True, blank=True)


    def __str__(self):
        return self.first_name +' '+self.last_name





