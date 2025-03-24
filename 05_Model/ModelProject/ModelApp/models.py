from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    #age = models.IntegerField()
    #country = models.CharField(max_length=30)
    
    #def __str__(self):
        #return self.first_name + ' ' + self.last_name

class Sales(models.Model):
    fee = models.IntegerField()
    create_at = models.DateTimeField(null=True)
    update_at = models.DateTimeField(null=True)