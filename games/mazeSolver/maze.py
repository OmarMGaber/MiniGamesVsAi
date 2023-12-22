import random

from pyamaze import maze, agent, textLabel, COLOR

from games.miniGame import MiniGame


class Maze(MiniGame):
    MAZE_LINES = ['h', 'v', None]

    def __init__(self, title, mazeSize=(20,20), algorithmType="Default"):
        super().__init__(title)

        self.mazeSize = mazeSize
        self.algorithmType = algorithmType

        self.cellsLabel = None
        self.destination = None
        self.startPoint = None
        self.testMaze = None
        self.AlgorithmLabel = None
        self.testAgent = None

    def getTitle(self):
        return self.title

    def getMazeMap(self):
        return self.testMaze.maze_map

    def roadToGoal(self):
        return self.testMaze.path

    def __traceGoal(self, agent, path, maze):
        maze.tracePath({agent: path}, delay=100)

    def validatePath(self, start, goal):
        while start == goal:
            start = (random.randint(1, self.testMaze.rows), random.randint(1, self.testMaze.cols))
            goal = (random.randint(1, self.testMaze.rows), random.randint(1, self.testMaze.cols))
        return start, goal

    def startGame(self):
        Maze(self.getTitle())
        self.testMaze = maze(self.mazeSize[0], self.mazeSize[1])

        self.startPoint, self.destination = self.validatePath(
            (
                random.randint(1, self.testMaze.rows),
                random.randint(1, self.testMaze.cols)
            ),

            (
                random.randint(1, self.testMaze.rows),
                random.randint(1, self.testMaze.cols)
            )
        )

        self.testMaze.CreateMaze(self.destination[0], self.destination[1], pattern=random.choice(Maze.MAZE_LINES))
        self.testAgent = agent(self.testMaze, self.startPoint[0], self.startPoint[1], shape='square',
                               color=COLOR.red,
                               goal=self.destination, footprints=True, filled=True)

        self.cellsLabel = textLabel(self.testMaze, 'Total Cells', self.testMaze.rows * self.testMaze.cols)
        self.AlgorithmLabel = textLabel(self.testMaze, 'Algorithm used', self.algorithmType)

        self.__traceGoal(self.testAgent, self.testMaze.path, self.testMaze)
        self.testMaze.run()


if "__main__" == __name__:
    sampleMaze = Maze("Maze Solver")
