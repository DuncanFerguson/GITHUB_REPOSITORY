import numpy as np

fout = open('tempData.npy','wb') 

NA = 3
NB = 3
NC = 3
ND = 2

mat = np.random.rand(NA,NB,NC,ND)
print(mat)

np.save(fout,mat)

# Attempt to read using file.read() -> just reads as a blob  (binary large object)
fin = open('tempData.npy','rb')
matRead = fin.read()
print("\n\nPrinting out what was read in fia fin.read():\n")
print(matRead)
#print(matRead.shape)  # uncommenting this causes an error


# Instead use np.load => this will read in as a numpy array
matRead2 = np.load('tempData.npy')
print("\n\nPrinting out what was read in using np.load():\n")
print(matRead2)
print(matRead2.shape)

