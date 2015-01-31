# -*- coding: utf-8 -*-
import Image
from PIL import Image,ImageDraw,ImageFont
color_str = '@MNH$OC?7>!:-;.'

def pic_to_ascii(img):

    img_name = img.split('.')
    img = Image.open(img).convert('L')
    pix = img.load()
    print pix
    width,height = img.size
    pic =[]
    for h in xrange(height):
        img_wid = []
        for w in xrange(width):
            img_wid.append(color_str[int(int(pix[w,h])*len(color_str)/255 )-1])
        pic.append(img_wid)

    pic_new = Image.new('RGB',(len(pic[0])*10,len(pic)*10),(255,255,255))
    draw = ImageDraw.Draw(pic_new)
    font = ImageFont.truetype('/home/lee/.local/share/fonts/arial.ttf',10)

    for y in range(len(pic)):
        for x in range(len(pic[0])):
            draw.text((x*10,y*10),pic[y][x],(255,0,0),font=font)


    pic_new.save(img_name[0]+"_ascii.jpg",'JPEG')

    print "saved!"


def main():
    pic_name = raw_input("please input the name of the picture:")
    pic_to_ascii(pic_name)

if __name__ == '__main__':
        main()
