import numpy as np
from scipy.fftpack import ifft
from scipy.signal import gaussian, argrelextrema
import matplotlib.pyplot as plt

def calculate_delays(dataset):
    APDP_values = [None] * 24;
    delays = np.asarray([None] * 24)
    for i in range(delays.size):
        delays[i] = np.asarray([None, None])
    
    for i in range(24):
        APDP_values[i] = channel2APDP(dataset, i);
    
    APDP_values = np.asarray(APDP_values) 
    
    plt.figure(figsize=(10, 10))
    for i in range(24):
        plt.plot(APDP_values[i])
      
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
    t1 = 0.00;
    t2 = 0.00;
    
    for j in range(2):
        for i in range(maximums[0].size):
            if(j == 0):
                if(maximums[0][i] != -1 and t1 < APDP[maximums[0][i]]):
                    t1 = APDP[maximums[0][i]]
                    maximums[0][i] = -1
            if(j == 1):
                if(maximums[0][i] != -1 and t2 < APDP[maximums[0][i]]):
                    t2 = APDP[maximums[0][i]]
                    maximums[0][i] = -1
    
    return t1, t2