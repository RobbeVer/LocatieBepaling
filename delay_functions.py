import numpy as np
from scipy.fftpack import ifft
from scipy.signal import gaussian, argrelextrema
import matplotlib.pyplot as plt

def calculate_delays(dataset):
    APDP_values = [None] * 24;
    delays = np.asarray([None] * 24)
    for i in range(delays.size):
        delays[i] = np.asarray([0.00, 0.00])
    
    for i in range(24):
        APDP_values[i] = channel2APDP(dataset, i, 1);
    
    APDP_values = np.asarray(APDP_values) 
    
    plt.figure(figsize=(10, 10))
    for i in range(24):
        plt.plot(APDP_values[i])
        
    x, y = APDP2delays(APDP_values[16])   
    for i in range(delays.size):
        delays[i][0], delays[i][1] = APDP2delays(APDP_values[i])
    return delays

# =============================================================================
# De APDP berekenen bij een bepaalde positie
# =============================================================================
def channel2APDP(data, pos, venster = 0):
    APDP = np.zeros(201)
    for i in range (100): # We itereren 100 keer omdat er per plaats 100 keer de frequentiekarakteristiek is gemeten
        f_karakteristiek = [None] * 201
        for j in range(201): # ALle frequenties worden overlopen, van 1GHz to 3GHz (201 meetpunten in totaal)
            f_karakteristiek[j] = data[j][pos][i]
        
        if(venster == 1) : # er kan gekozen worden om een window toe te passen
            s_ifft = ifft(f_karakteristiek*gaussian(201, 40))
        else:
            s_ifft = ifft(f_karakteristiek)
        
        power = (abs(s_ifft))**2 # het vermogen berekenen
        som = np.sum(power) # de som
        PDP = power/som # de PDP berekenen
        APDP += PDP
     
    APDP = APDP/100 # Het gemiddelde nemen van de 100 meetpunten
    return APDP

# =============================================================================
# De delays eruit halen uit de APDP
# =============================================================================
def APDP2delays(APDP):
    maximums = argrelextrema(APDP, np.greater)
    max1 = 0.00;
    max2 = 0.00;
    t1 = 0.00;
    t2 = 0.00;
    timestep = 0.498; # (1/10MHz)/201 seconden
    for j in range(2):
        for i in range(maximums[0].size):           
            if(j == 0):
                if(maximums[0][i] != -1 and max1 < APDP[maximums[0][i]]):
                    max1 = APDP[maximums[0][i]]
                    t1 = maximums[0][i] * timestep
            if(j == 1):
                if(maximums[0][i] != -1 and max2 < APDP[maximums[0][i]]):
                    max2 = APDP[maximums[0][i]]
                    t2 = maximums[0][i] * timestep
                    break

        for i in range(maximums[0].size):
            if(j == 0):
                if max1 != APDP[maximums[0][i]]:
                    maximums[0][i] = -1
                else:
                    maximums[0][i] = -1
                    break
            if(j == 1):
                if max2 != APDP[maximums[0][i]]:
                    maximums[0][i] = -1
                else:
                    maximums[0][i] = -1
                    break
    return t1, t2    

#def APDP2delays(APDP):
#    maximums = argrelextrema(APDP, np.greater)
#    max1 = 0.00;
#    max2 = 0.00;
#    t1 = 0.00;
#    t2 = 0.00;
#    timestep = 0.498; # (1/10MHz)/201 seconden
#    for j in range(2):
#        for i in range(maximums[0].size):           
#            if(j == 0):
#                if(maximums[0][i] != -1 and max1 < APDP[maximums[0][i]]):
#                    max1 = APDP[maximums[0][i]]
#                    t1 = maximums[0][i] * timestep
#            if(j == 1):
#                if(maximums[0][i] != -1 and max2 < APDP[maximums[0][i]]):
#                    max2 = APDP[maximums[0][i]]
#                    t2 = maximums[0][i] * timestep
#                    break
#
#        for i in range(maximums[0].size):
#            if(j == 0):
#                if max1 != APDP[maximums[0][i]]:
#                    maximums[0][i] = -1
#                else:
#                    maximums[0][i] = -1
#                    break
#            if(j == 1):
#                if max2 != APDP[maximums[0][i]]:
#                    maximums[0][i] = -1
#                else:
#                    maximums[0][i] = -1
#                    break
#    return t1, t2