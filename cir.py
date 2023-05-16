import sys
import math
import io

def cir(r, x0 = 0.0, y0 = 0.0, fi0 = 0.0, N=200, f=sys.stdout):
  for i in range(N):
    x = r*math.cos(fi0 + (math.pi - 2*fi0)*i/N)
    y = r*math.sin(fi0 + (math.pi - 2*fi0)*i/N)
    print("(xy {:9.4f} {:9.4f})".format( x, y ), file=f )
  
