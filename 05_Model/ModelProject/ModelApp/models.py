from django.db import models
from datetime import date,datetime
# Create your models here.

class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

################################################


class Person(BaseModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(default=date(1900, 1, 1))
    email = models.EmailField(db_index=True)
    salary = models.FloatField(null=True)
    memo = models.TextField()
    website = models.URLField(null=True)  
    
    class Meta:
        db_table = 'person'
        indexes = [
            models.Index(fields=['first_name', 'last_name']),
        ]
        ordering = ['salary']
    