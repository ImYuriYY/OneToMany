from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    company = models.ForeignKey('Company', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name}'