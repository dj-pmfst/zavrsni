import numpy as np 
import matplotlib.pyplot as plt 
import random

r =  0.1
n = 5
p = np.pi*r**2
rn = [] 
pn = [p/n for x in range(n)]
x  = 0
y = 0
rn=[np.sqrt(pi/np.pi) for pi in pn] 

def plot():
    fig, axs = plt.subplots()
    x = np.zeros(n)
    y = np.zeros(n)
    xn = np.linspace(0,r,300)
    yn = np.linspace(0,r,300)
    y[0] = r+rn[0]  

    for i in range(2,n):
        
        x[1] = 0
        y[1] = random.uniform(rn[0],r-2*rn[1])
        x[0] = 0
        y[0] = 0
        
        a = True 
        while a:
            xt = random.uniform(-r,r)
            yt = random.uniform(-r,r)
            if np.sqrt(xt**2 + yt**2) < r-rn[0] and np.sqrt(xt**2 + yt**2) >= rn[1] and np.sqrt(xt**2 + yt**2) >=rn[0] and xt != x[1] and xt != x[0] and yt != y[1] and yt != [0]:
                x[i] = xt
                y[i] = yt
                a = False
                print(x,y)
            else:
                xt = random.uniform(-r,r)
                yt = random.uniform(-r,r)
    
    for i in range(2,len(x)):
        for j in range(2, len(y)):
            udaljenost = np.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
            if udaljenost < rn[i]:
                ax = x[i] + rn[i]/2
                ay = y[i] - rn[i]/2
                if np.sqrt(ax**2 + ay**2) < r-rn[0]:
                    x[i] = ax
                    y[i] = ay  

    
    
    x[0] = 0
    y[0] = 0
    print(x,y)
    plt.grid()
    circle=plt.Circle((0,0), radius=r, fill=False, color='red')
    axs.add_patch(circle)
    circle=plt.Circle((x[0],y[0]), radius=rn[0], fill=False, color='blue')
    axs.add_patch(circle)
    circle=plt.Circle((x[1],y[1]), radius=rn[0], fill=False, color='green')
    axs.add_patch(circle)
    for i in range(2,len(x)):
        plt.xlim(-r*2,r*2)
        plt.ylim(-r*2,r*2)
        circle = plt.Circle((x[i], y[i]), radius=rn[i], fill=False) #color=boje[i]
        axs.add_patch(circle)
    plt.show() 

plot()