from django.db import models

# Create your models here.
class Greeting(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=120)
    message = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.name 
