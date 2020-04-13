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
    lightspeed = 0.299792458 #meter/nanoseconde
    
    distances = np.asarray([None] * delays.size) #Initialiseer array even groot als delays
    for i in range(distances.size):
        distances[i] = (delays[i][0] * lightspeed , delays[i][1] * lightspeed) #Afstanden in meter
    print("distances")
    print(distances)
    answers = np.asarray([None] * delays.size) 
    for i in range(answers.size):
        d0 = distances[i][0]
        d1 = distances[i][1]
    
        c = Symbol('c')
        answers[i] = solve((1+c)**2+(sqrt((d0)**2-c**2)-sqrt((d1/(2+c))**2-1))**2-(d1-d1/(2+c))**2, c)
        
        answers[i][0] = sqrt(d0**2 - answers[i][1]**2)
        answers[i][1] = answers[i][1] + 1;
    

    return answers