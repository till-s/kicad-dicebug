import sys
import math
import io

def cir(r, x0 = 0.0, y0 = 0.0, fi0 = 0.0, fi1 = math.pi, N=200, f=sys.stdout):
  for i in range(N):
    x = r*math.cos(fi0 + (fi1 - fi0)*i/(N - 1)) + x0
    y = r*math.sin(fi0 + (fi1 - fi0)*i/(N - 1)) + y0
    print("(xy {:9.4f} {:9.4f})".format( x, y ), file=f )
  

r = 20
x0 = 100
y0 = 100
fid = math.asin(0.8/r)
fi0 = math.pi*(-0.5) + fid
fi1 = math.pi*(0.5) - fid
cir(r,x0,y0,fi0,fi1)
