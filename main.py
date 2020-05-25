import scipy.io
import csv
import numpy as np
import os
from pathlib import Path
import matplotlib.pyplot as plt
from delay_functions import calculate_delays
from location_functions import calculate_locations, get_locations

def get_matfile(name):
	dirname = Path(__file__).parent.parent
	return (dirname / name).resolve()

def export_to_csv(data, name):
    file_name =  '../csv_files/' + name + '.csv'
    with open(file_name, mode='w', newline='') as data_file:
        data_write = csv.writer(data_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)        
        data_write.writerow(['x','y'])
        for i in range(data.size):
            data_write.writerow([data[i][0].round(2), data[i][1].round(2)])
            
def print_locations(name, locations):
    print('Locaties van ' + name)
    for i in range(locations.size):
        text = '  locatie ' + str(i+1) + ':\n    x = ' + str(locations[i][0]) + '\n    y = ' + str(locations[i][1])
        print(text)
        i == locations.size-1 and print('')
            
def plot_path(x_array, y_array, marker, color, title):
    plt.figure(figsize=(8, 8))
    plt.grid(b=True)
    plt.xlim(left=-1)
    plt.xlim(right=7)
    plt.ylim(bottom=0)
    plt.ylim(top=5)
    plt.xlabel('plaats x (m)')
    plt.ylabel('plaats y (m)')
    plt.title(label=title)
    plt.scatter(0,1, marker="o", color='g', label='station')
    plt.plot(x_array, y_array, marker=marker, color=color, label='baan drone')
    plt.legend()

mat1 = scipy.io.loadmat(get_matfile("Dataset_1.mat"))
mat2 = scipy.io.loadmat(get_matfile("Dataset_2.mat"))

delays1_a = calculate_delays(mat1.get('H'), venster_on=1, title='Dataset 1 met venster') # dataset 1 met venster
delays1_b = calculate_delays(mat1.get('H'), venster_on=0, title='Dataset 1 zonder venster') # dataset 1 zonder venster
delays2_a = calculate_delays(mat2.get('H'), venster_on=1, title='Dataset 2 met venster') # dataset 2 met venster
delays2_b = calculate_delays(mat2.get('H'), venster_on=0, title='Dataset 2 zonder venster') # dataset 2 zonder venster

loc_array = get_locations()
loc_x_array = np.asarray([None] * 24)
loc_y_array = np.asarray([None] * 24)
for i in range(loc_array.size):
    loc_x_array[i] = loc_array[i][0]
    loc_y_array[i] = loc_array[i][1]

locations1_a = calculate_locations(delays1_a)
locations1_a_x = np.asarray([None] * 24)
locations1_a_y = np.asarray([None] * 24)
for i in range(locations1_a.size):
    locations1_a_x[i] = locations1_a[i][0]
    locations1_a_y[i] = locations1_a[i][1]

locations2_a = calculate_locations(delays2_a)
locations2_a_x = np.asarray([None] * 24)
locations2_a_y = np.asarray([None] * 24)
for i in range(locations2_a.size):
    locations2_a_x[i] = locations2_a[i][0]
    locations2_a_y[i] = locations2_a[i][1]
    
locations1_b = calculate_locations(delays1_b)
locations1_b_x = np.asarray([None] * 24)
locations1_b_y = np.asarray([None] * 24)
for i in range(locations1_b.size):
    locations1_b_x[i] = abs(locations1_b[i][0]) # Hier wordt de absolute waarde genomen omdat er complexe waarden tussen zitten die zorgen voor problemen
    locations1_b_y[i] = abs(locations1_b[i][1])

locations2_b = calculate_locations(delays2_b)
locations2_b_x = np.asarray([None] * 24)
locations2_b_y = np.asarray([None] * 24)
for i in range(locations2_b.size):
    locations2_b_x[i] = abs(locations2_b[i][0]) # Hier wordt de absolute waarde genomen omdat er complexe waarden tussen zitten die zorgen voor problemen
    locations2_b_y[i] = abs(locations2_b[i][1])

errors1_a = abs(locations1_a - loc_array)
errors1_b = abs(locations1_b - loc_array)
errors2_a = abs(locations2_a - loc_array)
errors2_b = abs(locations2_b - loc_array)

# =============================================================================
# CSV bestanden maken
# =============================================================================
if not os.path.exists('../csv_files/'):
    os.makedirs('../csv_files/')
export_to_csv(loc_array, 'original_coordinates')
export_to_csv(locations1_a, 'locations1_a_coordinates')
export_to_csv(locations1_b, 'locations1_b_coordinates')
export_to_csv(locations2_a, 'locations2_a_coordinates')
export_to_csv(locations2_b, 'locations2_b_coordinates')
export_to_csv(errors1_a, 'errors1_a')
export_to_csv(errors1_b, 'errors1_b')
export_to_csv(errors2_a, 'errors2_a')
export_to_csv(errors2_b, 'errors2_b')

# =============================================================================
# Print de locaties uit
# =============================================================================
print_locations('dataset 1', locations1_a)
print_locations('dataset 2', locations2_a)

# =============================================================================
# Plot de baan die drone beschrijft
# =============================================================================
plot_path(loc_x_array, loc_y_array, marker='o', color='k', title='Origineel pad')
plot_path(locations1_b_x, locations1_b_y, marker='s', color='r', title='Dataset 1 zonder venster')
plot_path(locations1_a_x, locations1_a_y, marker='s', color='b', title='Dataset 1 met venster')
plot_path(locations2_b_x, locations2_b_y, marker='D', color='r', title='Dataset 2 zonder venster')
plot_path(locations2_a_x, locations2_a_y, marker='D', color='b', title='Dataset 2 met venster')
