from django.db import models

# Create your models here.
class Slogin(models.Model):
    name = models.CharField(max_length=100, null=True)
    email =models.CharField(max_length=100, null=True)
    passwd = models.CharField(max_length=100, null=True)
    userPass = models.JSONField(max_length=200, null=True)
    def __str__(self):
        return self.name