import numpy as np
import matplotlib.pyplot as plt

dataset = np.empty([40,8])

data = np.random.randint(0,2, (40,8))
data_output = [sum(vect) for vect in data]
print(data_output)

y = np.empty(40)
for i in range(0,40):
  for j in range(0,8):
    if(dataset[i][j]==1):
      y[i]+=1

data = np.random.randint(0,2, (40,8))


#print(y)

fic = open("data_kmeans.txt","r")

lines = fic.read().splitlines()
kmeans_data = np.array([ [float(digit) for digit in line.split(' ') ] for line in lines])
x = kmeans_data[:,0]
y = kmeans_data[:,1]
print(x)
plt.plot(x, y, '.')
plt.show()

fich = open("data_pca.txt","r")
lines = fich.read().splitlines()
pca_data = np.array([ [float(digit) for digit in line.split(' ') ] for line in lines])
x_pca = pca_data[:,0]
y_pca = pca_data[:,1]
print(x_pca)
plt.plot(x_pca, y_pca, '.')
plt.show()
