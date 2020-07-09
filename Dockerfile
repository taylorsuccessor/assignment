FROM python
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

ADD . /usr/src/app/
RUN cd /usr/src/app/


RUN pip install -r requirements.txt
RUN python manage.py migrate # Can this be done during build? i.e. no link to the DB?
RUN python manage.py migrate auth
VOLUME ["/opt/django_project/collected_static"]