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
    
    for i in range(24):
        APDP_values[i] = channel2APDP(dataset.get('H'), i);
    print(APDP_values)
    
def channel2APDP(dataset, pos):
    APDP = 0.00
    PDP_array = PDP_calc(dataset, pos)
    for i in range(PDP_array.size):
        APDP += PDP_array[i]
    APDP = APDP / PDP_array.size
    return APDP

def PDP_calc(dataset, pos):
    PDP_values = [None] * 100;
    frequentiekarakteristiek = [complex] * 201
    
    for i in range(100):
        for j in range(201):
            frequentiekarakteristiek[j] = dataset[j][pos][i]  
        frequentiekarakteristiek = np.asarray(frequentiekarakteristiek)   
        ifft_freq = ifft(frequentiekarakteristiek) 
        ifft_freq = abs(ifft_freq)
        power_value = sp.sum(ifft_freq*ifft_freq)/ifft_freq.size
        PDP_values[i] = power_value
        PDP_values = np.asarray(PDP_values)
    return PDP_values
            
            
