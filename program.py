import scipy.io
mat = scipy.io.loadmat('Dataset_1.mat')

print(mat.get('H')[0][0].size)
print(mat.get('H')[0].size)
print(mat.get('H').size)

print(mat.get('H')[0][0][0].real)
print(mat.get('H')[0][0][0].imag)
