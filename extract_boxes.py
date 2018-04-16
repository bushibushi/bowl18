import os
from PIL import Image, ImageDraw

def frameCell(mask_path):
    image = Image.open(os.path.join(os.getcwd(), mask_path))
    px = image.load()
    xmin = image.width
    xmax = 0
    ymin = image.height
    ymax = 0

    for i in range(0, image.width):
        for j in range(0, image.height):

            if(px[i,j] != 0):
                if(i > xmax):
                    xmax = i
                if(i < xmin):
                    xmin = i
                if(j > ymax):
                    ymax = j
                if(j < ymin):
                    ymin = j

    return xmin, xmax, ymin, ymax

xmin, xmax, ymin, ymax = frameCell('../stage1_train/0a7d30b252359a10fd298b638b90cb9ada3acced4e0c0e5a3692013f432ee4e9/masks/0adbf56cd182f784ca681396edc8b847b888b34762d48168c7812c79d145aa07.png')
image = Image.open(os.path.join(os.getcwd(), '../stage1_train/0a7d30b252359a10fd298b638b90cb9ada3acced4e0c0e5a3692013f432ee4e9/masks/0adbf56cd182f784ca681396edc8b847b888b34762d48168c7812c79d145aa07.png'))
imageFrame = ImageDraw.Draw(image)
imageFrame.rectangle([xmin, ymin, xmax, ymax], outline=(128))
image.show()