from math import pi

def euler_area_int(func,dt):
    """
    Calculate orbital area using Euler integration method
    Area = (1/2) * integral of r^2 dθ
    """
    area =0
    
    for i in range(int(2*pi/dt)):
        area += 0.5*func[i]**2*dt
    print(f'Total Area of orbit using Euler method is: {area}')

def trapezoidal_area_int(func,dt):
    """
    Calculate orbital area using Trapezoidal Rule
    Area = (1/2) * integral of r^2 dθ
    
    Trapezoidal rule: integral ≈ (dt/2) * [f(0) + 2*f(1) + 2*f(2) + ... + 2*f(n-1) + f(n)]
    """
    
    n = int(2*pi/dt)
    
    # Calculate area using trapezoidal rule
    area = 0.5 * func[0]**2  # First term
    
    # Middle terms (multiplied by 2)
    for i in range(1, n):
        area += func[i]**2
    
    # Last term
    area += 0.5 * func[n]**2
    
    # Multiply by step size and factor of 1/2 for orbital area
    area = 0.5 * area * dt
    
    print(f'Total Area of orbit using Trapezoidal method is: {area}')

def simpsons_area_int(func,dt):
    """
    Calculate orbital area using Simpson's Rule
    Area = (1/2) * integral of r^2 dθ
    
    Simpson's rule: integral ≈ (dt/3) * [f(0) + 4*f(1) + 2*f(2) + 4*f(3) + ... + 4*f(n-1) + f(n)]
    Note: n must be even for Simpson's rule
    """
    n = int(2*pi/dt)
    
    # Ensure n is even for Simpson's rule
    if n % 2 != 0:
        n -= 1
        print(f"Adjusted n to {n} (must be even for Simpson's rule)")
    
    # Calculate area using Simpson's rule
    area = func[0]**2  # First term
    
    # Alternating pattern: 4, 2, 4, 2, ..., 4
    for i in range(1, n):
        if i % 2 == 1:  # Odd indices get coefficient 4
            area += 4 * func[i]**2
        else:           # Even indices get coefficient 2
            area += 2 * func[i]**2
    
    # Last term
    area += func[n]**2
    
    # Multiply by dt/3 and factor of 1/2 for orbital area
    area = 0.5 * (dt/3) * area
    
    print(f'Total Area of orbit using Simpson\'s rule is: {area}')
    




