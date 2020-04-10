import scipy.io
from delay_functions import * 
from pathlib import Path

def get_matfile(name):
	dirname = Path(__file__).parent.parent
	return (dirname / name).resolve()

mat1 = scipy.io.loadmat(get_matfile("Dataset_1.mat"))
mat2 = scipy.io.loadmat(get_matfile("Dataset_2.mat"))

calculate_delays(mat1.get('H'))