from django.db import models
import random as r

class Grass(models.Model):
    x = models.IntegerField(default=r.randint(5,955))
    y = models.IntegerField(default=r.randint(5,635))
    image = models.ImageField(default = "images/grass.png")
    energy = models.IntegerField(default=5)




