import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Renderer():
	def __init__(self, size):
		self.size = size
		self.imagePrim = np.zeros((self.size, self.size))
		self.fig = plt.figure()
		self.image = plt.imshow(self.imagePrim, cmap='gray', vmin=0, vmax=25)
		plt.axis('off')

	def setData(self, x, y, val):
		self.imagePrim[x,y] = val
		self.image.set_array(self.imagePrim)

	def render(self):
		plt.pause(0.00001)

	def finalShow(self):
		plt.show()