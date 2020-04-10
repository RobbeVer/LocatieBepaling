import numpy as np
from scipy.fftpack import ifft
from scipy.signal import gaussian
import matplotlib.pyplot as plt

def coswav(f, fs, duur):
    lengte = fs * duur
    stap = 2 * np.pi * f / fs
    return np.cos(np.arange(0, lengte * stap, stap))

# Uit ADPD de delays berekenen:
def calculate_delays(dataset): 
    APDP_values = [None] * 24;
    for i in range(24):
        APDP_values[i] = channel2APDP(dataset, i);
     
    plt.figure(figsize=(10, 10))
    for i in range(24):
        plt.plot(APDP_values[i])

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
    
#def channel2APDP(dataset, pos):
#    APDP = 0.00
#    PDP_array = PDP_calc(dataset, pos) # voor 1 positie de PDP waarden gaan berekenen (want er 100 keer gemeten op 1 positie)
#    for i in range(PDP_array.size):
#        APDP += PDP_array[i] # alle PDP waarden optellen
#    APDP = APDP / PDP_array.size # het gemiddelde ervan nemen
#    return APDP
#
#def PDP_calc(dataset, pos):
#    PDP_values = [None] * 100;
#    frequentiekarakteristiek = [complex] * 201
#    
#    for i in range(100): # er wordt 100 keer gekeken vanwege dat er 100 keer werd gemeten per positie
#        for j in range(201): # elke frequentie overlopen, van 1GHz tot 3GHz
#            frequentiekarakteristiek[j] = dataset[j][pos][i] # de complexe getallen van elke frequentie in het array steken
#        frequentiekarakteristiek = np.asarray(frequentiekarakteristiek)   
#        ifft_freq = ifft(frequentiekarakteristiek) 
#        ifft_freq = abs(ifft_freq)
#        power_value = sp.sum(ifft_freq**2)/ifft_freq.size # het vermogen van het signaal berekenen
#        PDP_values[i] = power_value # de vermogens opslaan in het array
#        PDP_values = np.asarray(PDP_values)
#        plt.plot(ifft_freq)
#    return PDP_values
       