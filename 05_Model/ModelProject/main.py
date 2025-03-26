import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ModelProject.settings")
from django import setup
setup()

from ModelApp.models import Person

# p = Person(
#     first_name='Taro', 
#     last_name='Sato',
#     birthday='2000-01-01', 
#     email='aa@gmail.com',
#     salary=1000, 
#     memo='memo', 
#     website='http://google.com',
# )
# # p.save()

# p = Person(
#     first_name='Jiro',  
#     last_name='Sato4',
#     email='aa@gmail.com',
#     salary=None, 
#     memo='memo taro', 
#     website=None,
# )
#p.save()


# #create
# Person.objects.create(
#     first_name = 'Jiro', last_name ='Ito',
#     email='bb@gmail.com',
#     salary=20000,
#     memo='creatememethod実行',
#     website=None
# )    


#get_or_create(get or create)
Person.objects.get_or_create(
    first_name = 'Jiro5', last_name ='Ito',
    email = 'bbcde@gmail.com',salary = 20000,
    memo = 'get method実行2',
    website = None
)

