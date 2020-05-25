import numpy as np
from scipy.fftpack import ifft
from scipy.signal import gaussian, find_peaks #argrelextrema
import matplotlib.pyplot as plt

def calculate_delays(dataset, venster_on, title):
    n_freq = dataset.size//dataset[0].size
    n_pos = dataset[0].size//dataset[0][0].size # 24
    n_measure = dataset[0][0].size
    timestep = ((10**-7)/n_freq)*10**9
    APDP_values = [None] * n_pos;
    delays = np.asarray([None] * n_pos)
    for i in range(delays.size):
        delays[i] = np.asarray([0.00, 0.00])
    
    for i in range(n_pos):
        APDP_values[i] = channel2APDP(dataset, i, n_freq, n_measure,venster = venster_on);

    APDP_values = np.asarray(APDP_values) 
    x_time_values = np.asarray([None] * APDP_values[0].size)
    for i in range(APDP_values[0].size):
        x_time_values[i] = i * timestep
        
    plt.figure(figsize=(10, 10))
    plt.title(label=title) 
    plt.xlim(right=40)
    plt.xlim(left=0)
    plt.xlabel('delay (ns)')
    plt.ylabel('APDP')
    for i in range(n_pos):
        plt.plot(x_time_values, APDP_values[i])
         
    for i in range(delays.size):
        delays[i][0], delays[i][1] = APDP2delays(APDP_values[i], timestep)
    return delays

# =============================================================================
# De APDP berekenen bij een bepaalde positie
# =============================================================================
def channel2APDP(data, pos, n_freq, n_measure, venster = 0):
    APDP = np.zeros(n_freq)
    for i in range (n_measure): # We itereren 100 keer omdat er per plaats 100 keer de frequentiekarakteristiek is gemeten
        f_karakteristiek = [None] * n_freq
        for j in range(n_freq): # Alle frequenties worden overlopen, bv. van 1GHz to 3GHz voor dataset 1(201 meetpunten in totaal)
            f_karakteristiek[j] = data[j][pos][i]
        
        if(venster == 1) : # er kan gekozen worden om een window toe te passen
            s_ifft = ifft(f_karakteristiek*gaussian(n_freq, 40))
        else:
            s_ifft = ifft(f_karakteristiek)
        
        power = (abs(s_ifft))**2 # het vermogen berekenen
        som = np.sum(power) # de som
        PDP = power/som # de PDP berekenen
        APDP += PDP
     
    APDP = APDP/n_measure # Het gemiddelde nemen van de 100 meetpunten
    return APDP

# =============================================================================
# De delays uit de APDP halen
# =============================================================================
def APDP2delays(APDP, timestep):
    peak1 = 0
    peak2 = 0
    pos_peak1= 0
    pos_peak2= 0
    maximum_indices, properties = find_peaks(APDP, height = 0) # Vind de indexen van de peaken
    heights = properties["peak_heights"] # Hoogte van alle peaken opvragen
    
    for i in range(heights.size):
        if(heights[i] > peak1): # Grootste peak
            pos_peak1 = maximum_indices[i]
            peak1 = heights[i];
        elif(heights[i] > peak2): # 2de hoogste peak
            pos_peak2 = maximum_indices[i]
            peak2 = heights[i]

    return (pos_peak1*timestep), (pos_peak2*timestep)
