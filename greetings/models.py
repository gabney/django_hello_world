from django.db import models

# Create your models here.
class Greeting(models.Model):
    hello = models.CharField(max_length=50)
    world = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.hello} {self.world}"