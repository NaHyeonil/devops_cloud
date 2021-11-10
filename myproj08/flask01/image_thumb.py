# pip install pillow

from PIL import Image

im = Image.open("static/korea.jpg")
im.thumbnail((800, 600))
im.save("static/korea.jpg")
