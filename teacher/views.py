# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Teacher as Model
from django.shortcuts import render, redirect
from teacher.form import SearchForm, UploadTeacherForm
from teacher.filter import filter_teacher
import csv
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def teacher_list(request):
    search_form = SearchForm(request.GET)
    teacher_list = filter_teacher(request.GET)

    return render(request, 'teacher_list.html', {'teacher_list': teacher_list, 'search_form': search_form})


def teacher_info(request, teacher_id):
    teacher = Model.objects.get(pk=teacher_id)

    return render(request, 'teacher_info.html', {'teacher': teacher})


@login_required(login_url="/admin/login/")
def upload_teacher_list(request):
    upload_teacher_form = UploadTeacherForm(request.POST, request.FILES)

    errors = []
    if request.method == 'POST':

        csv_file = request.FILES['teacher_list_csv'].read().decode('utf-8').splitlines()
        reader = csv.DictReader(csv_file)

        teacher_list = [Model(
            first_name=row['First Name'],
            last_name=row['Last Name'],
            email=row['Email Address'],
            profile_picture=row['Profile picture'],
            phone_number=row['Phone Number'],
            room_number=row['Room Number'],
            subjects_taught=row['Subjects taught']
        ) for row in reader if len(row['Email Address']) > 5]

        try:
            Model.objects.bulk_create(teacher_list)
            return redirect('teacher_list')
        except IntegrityError as e:
            for error in e.args:
                if 'UNIQUE' in error:
                    errors.append('Email field should be unique')

    return render(request, 'upload_teacher_list.html', {'upload_teacher_form': upload_teacher_form, 'errors': errors})
