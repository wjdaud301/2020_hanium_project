from django.db import models

# Create your models here.
class Addresses(models.Model): #장고에서 제공하는 models.Model를 상속받아야한다.
    name = models.CharField(max_length=10) 
    phone_number = models.CharField(max_length=13) 
    address = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 

    class Meta: 
        ordering = ['created']

