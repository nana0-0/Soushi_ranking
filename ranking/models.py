from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.TextField()
    score = models.IntegerField()

    def __str__(self):
        return f'<Person name="{self.name}" score={self.score}>'
