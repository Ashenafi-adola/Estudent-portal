from django.db import models

# Create your models here.
class Student_informations(models.Model):
    Name = models.CharField(max_length=30)
    Father = models.CharField(max_length=30)
    GrandFather = models.CharField(max_length=30)
    Gender = models.CharField(max_length=20)
    MaritalStatus = models.CharField(max_length=20)
    MatricResult = models.IntegerField()
    DateOfBirth = models.DateField()
    Age = models.IntegerField()
    PlaceOfBirth = models.CharField(max_length=30)
    Photo = models.ImageField(null=True, upload_to='photos/')
    Nationality = models.CharField(max_length=20)
    Region = models.CharField(max_length=30)
    Disability = models.CharField(max_length=30)
    Email = models.EmailField(unique=True)
    Phone = models.IntegerField()
    Password = models.CharField(unique=False, max_length=20)
    IdentityCard = models.CharField(max_length=20)
    No = models.IntegerField()
