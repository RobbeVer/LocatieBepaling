import scipy.io
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from delay_functions import calculate_delays
from location_functions import calculate_locations, get_locations

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

for i in range(delays.size):
    print("delays op index",i,":",delays[i])

loc_array = get_locations()
loc_x_array = np.asarray([None] * 24)
loc_y_array = np.asarray([None] * 24)
for i in range(loc_array.size):
    loc_x_array[i] = loc_array[i][0]
    loc_y_array[i] = loc_array[i][1]

locations = calculate_locations(delays)
locations_x = np.asarray([None] * 24)
locations_y = np.asarray([None] * 24)
for i in range(locations.size):
    locations_x[i] = locations[i][0]
    locations_y[i] = locations[i][1]
for i in range(locations.size):
    print("locations op index",i,":",locations[i])

# =============================================================================
# Plot baan die drone beschrijft
# =============================================================================
print("Delays:", *delays, sep = "\n")

locations = calculate_locations(delays)
print("Position:", *locations, sep = "\n")

loc_array = get_locations()
plt.figure(figsize=(8, 8))
plt.xlim(left=0)
plt.xlim(right=8)
plt.ylim(bottom=0)
plt.ylim(top=5)
plt.plot(0,1, marker="x", color='r', mew=3)
plt.scatter(loc_x_array, loc_y_array, marker='o', color='k')
plt.plot(loc_x_array, loc_y_array, color='k')
plt.scatter(locations_x, locations_y, marker='s', color='b')
plt.plot(locations_x, locations_y, color='b')
