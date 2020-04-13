import scipy.io
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from delay_functions import calculate_delays
from location_functions import calculate_locations, get_locations

def get_matfile(name):
	dirname = Path(__file__).parent.parent
	return (dirname / name).resolve()

mat1 = scipy.io.loadmat(get_matfile("Dataset_1.mat"))
mat2 = scipy.io.loadmat(get_matfile("Dataset_2.mat"))

delays1 = calculate_delays(mat1.get('H'))
delays2 = calculate_delays(mat2.get('H'))

loc_array = get_locations()
loc_x_array = np.asarray([None] * 24)
loc_y_array = np.asarray([None] * 24)
for i in range(loc_array.size):
    loc_x_array[i] = loc_array[i][0]
    loc_y_array[i] = loc_array[i][1]

locations1 = calculate_locations(delays1)
locations1_x = np.asarray([None] * 24)
locations1_y = np.asarray([None] * 24)
for i in range(locations1.size):
    locations1_x[i] = locations1[i][0]
    locations1_y[i] = locations1[i][1]

locations2 = calculate_locations(delays2)
locations2_x = np.asarray([None] * 24)
locations2_y = np.asarray([None] * 24)
for i in range(locations2.size):
    locations2_x[i] = locations2[i][0]
    locations2_y[i] = locations2[i][1]

# =============================================================================
# Plot baan die drone beschrijft
# =============================================================================
loc_array = get_locations()
plt.figure(figsize=(8, 8))
plt.xlim(left=0)
plt.xlim(right=8)
plt.ylim(bottom=0)
plt.ylim(top=5)
plt.plot(0,1, marker="x", color='r', mew=3)
plt.scatter(loc_x_array, loc_y_array, marker='o', color='k')
plt.plot(loc_x_array, loc_y_array, color='k')

plt.scatter(locations1_x, locations1_y, marker='s', color='b')
plt.plot(locations1_x, locations1_y, color='b')

plt.scatter(locations2_x, locations2_y, marker='h', color='g')
plt.plot(locations2_x, locations2_y, color='g')
