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
    a = s.Object()  
    '''                      v,  x,  y, kut, r,  m'''
    a.set_initial_conditions(1, -1.5, 0, 0, r1, 0.5, 'blue')

    y = np.random.normal(sr, st_dev)
    #print(y)
    b = s.Object() 
    b.set_initial_conditions(-1, 1.5, y, 0, r2, 0.5, 'red')
    
    c = s.Collision(5)
    c.add_object(a, 1)
    c.add_object(b, 2)

    xx =[1.5,1.46]
    yy =[-0.07,0.05]
    for i in range (n):
        r = r1/(n+1)
        d = s.Object()
        d.set_initial_conditions(1, -xx[i], -yy[i], 0, r, 0.25, 'blue')
        c.add_object(d, 1)
        r = r2/(n+1)
        e = s.Object()
        e.set_initial_conditions(-1, xx[i], yy[i]+y, 0, r, 0.25, 'red')
        c.add_object(e, 2)
    
    
    #c.plot()
    c.animate()

start(0.1,0.1)



#su = s.Object()

# a = su.set_initial_conditions(5,0,0,0,5,5)
# b = su.set_initial_conditions(-5,10,0,0,5,5)

# c = s.Collision(30)
# c.add_object(a)
# c.add_object(b)


# circle1 = plt.Circle((0,0), radius=1, color='r', fill=False)
# circle2 = plt.Circle((1.5,0.25), radius=1, color='b', fill=False)
# axs = plt.subplot()
# plt.plot(-10,10)
# axs.add_patch(circle1)
# axs.add_patch(circle2)
# plt.show()
# sus = s.Collision(5)

# writer = PillowWriter(30)
# axs = plt.subplot()
# fig = plt.figure()
# with writer.saving(fig, 'sudar.gif', 100):
#     print(len(a.x))
#     for i in range (len(a.x)):
#         if i%1 == 0:
#             plt.clf()
#             for j in sus.objects:
#                 cir = plt.Circle((x[i], y[i]), radius = j.r)
#                 axs.add_patch(cir)
#                 plt.plot(j.x[:i], j.y[:i], lw = 0.4)
#             plt.axis()
#             writer.grab_frame()
