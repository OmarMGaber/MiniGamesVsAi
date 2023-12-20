import random
from pyamaze import maze, agent , textLabel

from games.miniGame import MiniGame


class Maze(MiniGame):

    def __init__(self, title, mazeSize=(15, 20) , algorithmType="Default"):
        super().__init__(title)
        self.mazeSize = mazeSize
        self.algorithmType = algorithmType
        self.testMaze = maze(self.mazeSize[0], self.mazeSize[1])
        self.xStartPosition = random.randint(0, self.testMaze.rows)
        self.yStartPosition = random.randint(0, self.testMaze.cols)
        self.xGoalPosition = random.randint(0, self.testMaze.rows)
        self.yGoalPosition = random.randint(0, self.testMaze.cols)

    def getTitle(self):
        return self.title

    def getMazeMap(self):
        return self.testMaze.maze_map

    def roadToGoal(self):
        return self.testMaze.path

    def traceGoal(self , agent , path):
        self.testMaze.tracePath({agent : path} ,delay=120)

    def startGame(self):
        # helper = Maze(self.getTitle())

        self.testMaze.CreateMaze()
        self.testAgent = agent(self.testMaze, self.xStartPosition, self.yStartPosition, shape='square', color='red',
                               goal=(self.xGoalPosition, self.yGoalPosition), footprints=True, filled=True)
        #self.cellsLabel = textLabel(self.testMaze, 'Total Cells', self.testMaze.rows * self.testMaze.cols)
        self.AlgorithmLabel = textLabel(self.testMaze, 'Algorithm used' , self.algorithmType)
        self.traceGoal(self.testAgent , self.testMaze.path)
        self.testMaze.run()



if "__main__" == __name__:
    sampleMaze = Maze("Maze Solver")
