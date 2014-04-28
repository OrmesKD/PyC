import sys
from obj import *


def search(Shapes):
	edgesList = []
	for shape in Shapes:
		temp = shape.findEdges()
		for edge in temp:
			edgesList.append(edge)

	# for edge in edgesList:
 # 		print str(edge.getPoint1()) + " to " + str(edge.getPoint2()) + " is a " + str(edge.getType())

 	top = []
 	bottom = []
 	left = []
 	right = []
 	
 	for edge in edgesList:
	 	if edge.getType() == 'TOP':
	 		top.append(edge)
	 	elif edge.getType() == 'BOTTOM':
	 		bottom.append(edge)
	 	elif edge.getType() == 'LEFT':
	 		left.append(edge)
	 	elif edge.getType() == 'RIGHT':
	 		right.append(edge)

 	#PICK A BOTTOM
	for edge in bottom:
		print '----------START----------'
		eList = []
 		adjEdges = []
 		tempList = []
		possibleAdj = []
		leftAdj = []
		rightAdj = []
		leftGroup = []
		rightGroup = []

		tempLeft = left
		tempRight = right
		tempBottom = bottom
		tempTop = top
		

		eList.append(tempLeft)
		eList.append(tempRight)
		eList.append(tempTop)
		eList.append(tempBottom)

		bottomEdge = edge

		#print 'Bottom Edge:', str(bottomEdge.getPoint1()), str(bottomEdge.getPoint2())

		tempLeft = [e for e in tempLeft if not (e.getParent() == bottomEdge.getParent() and (e.getY1() > bottomEdge.getY1() or e.getY2() > bottomEdge.getY2()))]
		tempRight = [e for e in tempRight if not (e.getParent() == bottomEdge.getParent() and (e.getY1() > bottomEdge.getY1() or e.getY2() > bottomEdge.getY2()))]
		tempBottom = [e for e in tempBottom if not (e.getParent() == bottomEdge.getParent() and (e.getY1() > bottomEdge.getY1() or e.getY2() > bottomEdge.getY2()))]
		tempTop = [e for e in tempTop if not (e.getParent() == bottomEdge.getParent() and (e.getY1() > bottomEdge.getY1() or e.getY2() > bottomEdge.getY2()))]

		possibleAdj.append(bottomEdge.hasAdjacent(tempLeft))
		possibleAdj.append(bottomEdge.hasAdjacent(tempRight))

		
		for adj in possibleAdj:
			if adj and (adj.getY1() <= bottomEdge.getY1() and adj.getY2() <= bottomEdge.getY1()):
				adjEdges.append(adj)
				print str(adj.getType()),'edge found: ', str(adj.getPoint1()), str(adj.getPoint2())
		
		
		#PICK A TOP
		for edge in tempTop:
			if not edge.getLength() == bottomEdge.getLength():
				continue
			else:
				topEdge = edge
				#print 'Top Edge:', str(topEdge.getPoint1()), str(topEdge.getPoint2())
				tempLeft = [e for e in tempLeft if not (e.getParent() == shape and (e.getY1() < topEdge.getY1() or e.getY2() < topEdge.getY2()))]
 				tempRight = [e for e in tempRight if not (e.getParent() == shape and (e.getY1() < topEdge.getY1() or e.getY2() < topEdge.getY2()))]
 				tempBottom = [e for e in tempBottom if not (e.getParent() == shape and (e.getY1() < topEdge.getY1() or e.getY2() < topEdge.getY2()))]
 				tempTop = [e for e in tempTop if not (e.getParent() == shape and (e.getY1() < topEdge.getY1() or e.getY2() < topEdge.getY2()))]

 				possibleAdj.append(topEdge.hasAdjacent(tempLeft))
 				possibleAdj.append(topEdge.hasAdjacent(tempRight))

 				for adj in possibleAdj:
					if adj and (adj.getY1() >= topEdge.getY1() and adj.getY2() >= topEdge.getY1()):
						adjEdges.append(adj)
						print str(adj.getType()),'edge found: ', str(adj.getPoint1()), str(adj.getPoint2())

			#PICK A LEFT

			for adj in adjEdges:
				if adj.getType() == 'LEFT':
					leftAdj.append(adj)
				else:
					rightAdj.append(adj)
			print 'How many left adjacents:', str(len(leftAdj))
			print 'How many right adjacents:', str(len(rightAdj))
			if len(leftAdj) > 0:
				print 'left conflict'
				combinedLeft = 0
				combinedRight = 0
				for adj in leftAdj:
					combinedLeft += adj.getLength()
				if len(rightAdj) > 0:
					for adj in rightAdj:
						combinedRight += adj.getLength()
					if combinedLeft == combinedRight:
						print 'combined left and right'
						leftGroup = [adj for adj in leftAdj]
						rightGroup = [adj for adj in rightAdj]				
				for r in tempRight:
					if combinedLeft == r.getLength():
						print 'found right to match combined left'
						rightEdge = r
						leftGroup = [adj for adj in leftAdj]


			if len(rightAdj) > 0:
				print 'right conflict'
				combinedLeft = 0
				combinedRight = 0
				for adj in rightAdj:
					combinedRight += adj.getLength()
					if len(leftAdj) > 0:
						for adj in leftAdj:
							combinedLeft += adj.getLength()
						if combinedRight == combinedLeft:
							print 'combined left and right'
							leftGroup = [adj for adj in leftAdj]
							rightGroup = [adj for adj in rightAdj]
					for l in tempLeft:
						if combinedRight == l.getLength():
							print 'found left to match combined right'
							leftEdge = l
							rightGroup = [adj for adj in rightAdj]

			if len(rightAdj) == len(leftAdj) == 0:
				print 'finding fresh left and rights'
				print 'Possibile lefts:', str(len(tempLeft))
				for edge in tempLeft:
					print str(edge.getPoint1()), str(edge.getPoint2()), str(edge.getLength())
				for edge in tempLeft:
					leftGroup = []
					leftEdge = edge
					#print 'Left edge: ', str(leftEdge.getPoint1()), str(leftEdge.getPoint2())
					leftGroup.append(leftEdge)
					tempLeft = [e for e in tempLeft if not (e.getParent() == leftEdge.getParent() and (e.getX1() < leftEdge.getX1() or e.getX2() > leftEdge.getX2()))]
					tempRight = [e for e in tempRight if not (e.getParent() == leftEdge.getParent() and (e.getX1() < leftEdge.getX1() or e.getX2() > leftEdge.getX2()))]
					tempBottom = [e for e in tempBottom if not (e.getParent() == leftEdge.getParent() and (e.getX1() < leftEdge.getX1() or e.getX2() > leftEdge.getX2()))]
					tempTop = [e for e in tempTop if not (e.getParent() == leftEdge.getParent() and (e.getX1() < leftEdge.getX1() or e.getX2() > leftEdge.getX2()))]

					for edge in tempRight:
						rightGroup = []
						if edge.getLength() == leftEdge.getLength():

							rightEdge = edge
							rightGroup.append(rightEdge)
			# print 'Left groups: ', str(len(leftGroup))
			# print 'Right groups: ', str(len(rightGroup))
			# print 'Left adj: ', str(len(leftAdj))
			# print 'Right adj: ', str(len(rightAdj))

		print '---Shape---'
		for edge in leftGroup:
			print 'Left edge:', str(edge.getPoint1()), str(edge.getPoint2())
		for edge in rightGroup:
			print 'Right edge:', str(edge.getPoint1()), str(edge.getPoint2())

		print 'Top edge:', str(topEdge.getPoint1()), str(topEdge.getPoint2())
		print 'Bottom edge:', str(bottomEdge.getPoint1()), str(bottomEdge.getPoint2())


					

