# -*- coding: utf-8 -*-
#import lib_map
import pygame
import random
import time
import numpy as np

s = 300
screen = pygame.display.set_mode((s, s))

pixels = np.zeros((s,s)).astype(np.uint32)
#start = time.time()
for x in xrange(100):
    #pixels.fill(random.randint(0,256**3))
    
    pixels=np.random.randint(np.iinfo(np.uint32).max,size=(s, s)).astype(np.uint32)
    pygame.surfarray.blit_array(screen, pixels)
    
    pygame.display.flip()
    time.sleep(0.04)
    
#print 100./(time.time()-start)
   
#input()

#lib_map.init()
