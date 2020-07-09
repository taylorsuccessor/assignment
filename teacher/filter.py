from .models import Teacher as Model
from django.db.models import Q


def filter_teacher(data):

    teacher_list = Model.objects.order_by('-id')

    search_text=data.get('search_text',None)
    if search_text:
        teacher_list=teacher_list.filter(\
            Q(first_name__icontains=search_text)\
            |Q(last_name__icontains=search_text)\
            |Q(subjects_taught__icontains=search_text))

    page = int(data.get('page',1))
    limit = 20
    offset = limit * (page - 1)
    teacher_list = teacher_list[offset:offset + limit]

    return teacher_list
