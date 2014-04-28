import sys,algorithm
from obj import *

#Hard coded shapes
shape1 = Shape((10,10),(15,10),(15,30),(10,30),(10,10))
shape2 = Shape((30,10),(35,10),(35,30),(30,30),(30,10))
shape3 = Shape((70,10),(75,10),(75,35),(50,35),(50,30),(70,30),(70,10))
shape4 = Shape((85,10),(110,10),(110,35),(105,35),(105,15),(85,15),(85,10))

Shapes = [shape1,shape2,shape3,shape4]

algorithm.search(Shapes)




	


# pygame.init()

# done = False
# clock = pygame.time.Clock()

# while not done:
# 	clock.tick(30)

# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			done = True




# pygame.quit()