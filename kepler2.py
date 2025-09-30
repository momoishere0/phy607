from Area_int import euler_area_int 
from Area_int import trapezoidal_area_int
from Area_int import simpsons_area_int 
from initials_int_plot import rk4_method
from initials_int_plot import get_pars
from initials_int_plot import euler_method
from initials_int_plot import plot_rvs0
from initials_int_plot import calc_area     
# Main execution
# Get orbital parameters from user
integration = int(input("Integartion method? RK4 method [0], Euler method [1]  "))
integration_method=[rk4_method,euler_method]
area_int = int(input('Area integration method? Euler[0], Simpson\'s[1], Trapezoidal[2]  '))
area_int_method=[euler_area_int,simpsons_area_int,trapezoidal_area_int]
#getting parameters
par = get_pars()
#Main loop
while par != 0:
    # Solve orbital dynamics
    dynamics = integration_method[integration](par[0],par[1],par[2],par[3],par[4],par[7])
    #calulcating orbital area
    area = area_int_method[area_int](dynamics[2],par[7])
    #Acutal area
    print(f"Actual area = {calc_area(par[0],par[6],par[5])}")
    # Plot the orbital trajectory
    plot_rvs0(dynamics[2],dynamics[3])
    break