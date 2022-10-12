from audioop import maxpp
from os import name
from random import choices
#from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=150)
    logo=models.ImageField()
    summery=models.CharField(max_length=1000)
    herf=models.URLField(max_length=500)


    def __str__(self):

        return self.name
        




class Adevactes(models.Model):
    name=models.CharField(max_length=150)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    profile_pic=models.ImageField()
    short_bio=models.CharField(max_length=500)
    long_bio=models.CharField(max_length=1000)
    advocate_years_exp=models.IntegerField()
    youtube=models.CharField(max_length=100)
    twitter=models.CharField(max_length=100)
    github=models.CharField(max_length=100)

    def __str__(self):
        return self.name


