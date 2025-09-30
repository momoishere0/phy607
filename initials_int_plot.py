import math
import matplotlib.pyplot as plt
import numpy as np
def get_pars():
    """
    Get orbital parameters from user input and check for bound orbit
    
    Returns:
        tuple: (m1, r0, vr0, v00, e, h, n,d0) - mass, initial radius, initial radial velocity,
               initial tangential velocity, number of orbits, angular momentum, energy, integration step
    """
    # Get orbital parameters from user
    d0 = float(input('integration step size:  '))
    m1 = float(input("Mass of star: "))
    r0 = float(input("intial radial distance: "))
    vr0 = float(input("intial radial velocity: "))
    v00 = float(input("intial tangental velocity: "))
    n = int(input('number of orbits: '))
    e = 1/2*(vr0**2+v00**2)-m1/r0
    h = r0*v00 
    # Check if orbit is bound (total energy < 0)
    # E = (1/2)(vr^2 + v_theta^2) - GM/r
    if 1/2*(vr0**2+v00**2)-m1/r0 >= 0:
             print("ERROR: Energy is unbound!!")
             return 0
             exit
    else:
        return m1,r0,vr0,v00,n,e,h,d0
def euler_method(m1,r0,vr0,v00,n,d0):
    """
    Solve orbital mechanics ODE using Euler's method
    
    The system of ODEs being solved:
    dy1/dθ = y2, where y1 = 1/r
    dy2/dθ = -y1 + u/h²
    
    Parameters:
        m1: Mass of central star
        r0: Initial radial distance
        vr0: Initial radial velocity
        v00: Initial tangential velocity
        n: Number of orbits to simulate
    
    Returns:
        tuple: (y1, y2, r, theta) - arrays of computed values
    """
    h = r0*v00      # Angular momentum (conserved quantity)
    theta = [0]      # Angle array
    u = m1          # Gravitational parameter
    y1 = [1/r0]     # Initial value of 1/r
    y2 = [-vr0/h]   # Initial value of d(1/r)/dθ
    r = [r0]          # Radial distance array
    
    # Integrate over the specified number of orbits
    for i in range(int(2*n*math.pi/d0)):
         theta.append(i*d0)                                    # Current angle
         y1.append(y1[i]+y2[i]*d0)                            # Euler step for y1
         y2.append(y2[i]+(-y1[i]*(1)+u/h**2)*d0)             # Euler step for y2
         r.append(1/y1[i])                                    # Convert back to radius
    return y1,y2,r,theta

def rk4_method(m1,r0,vr0,v00,n,d0):
    """
    Solve orbital mechanics ODE using 4th-order Runge-Kutta method
    
    The system of ODEs being solved:
    dy1/dθ = y2, where y1 = 1/r
    dy2/dθ = -y1 + u/h²
    
    Parameters:
        m1: Mass of central star
        r0: Initial radius
        vr0: Initial radial velocity
        v00: Initial tangential velocity
        n: Number of orbital periods to simulate
    
    Returns:
        tuple: (y1, y2, r, theta) - arrays of computed values
    """
    h = r0 * v00    # Angular momentum (conserved quantity)
    u = m1          # Gravitational parameter

    # Initialize arrays with initial conditions
    y1 = [1/r0]         # 1/r
    y2 = [-vr0/h]       # d(1/r)/dθ
    r = [r0]            # Radius
    theta = [0]         # Angle
    
    # Number of integration steps
    num_steps = int(2*n * math.pi / d0)
    
    # RK4 integration loop
    for i in range(num_steps):
        # Current values at step i
        y1_curr = y1[i]
        y2_curr = y2[i]
        
        # Calculate RK4 coefficients (k1, k2, k3, k4)
        # k1: slope at beginning of interval
        k1_y1 = d0 * y2_curr
        k1_y2 = d0 * (-y1_curr + u/h**2)
        
        # k2: slope at midpoint using k1
        k2_y1 = d0 * (y2_curr + k1_y2/2)
        k2_y2 = d0 * (-(y1_curr + k1_y1/2) + u/h**2)
        
        # k3: slope at midpoint using k2
        k3_y1 = d0 * (y2_curr + k2_y2/2)
        k3_y2 = d0 * (-(y1_curr + k2_y1/2) + u/h**2)
        
        # k4: slope at end of interval using k3
        k4_y1 = d0 * (y2_curr + k3_y2)
        k4_y2 = d0 * (-(y1_curr + k3_y1) + u/h**2)
        
        # Update values using weighted average of slopes
        y1_new = y1_curr + (k1_y1 + 2*k2_y1 + 2*k3_y1 + k4_y1) / 6
        y2_new = y2_curr + (k1_y2 + 2*k2_y2 + 2*k3_y2 + k4_y2) / 6
        
        # Store new values
        theta.append((i+1) * d0)
        y1.append(y1_new)
        y2.append(y2_new)
        r.append(1/y1_new)
    
    return y1, y2, r, theta

def plot_rvs0(r,theta):
    """
    Plot orbital trajectory in Cartesian coordinates
    
    Parameters:
        r: Array of radial distances
        theta: Array of angles
    """
    # Convert to numpy arrays for vectorized operations
    r = np.array(r)
    theta = np.array(theta)
    
    # Convert polar coordinates to Cartesian and plot trajectory
    plt.plot(r*np.cos(theta),r*np.sin(theta), label = "y vs x")
    
    # Mark start point (green)
    plt.scatter(r[0]*np.cos(theta[0]),r[0]*np.sin(theta[0]),color = "Green" ,label = "Start Point")
    
    # Mark end point (yellow)
    plt.scatter(r[-1]*np.cos(theta[-1]),r[-1]*np.sin(theta[-1]),color = "Yellow" ,label = "End Point")
    
    # Mark central star at origin (red)
    plt.scatter([0],[0], color = "Red", label = "Star")
    
    # Add legend and display plot
    plt.legend(loc='upper right')
    plt.show()
def calc_area(m1,h,e):
     return math.pi/math.sqrt(m1)*h*(-m1/(2*e))**(3/2)
