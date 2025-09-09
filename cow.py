import numpy as np
import matplotlib.pyplot as plt
m = 1000
dt = 0.01
def get_int(): ## function gets the input variables
    y0 = float(input("Intial hight:  "))
    vx = float(input("Intial x Velocity:  "))
    vy = float(input("Intial y Velocity:  "))
    v0 = np.array([vx,vy])
    df = float(input('Drag Ceofficent:  '))
    return [y0,v0,df]


def force(y0,v0,df): ## function returns the force vector [FX,FY] at any input time
    time_of_force = float(input("Total force at time : "))
    r = [0,y0]
    v = v0
    total_force=[]
    for i in range(int(time_of_force/dt)):
        if r[1] < 0:
            break
        else:
            f_drag = -df*np.linalg.norm(v)*v
            f_grav = np.array([0,-m*9.8])
            tot_force = f_drag+f_grav
            a = (f_drag+f_grav)/m
            v += a*dt
            r += v+dt
            total_force.append(tot_force)
    return total_force[-1]


def dynamics(y0,v0,df): ##function that solves the system and returns back all the dynamical variables
    i = 0
    r = [0,y0]
    v = v0
    t = [0]
    x = [r[0]]
    y = [r[1]]
    vx = [v[0]]
    vy =[v[1]]
    while r[1]>=0:
        i += 1
        f_drag = -df*np.linalg.norm(v)*v
        f_grav = np.array([0,-m*9.8])
        a = (f_drag+f_grav)/m
        v += a*dt
        r += v*dt
        x.append(r[0])
        y.append(r[1])
        vx.append(v[0])
        vy.append(v[1])
        t.append(i*dt)
    return t,x,y,vx,vy


def energy(t,y,vx,vy): ## function that calculates the total, kinetic, and potential energy
    y = np.array(y)
    vx = np.array(vx)
    vy = np.array(vy)
    en = []
    kin=[]
    pot=[]
    for i in range(len(y)):
        en.append(1/2*m*(vx[i]**2+vy[i]**2)+m*9.8*int(y[i]))
        kin.append(1/2*m*(vx[i]**2+vy[i]**2))
        pot.append(m*9.8*y[i])
    return en,kin,pot


def plot_dyn(t,x,y,vx,vy): ## function that plots all the dynamical variables in one plot against time
    var = [x,y,vx,vy]
    lgnd = ['X vs Time','Y vs time', "VX vs time", 'VY vs time']
    i = 0
    for j in var:
        plt.plot(t,j,label = lgnd[i])
        i +=1
    plt.legend()
    plt.show()
    
def plot_energy(t,en,kin,pot): ## function that plots the total energy vs time
    plt.plot(t,en, label = 'Tot Energy')
    plt.plot(t,kin, label = 'Kinetic energy')
    plt.plot(t,pot, label = 'Potential energy')
    plt.legend()
    plt.show()



inti = get_int()

##print(force(inti[0],inti[1],inti[2]))
var = dynamics(inti[0],inti[1],inti[2])
en_var = energy(var[0],var[2],var[3],var[4])
plot_energy(var[0],en_var[0],en_var[1],en_var[2])
plot_dyn(var[0],var[1],var[2],var[3],var[4])






    