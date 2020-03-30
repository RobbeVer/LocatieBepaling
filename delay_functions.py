from math import *
from numpy import *
from scipy import *
from scipy.fftpack import *
from scipy.signal import *
import matplotlib.pyplot as plt


def calculate_delays(dataset):
    n_fasor = dataset.get('H')[0][0].size # total = 100
    n_pos = dataset.get('H')[0].size // dataset.get('H')[0][0].size # total = 24
    n_freq =  dataset.get('H').size // dataset.get('H')[0].size # total = 201
    
    frequencies = arange(0.00,  n_freq, 1)
    for i in range (n_freq):
        frequencies[i] = (1 + 0.01 * i)*10**9;
      
    for i in range(24):
        PDP_values = channel2APDP(dataset.get('H'), i, frequencies);
    
def channel2APDP(dataset, pos):
    APDP = 0.00
    for i in range()

def channel2PDP(dataset, pos, frequencies):
    PDP_values = [None] * 100;
    frequentiekarakteristiek = [complex] * 201
    
    for i in range(201):
        frequentiekarakteristiek[i] = dataset[i][pos][0]
    
    frequentiekarakteristiek = asarray(frequentiekarakteristiek) 
    
    ifft_freq = ifft(frequentiekarakteristiek)
    
    absF = abs(frequentiekarakteristiek)    
    fftFreq = fftfreq(len(absF), 1/(len(absF)))
    power = ifft_freq**2;
    
    plt.figure(figsize=(10, 10))
    plt.subplot(311)
    plt.plot(frequencies, absF, color='r', label='Frequency response')
    plt.legend()
    plt.subplot(312)
    plt.plot(power, color='k', label='absF')
    plt.legend()
    
