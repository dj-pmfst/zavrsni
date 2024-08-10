import math 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib.animation as animation 

class Object:
    def __init__(self):
        self.t = []
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.a = []
        self.kut = []
        self.dt = 0.01
        self.c = []
        self.m = []
    
    def set_initial_conditions(self, v0, x0, y0, kut, r, m, b):
        self.c.append(b)
        self.v0 = v0
        self.kut.append(kut)
        self.m.append(m) 
        self.r = [r]
        self.t.append(0)
        self.x.append(x0)
        self.y.append(y0)
        self.vx.append(v0 * np.cos(kut * np.pi/180))
        self.vy.append(v0 * np.sin(kut * np.pi/180))
        self.a.append(0)
        return self 
    

class Collision:    
    def __init__(self,t):
        self.t  = [0]
        self.t_uk = t 
        self.dt = 0.01
        self.xi = []
        self.yi = []
        self.xj = []
        self.yj = []
        self.objects1 = []  #lijevi
        self.objects2 = []  #desni
        self.tsudar = []

    def add_object(self, objekt, x):
       # self.objects.append(objekt)
       if x == 1:
           self.objects1.append(objekt)

       elif x == 2:
           self.objects2.append(objekt)

    def __move(self):
        i = self.objects1[0]
        j = self.objects2[0]
        #print(i.x[-1],j.x[-1])
        #print(self.objects)
        if  np.sqrt((i.x[-1] - j.x[-1])**2 + (i.y[-1] - j.y[-1])**2) <= i.r[0] + j.r[0] and i.y[-1] == j.y[-1]:  #centralni sudar
            v2i = -(2*j.m[0]*j.vx[-1]+(i.m[0]-j.m[0])*i.vx[-1])/(i.m[0]+j.m[0])
            v2j = -(2*i.m[0]*i.vx[-1]-(i.m[0]+j.m[0])*j.vx[-1])/(i.m[0]+j.m[0])
            i.vx.append(v2i)
            j.vx.append(v2j)

        if np.sqrt((i.x[-1] - j.x[-1])**2 + (i.y[-1] - j.y[-1])**2) <= i.r[0] + j.r[0]:   #ne-centralni sudar
            self.tsudar.append(self.t[-1])
            self.__angle()
            i.r.append(i.r[0]/3)
            j.r.append(j.r[0]/3)

        for o in self.objects1:
            o.t.append(o.t[-1] + o.dt)
            o.x.append(o.x[-1] + o.vx[-1]*o.dt)
            o.y.append(o.y[-1] + o.vy[-1]*o.dt)
            o.vx.append(o.v0 * np.cos(o.kut[-1] ))
            o.vy.append(o.v0 * np.sin(o.kut[-1] ))
            o.a.append(0)
        
        for o in self.objects2:
            o.t.append(o.t[-1] + o.dt)
            o.x.append(o.x[-1] + o.vx[-1]*o.dt)
            o.y.append(o.y[-1] + o.vy[-1]*o.dt)
            o.vx.append(o.v0 * np.cos(o.kut[-1] ))
            o.vy.append(o.v0 * np.sin(o.kut[-1] ))
            o.a.append(0)

        self.t.append(self.t[-1] - self.dt)
        self.tsudar.append(0)

    
    def __angle(self):
        i = self.objects1[0]
        j = self.objects2[0]

        self.xi.append(i.x[-1])
        self.yi.append(i.y[-1])
        self.xj.append(j.x[-1])
        self.yj.append(j.y[-1])
        #print(self.xi[0], self.xj[0])

        for o in self.objects1:
            o.x[0] += self.xi[0]
        for o in self.objects2:
            o.x[0] += self.xj[0]
        
        for e in self.objects1:
            a = (e.y[-1]-self.yj[0])/(e.x[-1]-self.xj[0])
            #print(e.x[0],self.xj[0])
            xt = self.xj[0] + j.r[0]/(np.sqrt( 1 + a**2))
            #yt = (xt - self.xj[0])*a + self.yj[0]
            #xs = 1 + yt*((yt - e.y[-1])/(xt - e.x[-1]))
            theta = math.acos(e.r[-1]/abs(e.x[-1]-xt))
            # i.kut.append(np.pi - 2*(theta*180/np.pi))
            # j.kut.append(np.pi - 2*(theta*180/np.pi))
            tgt = np.tan(theta)*((2*j.m[0]/(e.m[0]+j.m[0]))/((np.tan(theta))**2 + ((e.m[0]-j.m[0])/(e.m[0]+j.m[0]))))
            tht2 = np.arctan(tgt)
            e.kut.append(tht2*180/np.pi)
            j.kut.append(np.pi-2*theta*180/np.pi)  

        for e in self.objects2:
            a = (self.yi[0]-e.y[-1])/(self.xi[0]-e.x[-1])
            #print(self.xi[0],e.x[0])
            xt = e.x[-1] + e.r[0]/(np.sqrt( 1 + a**2))
            #yt = (xt - e.x[-1])*a + e.y[-1]
            #xs = 1 + yt*((yt - e.y[-1])/(xt - self.xi[0]))
            theta = math.acos(i.r[0]/abs(self.xi[0]-xt))
            # i.kut.append(np.pi - 2*(theta*180/np.pi))
            # j.kut.append(np.pi - 2*(theta*180/np.pi))
            tgt = np.tan(theta)*((2*e.m[0]/(i.m[0]+e.m[0]))/((np.tan(theta))**2 + ((i.m[0]-e.m[0])/(i.m[0]+e.m[0]))))
            tht2 = np.arctan(tgt)
            i.kut.append(tht2*180/np.pi)
            e.kut.append(np.pi-2*theta*180/np.pi)   

    
    def plot(self):
        fig, axs = plt.subplots()
        #print(self.objects)
        
        while self.t[-1] > -self.t_uk:
            self.__move()
        # print(self.objects[0].vy)
        # print(self.objects[1].vy)

        objects = []
        for o in self.objects1:
            objects.append(o)
        for o in self.objects2:
            objects.append(o)
        
        print("konacna brzina:",self.objects1[0].vx[-1], self.objects1[0].vy[-1])
        print("konacna brzina:",self.objects2[0].vx[-1], self.objects2[0].vy[-1])

        T = len(self.t)
        for o in objects:
            # print('drugi')
            # print(o.kut)
            # print(o.vx[0], o.vx[-1])
            for i in range(T):
                plt.xlim(-4,4)
                plt.ylim(-4,4)
                #print('x:', o.x[i], 'y:', o.y[i], 'r:', o.r)
                #print(i)
                plt.scatter(o.x[i], o.y[i], color=o.c[0])
                #circle = plt.Circle((o.x[i], o.y[i]), radius=o.r, color = o.c[0], fill = False)
                #axs.add_patch(circle)
            # x2 = []
            # y2 = []
            # x2.append(o.x)
            # y2.append(o.y)
            # plt.scatter(x2,y2, s=1)
            # if np.sqrt(o.vx[-1]**2 + o.vy[-1]**2) == np.sqrt(o.vx[0]**2 + o.vy[0]**2):
            #     print('isto')
            # else:
            #     print(np.sqrt(o.vx[-1]**2 + o.vy[-1]**2))
            #     print(np.sqrt(o.vx[0]**2 + o.vy[0]**2))
            #     print('nije isto')
        plt.grid()
        plt.show()
    
    def animate(self):
        fig, axs = plt.subplots()
        fig = plt.figure()
        writer = animation.PillowWriter(50)

        ii = self.objects1[0]
        jj = self.objects2[0]

        while self.t[-1] > -self.t_uk:
            self.__move()
        
        objects = []
        for o in self.objects1:
            objects.append(o)
           # print(o.r)
        for o in self.objects2:
            objects.append(o)
            #print(o.r)
        
        n = []
        for o in objects:
            n.append(len(o.x))
            #print(o.kut)
        
        rt = 0
     
        with writer.saving(fig, "sudar41.gif", 100):
            plt.xlim(-3,3)
            plt.ylim(-3,3)
            plt.grid()
            for i in range(n[1]):
                if i%1 == 0:
                    plt.clf()
                    for o in objects:
                        axs = plt.subplot()
                        plt.xlim(-3,3)
                        plt.ylim(-3,3)
                        x = o.x
                        y = o.y
                        plt.grid()
                        plt.plot(x[:i], y[:i], linewidth = 0.6)
                        if self.tsudar[i] != 0:
                            rt = -1
                        circle = plt.Circle((ii.x[i], ii.y[i]), radius=ii.r[rt], color = ii.c[0], fill = True)
                        axs.add_patch(circle)
                        circle = plt.Circle((jj.x[i], jj.y[i]), radius=jj.r[rt], color = jj.c[0], fill = True)
                        axs.add_patch(circle)
                        if rt == -1:
                            circle = plt.Circle((o.x[i], o.y[i]), radius=o.r[rt], color = o.c[0], fill = True)
                            axs.add_patch(circle)
                        #plt.scatter(o.x[i], o.y[i], color=o.c[0])
                        # plt.scatter(x[i], y[i], s = 20000/8)
                    writer.grab_frame()
    
