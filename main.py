import scipy.io
from delay_functions import * 
from pathlib import Path
import matplotlib.pyplot as plt
from delay_functions import calculate_delays
from location_functions import calculate_locations, get_locations
from sympy.solvers import solve
from sympy import Symbol, sqrt


def get_matfile(name):
	dirname = Path(__file__).parent.parent
	return (dirname / name).resolve()
def plot_course():
    loc_array = get_locations()
    plt.figure(figsize=(8, 8))
    plt.xlim(left=0)
    plt.xlim(right=8)
    plt.ylim(bottom=0)
    plt.ylim(top=5)
    plt.plot(0,1, marker="x", color='r', mew=3)
    for i in range(loc_array.size):
        plt.plot(loc_array[i][0], loc_array[i][1], marker=".", color='k', mew=1)
    

mat1 = scipy.io.loadmat(get_matfile("Dataset_1.mat"))
mat2 = scipy.io.loadmat(get_matfile("Dataset_2.mat"))

delays = calculate_delays(mat1.get('H'))
print("Delays:", *delays, sep = "\n")

plot_course()

c = Symbol('c')
answers = solve((1+c)**2+(sqrt((3.6)**2-c**2)-sqrt((5/(2+c))**2-1))**2-(5-5/(2+c))**2, c)
print("Answer pos1: ",answers)