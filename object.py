import sys,pygame
from numpy import *

class Object:

	def __init__(self,x1,y1,x2,y2):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2


	def getX1(self):
		return self.x1

	def getX2(self):
		return self.x2

	def getY1(self):
		return self.y1

	def getY2(self):
		return self.y2

	def setX1(self,x):
		self.x1 = x

	def setX2(self,x):
		self.x2 = x

	def setY1(self,y):
		self.y1 = y

	def setY2(self,y):
		self.y2 = y



class Shape(Object):

	def __init__(self,*points):
		self.pointList = []
		self.edges = []
		self.vEdges = []
		self.hEdges = []
		for point in points:
			self.pointList.append(point)

	def findEdges(self):

		self.objMap = zeros((100,100), dtype=int)
		outerEdges = []

		for index,point in enumerate(self.pointList):
			edges.append(Edge(point,point[index+1],self))

		for edge in edges:
			if edge.getX1() == edge.getX2():
				self.vEdges.append(edge)
			elif edge.getY1() == edge.getY2():
				self.hEdges.append(edge)

		#Find outer edges to shape
		lowest = 100
		highest = 0
		for edge in self.vEdges:
			if edge.getX1() < lowest:
				lowest = edge.getX1()
				leftEdge = edge

		for edge in self.vEdges:
			if edge.getX1() > highest:
				highest = edge.getX1()
				rightEdge = edge

		lowest = 100
		highest = 0

		for edge in self.hEdges:
			if edge.getY1() < lowest:
				lowest = edge.getY1()
				bottomEdge = edge
		for edge in self.hEdges:
			if edge.getY1() > highest:
				highest = edge.getY1()
				topEdge = edge

		leftEdge.setType('RIGHT')
		rightEdge.setType('LEFT')
		bottomEdge.setType('TOP')
		topEdge.setType('BOTTOM')
		outerEdges.append(leftEdge,rightEdge,bottomEdge,topEdge)

		longest = 0
		for edge in outerEdges:
			if edge.getLength() > longest:
				longestEdge = edge
				longest = edge.getLength()

		if longestEdge == leftEdge:
			xx = leftEdge.getX1()
			yy = leftEdge.getY1()
			while yy < leftEdge.getY2():
				for edge in self.vEdges:
					if edge.getX1() == xx and not edge.getX1() == leftEdge.getX1():
						xx = leftEdge.getX1()
						yy += 1
				objMap[xx,yy] = 1
				xx+=1

		elif longestEdge == rightEdge:
			xx = rightEdge.getX1()
			yy = rightEdge.getY1()
			while yy < rightEdge.getY2():
				for edge in self.vEdges:
					if edge.getX1() == xx and not edge.getX1() == rightEdge.getX1():
						xx = leftEdge.getX1()
						yy += 1
				objMap[xx,yy] = 1
				xx-=1

		elif longestEdge == bottomEdge:
			xx = bottomEdge.getX1()
			yy = bottomEdge.getY1()
			while xx < bottomEdge.getX2():
				for edge in self.hEdges:
					if edge.getY1() == yy and not edge.getY1() == bottomEdge.getY1():
						yy = bottomEdge.getY1()
						xx += 1
				objMap[xx,yy] = 1
				yy-=1

		elif longestEdge == topEdge:
			xx = topEdge.getX1()
			yy = topEdge.getY1()
			while xx < topEdge.getX2():
				for edge in self.hEdges:
					if edge.getY1() == yy and not edge.getY1() == topEdge.getY1():
						yy = bottomEdge.getY1()
						xx += 1
				objMap[xx,yy] = 1
				yy+=1		
		


		for edge in self.vEdges:
			if edge.hasType == False:
				y1 = edge.getY1()
				y2 = edge.getY2()
				x = edge.getX1()
				probe = [x+1,abs(y1,y2)/2]
				if objMap[probe] == 1:
					edge.setType('RIGHT')
				else:
					edge.setType('LEFT')

		for edge in self.hEdges:
			if edge.hasType == False:
				x1 = edge.getX1()
				x2 = edge.getX2()
				y = edge.getY1()
				probe = [y+1,abs(x1,x2)/2]
				if objMap[probe] == 1:
					edge.setType('BOTTOM')
				else:
					edge.setType('TOP')


class Edge(Object):

	def __init__(self,point1,point2,parentShape):
		self.setPoint1(point1)
		self.setPoint2(point2)
		self.parentShape = parentShape
		self.hasTypeBool = False

	def setPoint1(self,point):
		self.point1 = point
		self.x1 = point[0]
		self.y1 = point[1]

	def setPoint2(self,point):
		self.point2 = point
		self.x2 = point[0]
		self.y2 = point[1]

	def getPoint1(self):
		return self.point1

	def getPoint2(self):
		return self.point2

	def getParent(self):
		return self.parentShape

	def setType(self,edgeType):
		self.edgeType = edgeType
		self.hasTypeBool = True

	def getType(self):
		return self.edgeType

	def hasType(self):
		return self.hasTypeBool

	def getLength(self):
		if self.getX1() == self.getX2():
			return abs(self.getY1(),self.getY2())
		else:
			return abs(self.getX1(),self.getX2())


class Container(Object):

	def setScore(self,score):
		self.score = score

	def getScore(self):
		return self.score
