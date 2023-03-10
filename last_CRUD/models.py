from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    id = models.CharField(max_length=100,primary_key=True)
    house = models.CharField(max_length=100,blank=False,null=False)


def __str__(self):
    return self.name
