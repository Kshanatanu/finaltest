from django.db import models

# Create your models here.

class funclist(models.Model):
    photo=models.FileField(null=True,blank=True)
    fname=models.CharField(max_length=200,null=True,blank=True)
    branch=models.CharField(max_length=20,null=True,blank=True)
    vname=models.TextField(null=True,blank=True)
    vnum=models.IntegerField(null=True,blank=True)
    venue=models.TextField(null=True,blank=True)

class s_register(models.Model):
    name = models.CharField(max_length=200,blank=True)
    roll =models.TextField(null=True)
    phone=models.CharField(max_length=10,blank=True)
    email=models.EmailField()


