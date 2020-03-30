from math import *
import numpy as np
import scipy as sp
from scipy.fftpack import *
from scipy.signal import *

def calculate_delays(dataset):
    n_fasor = dataset.get('H')[0][0].size # total = 100
    n_pos = dataset.get('H')[0].size // dataset.get('H')[0][0].size # total = 24
    n_freq =  dataset.get('H').size // dataset.get('H')[0].size # total = 201
    
    APDP_values = np.arange(0.00, 24.00);
    
    for i in range(24): # De 24 posities doorlopen
        APDP_values[i] = channel2APDP(dataset.get('H'), i);
    print(APDP_values)
    
def channel2APDP(dataset, pos):
    APDP = 0.00
    PDP_array = PDP_calc(dataset, pos) # voor 1 positie de PDP waarden gaan berekenen (want er 100 keer gemeten op 1 positie)
    for i in range(PDP_array.size):
        APDP += PDP_array[i] # alle PDP waarden optellen
    APDP = APDP / PDP_array.size # het gemiddelde ervan nemen
    return APDP

def PDP_calc(dataset, pos):
    PDP_values = [None] * 100;
    frequentiekarakteristiek = [complex] * 201
    
    for i in range(100): # er wordt 100 keer gekeken vanwege dat er 100 keer werd gemeten per positie
        for j in range(201): # elke frequentie overlopen, van 1GHz tot 3GHz
            frequentiekarakteristiek[j] = dataset[j][pos][i] # de complexe getallen van elke frequentie in het array steken
        frequentiekarakteristiek = np.asarray(frequentiekarakteristiek)   
        ifft_freq = ifft(frequentiekarakteristiek) 
        ifft_freq = abs(ifft_freq)
        power_value = sp.sum(ifft_freq*ifft_freq)/ifft_freq.size # het vermogen van het signaal berekenen
        PDP_values[i] = power_value # de vermogens opslaan in het array
        PDP_values = np.asarray(PDP_values)
    return PDP_values
            
            
