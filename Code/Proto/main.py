# -*- coding: utf-8 -*-
#import lib_map
import pygame
import random
import time
import numpy as np
import Image

s = 512*2
screen = pygame.display.set_mode((s, s))

static_pixels = np.zeros((s,s)).astype(np.uint32)
pixels = np.zeros((s,s)).astype(np.uint32)

im = Image.open('out.bmp')

for i in range(512):
   for j in range(512):
      r, g, b = im.getpixel((i, j))
      
      col=pygame.Color(0,0,0,0)
      if r<225:
         col=pygame.Color(0,0,0,255)
      elif r<240:
         col=pygame.Color(0,255,255,128)
      else:
         col=pygame.Color(0,0,255,0)
         
      static_pixels[2*i  , 2*j  ]=col
      static_pixels[2*i+1, 2*j  ]=col
      static_pixels[2*i+1, 2*j+1]=col
      static_pixels[2*i  , 2*j+1]=col
         
         
#start = time.time()
for x in xrange(100):
    #pixels=np.random.randint(np.iinfo(np.uint32).max,size=(s, s)).astype(np.uint32)
    np.copyto(pixels, static_pixels) 
    pixels[100+x,100+x]=pygame.Color(0,255,0,0)
    pixels[101+x,100+x]=pygame.Color(0,255,0,0)
    pixels[101+x,101+x]=pygame.Color(0,255,0,0)
    pixels[100+x,101+x]=pygame.Color(0,255,0,0)
    pygame.surfarray.blit_array(screen, pixels)
    
    pygame.display.flip()
    time.sleep(0.04)
    
#print 100./(time.time()-start)
   
#input()

#lib_map.init()
