import scipy.io
from delay_functions import * 
from pathlib import Path
import matplotlib.pyplot as plt
from delay_functions import calculate_delays
from location_functions import calculate_locations, get_locations


def get_matfile(name):
	dirname = Path(__file__).parent.parent
	return (dirname / name).resolve()

mat1 = scipy.io.loadmat(get_matfile("Dataset_1.mat"))
mat2 = scipy.io.loadmat(get_matfile("Dataset_2.mat"))

delays = calculate_delays(mat1.get('H'))
print(delays)

loc_array = get_locations()
plt.figure(figsize=(10, 10))
for i in range(loc_array.size):
    plt.plot(loc_array[i][0], loc_array[i][1], marker=".", color='k', mew=1)