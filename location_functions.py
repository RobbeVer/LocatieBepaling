import numpy as np
from sympy.solvers import solve
from sympy import Symbol, sqrt

def get_locations():
    loc_array = np.asarray([None] * 24)
    
    for i in range(loc_array.size):
        loc_array[i] = np.asarray([None, None])
        
    for i in range(24):
        loc_array[i][0] = np.round(3+(15*i)/90,2)
        loc_array[i][1] = np.round(3+(2-(3/48)*i)*np.sin(i*15*np.pi/180),2)
    
    return loc_array

def calculate_locations(delays):
    locations = np.asarray([None] * 24)
    for i in range(delays.size):
        locations[i] = np.asarray([None, None])
        
    distances = delays*10**-9*299792458
    for i in range(locations.size):
        print("distances op index",i,":",distances[i])
    for i in range(delays.size):
        d_0 = distances[i][0]
        d_1 = distances[i][1]
        c = Symbol('c')
        answers = solve((1+c)**2+(sqrt((d_0)**2-c**2)-sqrt((d_1/(2+c))**2-1))**2-(d_1-d_1/(2+c))**2, c)
        h = 0.00
#        print("index",i,"answers:",answers)
        if(answers[0] > 0):
            h = answers[0]
        else:
            h = answers[1]
        y = h + 1
        x = sqrt(d_0**2-h**2)
        locations[i][0] = x
        locations[i][1] = y
        
    return locations