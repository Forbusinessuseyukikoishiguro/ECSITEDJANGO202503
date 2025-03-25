from django.db import models
from datetime import date,datetime
# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(default=(1900,1,1))
    email = models.EmailField(db_index=True)
    salary = models.FloatField(null=True)
    memo = models.TextField()
    website = models.URLField(null=True)  
    create_at = models.DateTimeField(default=datetime.now)
    