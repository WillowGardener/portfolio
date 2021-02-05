import PIL
from PIL import Image, ImageDraw
import random

plover = Image.open("plover.png")
ploverwidth, ploverheight = plover.size
pixels = plover.load()

#grabs a random pixel from the input image and returns its color
def randompixel(image,width,height,brush_size):
    x = random.randint(1,width-(brush_size+1))
    y = random.randint(1,height-(brush_size+1))
    pix = image.crop((x,y,x+brush_size,y+brush_size))
    return pix


def camodraw(width,height):
    brush_size = int(input("enter brush size: "))
    pattern = Image.new('RGB', (width,height))
    #draw = ImageDraw.Draw(pattern)
    x = 0
    y = 0
    for j in range(height//brush_size):
        x=0
        for i in range(width//brush_size):
            color = randompixel(plover,ploverwidth,ploverheight,brush_size)
            pattern.paste(color,(x,y))
            x+=brush_size
        y+=brush_size

    pattern.show()

camodraw(5000,5000)

# ranpix = randompixel(plover,ploverwidth,ploverheight)
# print(ranpix)