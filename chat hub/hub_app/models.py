from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=50, default=None)
    text = models.TextField()

    def __str__(self):
        return self.name

class Link(models.Model):
    text = models.TextField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    def __str__(self):
        return self.text


    