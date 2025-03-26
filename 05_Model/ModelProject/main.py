import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelProject.settings")
from django import setup
setup()

from ModelApp import Person

p = Persin{
    first_name = 'Taro', last_name = 'Sato',
    birthday = '2000-01-01', email = 'aa@gmail.com'
    salary = 1000, memo = 'memo',web_site = 'http:/google.com',
}
p.save()


