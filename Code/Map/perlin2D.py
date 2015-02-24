# -*- coding: utf-8 -*-
import math
import Image, ImageDraw
import sys

PERSISTENCE=0.66
NB_OCTAVE=6

def Noise(x, y):
   n = x + y * 57
   n = (n<<13) ^ n
   return ( 1.0 - ( (n * (n * n * 15731 + 789221) + 1376312589) & 0x7fffffff) / 1073741824.0);    

def SmoothedNoise(x, y):
   corners = ( Noise(x-1, y-1)+Noise(x+1, y-1)+Noise(x-1, y+1)+Noise(x+1, y+1) ) / 16
   sides   = ( Noise(x-1, y)  +Noise(x+1, y)  +Noise(x, y-1)  +Noise(x, y+1) ) /  8
   center  =  Noise(x, y) / 4
   return corners + sides + center

def Interpolate(a, b, x):
	ft = x * math.pi
	f = (1 - math.cos(ft)) * .5
	return  a*(1-f) + b*f
  
def InterpolatedNoise(x, y):
    intX  = int(x)
    fracX = x - intX
    intY  = int(y)
    fracY = y - intY

    v1 = SmoothedNoise(intX,     intY)
    v2 = SmoothedNoise(intX + 1, intY)
    v3 = SmoothedNoise(intX,     intY + 1)
    v4 = SmoothedNoise(intX + 1, intY + 1)

    i1 = Interpolate(v1 , v2 , fracX)
    i2 = Interpolate(v3 , v4 , fracX)

    return Interpolate(i1 , i2 , fracY)

def PerlinNoise_2D(x, y):
    total = 0
    p = PERSISTENCE
    n = NB_OCTAVE - 1

    for i in range(n):
       frequency = 2*i
       amplitude = p*i
       total += InterpolatedNoise(x * frequency, y * frequency) * amplitude

    return total


im = Image.new("RGB", (512, 512), "white")
draw = ImageDraw.Draw(im)

for i in range(512):
   sys.stdout.write(".")
   sys.stdout.flush()
   for j in range(512):
      v=int(255.*(PerlinNoise_2D(i/32., j/32.)+1)/2.)
      draw.point((i, j), (v,v,v))

im.save('out.bmp')


