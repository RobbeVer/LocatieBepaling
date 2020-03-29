import scipy.io

mat1 = scipy.io.loadmat('D:\\OneDrive\\UGent\\Schakeljaar\\Digitale signaalverwerking\\Project\\Dataset_1.mat')
mat2 = scipy.io.loadmat('D:\\OneDrive\\UGent\\Schakeljaar\\Digitale signaalverwerking\\Project\\Dataset_2.mat')
# mat1.get('H')[0][0][0] = complex getal of phasor, in totaal zijn er 100, dus van [0][0][0] tot [0][0][99]
# mat1.get('H')[0][0] = is een vliegtuig positie, in totaal zijn er 24, dus van [0][0] tot [0][23]
# mat1.get('H')[0] = is een frequentietoon, in totaal zijn er 201, dus van [0] tot [200]
# mat1.get('H')[0][0][0].real = het reëel gedeelte van de phasor
# mat1.get('H')[0][0][0].imag = het imaginair gedeelte van de phasor

def calculate_delays(dataset):
    n_fasor = dataset.get('H')[0][0].size # total = 100
    n_pos = dataset.get('H')[0].size // dataset.get('H')[0][0].size # total = 24
    n_freq =  dataset.get('H').size // dataset.get('H')[0].size # total = 201

def channel2APDP(dataset):
    return 0;

calculate_delays(mat1)