
curl https://pyenv.run | bash

 ~/.pyenv/bin/pyenv install  3.5.0

  ~/.pyenv/versions/3.5.0/bin/pip install django == 2.1
  ~/.pyenv/versions/3.5.0/bin/django-admin --version

 ~/.pyenv/versions/3.5.0/bin/pip install -r ~/django/liwwa/requirements.txt

 ~/.pyenv/versions/3.5.0/bin/python  ~/django/final_liwwa/manage.py runserver 0.0.0.0:9000



 ~/.pyenv/versions/3.5.0/bin/python ~/django/liwwa/manage.py startapp register


 ~/.pyenv/versions/3.5.0/bin/python  ~/django/final_liwwa/manage.py migrate auth
  ~/.pyenv/versions/3.5.0/bin/python  ~/django/liwwa/manage.py createsuperuser

http://3.122.208.22/flask/installation.sh