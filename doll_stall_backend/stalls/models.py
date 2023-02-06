from django.db import models

# Create your models here.

class Dolls(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100,default='')
    last_name = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=100)
    country = models.CharField(max_length= 100)
    user_name = models.CharField(max_length= 100)
    age = models.IntegerField(blank=False)

class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    doll = models.ForeignKey(
        'Dolls',
        on_delete=models.CASCADE,
    )

