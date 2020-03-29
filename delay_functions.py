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
        
    channel2APDP(dataset.get('H'), 0, frequencies);
    

def channel2APDP(dataset, pos, frequencies):
    frequentiekarakteristiek = [complex] * 201
    
    for i in range(201):
        frequentiekarakteristiek[i] = dataset[i][pos][0]
    
    frequentiekarakteristiek = asarray(frequentiekarakteristiek) 
    
    absF = abs(frequentiekarakteristiek)
    fftFreq = fftfreq(len(absF), 1/(len(absF)))
    
    ifft_freq= ifft(frequentiekarakteristiek)
    
    plt.figure(figsize=(10, 10))
    plt.subplot(211)
    plt.plot(frequencies, absF, color='r', label='Frequency response')
    plt.legend()
    plt.subplot(212)
    plt.plot(fftFreq, absF, color='b', label='Frequency response')
    plt.legend()