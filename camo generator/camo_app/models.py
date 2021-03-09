from django.db import models
from PIL import Image, ImageDraw
from django.core.files.base import ContentFile
from io import BytesIO, StringIO
import random


class Camoimage(models.Model):
    title = models.CharField(max_length=50)
    old_image = models.ImageField(upload_to='images')

    new_image = models.ImageField(default=None)

    def randompixel(self,old_image,image_width,image_height,brush_size):
        x = random.randint(1,image_width-(brush_size+1))
        y = random.randint(1,image_height-(brush_size+1))
        pix = old_image.crop((x,y,x+brush_size,y+brush_size))
        return pix

    def camodraw(self):
        brush_size = 3
        old_image = Image.open(self.old_image)
        old_image_width = old_image.width
        old_image_height = old_image.height
        new_image_width = 500
        new_image_height = 500

        pattern = Image.new('RGB',(new_image_width,new_image_height))
        x = 0
        y = 0
        for j in range(new_image_height):
            x=0
            for i in range(new_image_width):
                color = self.randompixel(old_image,old_image_width,old_image_height,brush_size)
                pattern.paste(color,(x,y))
                x+=brush_size
            y+=brush_size

        

        image_io = BytesIO()
        pattern.save(image_io, 'PNG')
        print(image_io)
        self.new_image.save('new_pattern.png', ContentFile(image_io.getvalue()), save=True)

        # art.image.save(art.name + '.jpg', ContentFile(img_io.getvalue()), save=True)
