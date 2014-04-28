import sys
from Object import *

class Handler:

	def __init__(self,shapeGroups):
		self.shapeGroups = shapeGroups

	def findContainer(self):
		for shapeg in self.shapeGroups:
			for shape in shapeg:
				