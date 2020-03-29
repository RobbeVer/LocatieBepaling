import scipy.io
from delay_functions import * 

mat1 = scipy.io.loadmat('D:\\OneDrive\\UGent\\Schakeljaar\\Digitale signaalverwerking\\Project\\Dataset_1.mat')
mat2 = scipy.io.loadmat('D:\\OneDrive\\UGent\\Schakeljaar\\Digitale signaalverwerking\\Project\\Dataset_2.mat')

calculate_delays(mat1)