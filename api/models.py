from django.db import models


class Album(models.Model):

    title = models.CharField(max_length=200)
    band = models.ForeignKey(
        "Band", related_name="albums", on_delete=models.SET_NULL, null=True
    )
    released = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Musician(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    band = models.ForeignKey(
        "Band", related_name="musicians", on_delete=models.SET_NULL, null=True
    )
    instrument = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Band(models.Model):

    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    formed = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
