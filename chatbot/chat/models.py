from math import degrees
from django.db import models

# Create your models here.
class LOGIN(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    type=models.CharField(max_length=10)

    class Meta:
        db_table = "LOGIN"

class DETAILS(models.Model):
    username=models.CharField(max_length=20)
    Name=models.CharField(max_length=20)
    Ph_no=models.CharField(max_length=10)
    Email=models.CharField(max_length=50)
    password=models.CharField(max_length=10)

    class Meta:
        db_table = "DETAILS"

class PROFILE(models.Model):
    adhaarNO=models.CharField(max_length=20)
    PanNO=models.CharField(max_length=20)
    voterNO=models.CharField(max_length=20)
    driveNO=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    fname=models.CharField(max_length=20)
    mname=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    focc=models.CharField(max_length=20)
    mocc=models.CharField(max_length=20)


    class Meta:
        db_table = "PROFILE"

class FILES(models.Model):
    adhaar=models.CharField(max_length=100)
    pan=models.CharField(max_length=100)
    voterid=models.CharField(max_length=100)
    drlics=models.CharField(max_length=100)
    rcard=models.CharField(max_length=100)
    sslc=models.CharField(max_length=100)
    plustwo=models.CharField(max_length=100)
    fsslc=models.CharField(max_length=100)

    class Meta:
        db_table ="FILES"

    

