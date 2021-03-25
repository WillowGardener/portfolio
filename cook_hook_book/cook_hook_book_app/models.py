from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)    
    category = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)

class Card(models.Model):
    title = models.CharField(max_length=50, default="")
    text = models.TextField(default="")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Image(models.Model):
    image = models.ImageField(upload_to='images')
    caption = models.CharField(max_length=50, default="")
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    position = models.CharField(max_length=5)
