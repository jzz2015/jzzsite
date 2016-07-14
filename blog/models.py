from django.db import models

class user(models.Model):
    userno = models.CharField(max_length=11)
    username = models.CharField(max_length=30)
    age = models.CharField(max_length=11)




