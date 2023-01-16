from django.db import models


class city(models.Model):
    name = models.CharField(default="", max_length=50)

    def __str__(self):
        return self.name


class test1(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(city, default="",  on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class vehicle(models.Model):
    name = models.CharField(max_length=50)
    test1 = models.ManyToManyField(test1)

    def __str__(self):
        return self.name
