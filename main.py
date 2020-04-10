import scipy.io
from delay_functions import calculate_delays
from location_functions import calculate_locations, get_locations
import matplotlib.pyplot as plt

mat1 = scipy.io.loadmat('D:\\OneDrive\\UGent\\Schakeljaar\\Digitale signaalverwerking\\Project\\Dataset_1.mat')
mat2 = scipy.io.loadmat('D:\\OneDrive\\UGent\\Schakeljaar\\Digitale signaalverwerking\\Project\\Dataset_2.mat')

delays = calculate_delays(mat1.get('H'))
print(delays)

loc_array = get_locations()
plt.figure(figsize=(10, 10))
for i in range(loc_array.size):
    plt.plot(loc_array[i][0], loc_array[i][1], marker=".", color='k', mew=1)