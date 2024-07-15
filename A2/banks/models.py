from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bank(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    #null ensures that a value must be provided
    name = models.CharField(max_length=100, null=False)
    swiftcode = models.CharField(max_length=100, null=False)
    institution_number = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name
    
