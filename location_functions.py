import numpy as np

def get_locations():
    loc_array = np.asarray([None] * 24)
    
    for i in range(loc_array.size):
        loc_array[i] = np.asarray([None, None])
        
    for i in range(24):
        loc_array[i][0] = np.round(3+(15*i)/90,2)
        loc_array[i][1] = np.round(3+(2-(3/48)*i)*np.sin(i*15*np.pi/180),2)
    
    return loc_array

def calculate_locations(delays):
    lightspeed = 299792458 #meter/second
    
    return delays