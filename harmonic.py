import numpy as np
import matplotlib.pyplot as plt
m = 10
dt = 0.0001
def get_int(): ## function gets the input variables
    y0 = float(input("Intial displacement:  "))
    v0 = float(input("Intial Velocity:  "))
    k = float(input('spring constant:  '))
    t = float(input('Total time:  '))
    return [y0,v0,k,t]


def force(y0,v0,df): ## function returns the force vector [FX,FY] at any input time
    time_of_force = float(input("Total force at time : "))
    r = [0,y0]
    v = v0
    total_force=[]
    for i in range(int(time_of_force/dt)):
            f_hooks = np.array([0,-ky])
            tot_force = f_drag+f_grav
            a = (f_drag+f_grav)/m
            v += a*dt
            r += v+dt
            total_force.append(tot_force)
    return total_force[-1]


def dynamics(y0,v0,k,time): ##function that solves the system and returns back all the dynamical variables
    v = [v0]
    t = [0]
    y = [y0]
    for j in range(int(time/dt)):
        f_hooks = -k*y[j]
        a = (f_hooks)/m
        v.append(v[j]+a*dt)
        y.append(y[j]+v[j]*dt)        
        t.append(j*dt)
    return t,y,v


def energy(k,y,v): ## function that calculates the total, kinetic, and potential energy
    en = []
    kin=[]
    pot=[]
    for i in range(len(y)):
        en.append(1/2*m*(v[i]**2)+1/2*k*y[i]**2)
        kin.append(1/2*m*(v[i]**2))
        pot.append(1/2*k*y[i]**2)
    return en,kin,pot


def plot_dyn(t,y,v): ## function that plots all the dynamical variables in one plot against time
    var = [y,v]
    lgnd = ['X vs Time', "V vs time",]
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
var = dynamics(inti[0],inti[1],inti[2],inti[3])
en_var = energy(inti[2],var[1],var[2])

##with open("comp/cow_output.txt","w") as f:
   # f.write("time,x,y\n")
   # for i,j,k in zip(var[0],var[1],var[2]):
    #    f.write(f"{i},{j},{k}\n")
plot_energy(var[0],en_var[0],en_var[1],en_var[2])
plot_dyn(var[0],var[1],var[2])






    