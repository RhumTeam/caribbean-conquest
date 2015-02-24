# -*- coding: utf-8 -*-
import math
import Image, ImageDraw
import sys

im = Image.open('out.bmp')
draw = ImageDraw.Draw(im)

for i in range(512):
   for j in range(512):
      r, g, b = im.getpixel((i, j))
      if r<225:
         col=(0,0,255)
      elif r<240:
         col=(255,255,128)
      else:
         col=(0,255,0)
         
      draw.point((i, j), col)

im.save('out_bin.bmp')
