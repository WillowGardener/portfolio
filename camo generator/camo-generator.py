import PIL
from PIL import Image, ImageDraw
import random

plover = Image.open("ploverpattern.png")
ploverwidth, ploverheight = plover.size
pixels = plover.load()

#grabs a random pixel from the input image and returns its color
def randompixel(image,width,height):
    x = random.randint(1,width-1)
    y = random.randint(1,height-1)
    pix = image.getpixel((x,y))
    return pix


def camodraw(width,height):
    pattern = Image.new('RGB', (width,height))
    draw = ImageDraw.Draw(pattern)
    x = 0
    y = 0
    for j in range(height):
        x=0
        for i in range(width):
            color = randompixel(plover,ploverwidth,ploverheight)
            draw.point((x,y),color)
            x+=1
        y+=1

    pattern.show()

camodraw(500,500)

# ranpix = randompixel(plover,ploverwidth,ploverheight)
# print(ranpix)