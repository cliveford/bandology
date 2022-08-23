from django.db import models


class Album(models.Model):

    title = models.CharField(max_length=100)
    band = models.ForeignKey(
        "Band", related_name="albums", on_delete=models.SET_NULL, null=True
    )
    released = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Musician(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    band = models.ForeignKey(
        "Band", related_name="musicians", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Band(models.Model):

    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    formed = models.DateField(null=True, blank=True)

    def get_genre(self):
        return self.name + ' belongs to ' + self.genre + ' genre.'

    def __str__(self):
        return self.name


class Instrument(models.Model):

    name = models.CharField(max_length=50)
    musician = models.ManyToManyField("Musician", related_name="instruments")

    def __str__(self):
        return self.name
