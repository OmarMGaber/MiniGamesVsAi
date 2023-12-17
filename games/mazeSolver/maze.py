import random
from pyamaze import maze,agent

mazeSize = (20,20)
xGoal,yGoal = random.randint(0 , mazeSize[0]) ,random.randint(0 , mazeSize[1])
testMaze = maze(mazeSize[0],mazeSize[1])
testMaze.CreateMaze(xGoal , yGoal)

xStrat , yStart = random.randint(0,testMaze.rows) , random.randint(0 , testMaze.cols)

testAgent = agent(testMaze , xStrat , yStart , shape='arrow' ,color='red' , goal=(xGoal,yGoal))
testMaze.run()