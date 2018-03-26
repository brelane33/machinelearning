import random
import numpy as np
import matplotlib.pyplot as plt

#declare globals
N = 20
classY = []
classX = []
misclassX = []
misclassY = []
adjustment = 0
adjust = True
xcoord1, xcoord2 = 0, 1
w0, w1, w2 = 0, 1, 2

#generate data
data = np.random.random((N, 2))
xdata = data[:,0]
ydata = data[:,1]
xycoord = list(zip(xdata, ydata)) #create list of 2-tuples of coordinates

#generate ideal function to initially classify all points +1 or -1
x1, y1, x2, y2 = [random.random() for i in range(4)]
weights = np.array([x2*y1 - x1*y2, y2-y1, x1-x2])

x = np.linspace(0,1)
m = -weights[w1]/weights[w2]
b = -weights[w0]/weights[w2]

#classify
for coordinate in xycoord:
	sign = np.sign(np.matrix([weights[w0],weights[w1],weights[w2]]) * \
	 np.matrix([1, coordinate[xcoord1], coordinate[xcoord2]]).transpose())
	#the transpose of the matrix X (x0, x1, x2) is multiplied by W (w0, w1, w2)
	#and the sign of this multiplcation is taken. the sign is then used to classify
	#the data points.
	if(sign[0] == 1):
		classX.append(coordinate[xcoord1])
		classY.append(coordinate[xcoord2])
	if(sign[0] == -1):
		misclassX.append(coordinate[xcoord1])
		misclassY.append(coordinate[xcoord2])


#all updating code is below here
classcoord = list(zip(classX, classY))
miscoord = list(zip(misclassX, misclassY))

#guess to see if the points were correctly classified
newWeight = np.matrix([np.random.random(3)])

while(adjust == True):

	w0, w1, w2 = newWeight.item(0), newWeight.item(1), newWeight.item(2)

	for coordinate in xycoord:
		adjust = False
		coordinates = np.matrix([1, coordinate[xcoord1], coordinate[xcoord2]]).transpose()
		sign = np.sign(newWeight * coordinates)[0]

		if(sign == 1 or sign == 0):
			if coordinate not in classcoord:
				newWeight = newWeight - coordinates.transpose()
				adjust = True
				break
		elif(sign == -1):
			if coordinate not in miscoord:
				newWeight = newWeight + coordinates.transpose()
				adjust = True
				break
		
		adjustment += 1
		print("iteration: ", adjustment)

newx = np.linspace(0,1)
newm = -w1/w2
newb = -w0/w2


#plot all the things/```q
plt.plot(x, m*x+b, 'g', label='f(x)')
plt.plot(newx, newm*newx+newb, label='newf(x)', c="yellow")  #plot line
plt.scatter(classX, classY, c="blue")  #plot classified points
plt.scatter(misclassX, misclassY, c="red") #plot misclassified points
plt.xlabel('testing')
plt.show()

"""	plug into for loop to better understand math

	print("Matrix X: ", np.matrix([1, coordinate[xcoord1], coordinate[xcoord2]]))

	print("Matrix X^T: ", np.matrix([1, coordinate[xcoord1], coordinate[xcoord2]]).transpose(), '\n')

	print("Matrix W: ", np.matrix([weights[w0],weights[w1],weights[w2]]), '\n')

	print("X^T * W: ", np.matrix([weights[w0],weights[w1],weights[w2]]) * \
	 np.matrix([1, coordinate[xcoord1], coordinate[xcoord2]]).transpose(), '\n')

	print("sign(X^T * W): ", np.sign(np.matrix([weights[w0],weights[w1],weights[w2]]) * \
	 np.matrix([1, coordinate[xcoord1], coordinate[xcoord2]]).transpose()),'\n')
"""