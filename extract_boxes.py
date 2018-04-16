import os
from PIL import Image


image = Image.open(os.path.join(os.getcwd(), '../stage1_train/00071198d059ba7f5914a526d124d28e6d010c92466da21d4a04cd5413362552/masks/0f5a3252d05ecdf453bdd5e6ad5322c454d8ec2d13ef0f0bf45a6f6db45b5639.png'))

image.show()