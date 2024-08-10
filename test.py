import sudar as s 
import matplotlib.pyplot as plt 
import math
import numpy as np 
import random 
from matplotlib.animation import PillowWriter

def start(r1,r2, n=2):
    r = abs(2*r1+r2-0.1)
    l = -abs(2*r1+r2-0.1)
    sr = (l+r)/2
    x = np.arange(-r1, r2)
    sm = 0
    for i in range (len(x)):
        sm += (x[i]-sr)**2
    
    st_dev = math.sqrt(sm/len(x))

    '''a je kuglica s lijeve strane, radi jednostavnosti njen početni y je uvijek fiksne vrijednosti
    b je kuglica s desne strane cija se pocetna y vrijednost mijenja pri svakom pokretanju koda'''
    
    a = s.Object()  
    '''pocetni uvjeti:       v,  x,  y, kut, r,  m'''
    a.set_initial_conditions(1, -1.5, 0, 0, r1, 0.5, 'blue')

    y = np.random.normal(sr, st_dev) '''nasumicno gneriranje pocetnog uvjeta y koordinate za desnu kuglicu'''
    
    '''u ovom slucaju, zbog testiranja, y je na fiksnoj vrijednosti pri svakom pokretanju '''
    b = s.Object() 
    b.set_initial_conditions(-1, 1.5, 0.07, 0, r2, 0.5, 'red')
    
    c = s.Collision(5)
    c.add_object(a, 1)
    c.add_object(b, 2)

    '''radi jednostavnosti testiranja, prozivoljno odabrane pocetne koordinate za kuglice koje se stvore pri sudaru/raspadu'''
    #xx =[1.5,1.46]
    #yy =[-0.07,0.05]
    
    #for i in range (n):
     #   r = r1/(n+1)
     #   d = s.Object()
     #   d.set_initial_conditions(1, -xx[i], -yy[i], 0, r, 0.25, 'blue')
     #   c.add_object(d, 1)
     #   r = r2/(n+1)
     #   e = s.Object()
     #   e.set_initial_conditions(-1, xx[i], yy[i]+y, 0, r, 0.25, 'red')
     #   c.add_object(e, 2)
    
    
    c.plot() '''plotanje putanje kuglica'''
    #c.animate() '''stvaranje gif-a sudara'''

start(0.15,0.15)

