# -*- coding: utf-8 -*- #文件也为UTF-8
#!/usr/bin/env python
from PIL import Image,ImageDraw,ImageFont
font = ImageFont.truetype('/home/lee/.local/share/fonts/arial.ttf',10)
width = len("Hello,World!")*10
height= len("Hello,World!")*10
img = Image.new('RGB',(width,height),(255,255,255))
draw = ImageDraw.Draw(img)
for x in xrange(len("Hello,World!")):
	for y in xrange(len("Hello,World!")):

		draw.text( (x*10,y*10), 'Hello,World!'[y],(0,0,0),font=font)

draw.text((0,65),unicode('Hello','utf-8'),(0,0,0),font=font) 
img.show()