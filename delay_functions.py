import numpy as np
from scipy.fftpack import ifft
from scipy.signal import gaussian, argrelextrema, find_peaks
import matplotlib.pyplot as plt

def calculate_delays(dataset):
    APDP_values = [None] * 24;
    delays = np.asarray([None] * 24)
    for i in range(delays.size):
        delays[i] = np.asarray([None, None])
    
    for i in range(24):
        APDP_values[i] = channel2APDP(dataset, i);
    
    APDP_values = np.asarray(APDP_values) 
    
    plt.figure(figsize=(20, 10))
    plt.xlim((0,60))
    plt.locator_params(axis='x', nbins='60')
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
    peak1 = 0
    peak2 = 0
    maximum_indices, properties = find_peaks(APDP, height = 0) #Vind de indexen van de peaken
    heights = properties["peak_heights"] #Hoogte van alle peaken opvragen
    timestep = 0.498 #nanoseconden per stap
    
    for i in range(heights.size):
        if(heights[i] > peak1): #Grootste peak
            peak1 = maximum_indices[i]
        elif(heights[i] > peak2): #2de hoogste peak
            peak2 = maximum_indices[i]


    return (peak1*timestep), (peak2*timestep)
