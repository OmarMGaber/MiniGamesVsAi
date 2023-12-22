import random

from pyamaze import maze, agent, textLabel, COLOR

from games.miniGame import MiniGame


class Maze(MiniGame):
    MAZE_LINES = ['h', 'v', None]
    SEARCH_ALGORITHMS = {1: "DFS", 2: "A*", 3: "BFS"}
    DIRECTIONS = "ESNW"

    def __init__(self, title, mazeSize=(50, 50), algorithmType=SEARCH_ALGORITHMS[1]):
        super().__init__(title)

        self.testMaze = maze(mazeSize[0], mazeSize[1])
        self.mazeMap = self.testMaze.maze_map
        self.mazeSize = mazeSize
        self.mazeCols = mazeSize[1]
        self.mazeRows = mazeSize[0]

        self.randomStart = (random.randint(1, self.mazeRows), random.randint(1, self.mazeCols))
        self.randomEnd = (random.randint(1, self.mazeRows), random.randint(1, self.mazeCols))

        self.algorithmType = algorithmType

        self.testMaze = None
        self.testAgent = None

        self.AlgorithmLabel = None
        self.cellsLabel = None

        self.startPoint = None
        self.destination = None

    def getTitle(self):
        return self.title

    def addAlgorithm(self, algorithmName):
        Maze.SEARCH_ALGORITHMS[len(Maze.SEARCH_ALGORITHMS)+1] = algorithmName

    def __getMazeMap(self):
        return self.testMaze.maze_map

    def roadToGoal(self):
        return self.testMaze.path

    def __validatePath(self, start, goal):
        while start == goal:
            start = (random.randint(1, self.testMaze.rows), random.randint(1, self.testMaze.cols))
            goal = (random.randint(1, self.testMaze.rows), random.randint(1, self.testMaze.cols))
        return start, goal

    def __applyLabels(self , *args):
        self.cellsLabel = textLabel(self.testMaze, f'{args[0]}', self.testMaze.rows * self.testMaze.cols)
        self.pathLengthLabel = textLabel(self.testMaze , f'{args[1]}' , args[2])
        self.AlgorithmLabel = textLabel(self.testMaze, f'{args[3]}', self.algorithmType)

    def __findNextDirection(self, point, openedDirection):
        nextDirection = None

        if openedDirection == Maze.DIRECTIONS[0]:
            nextDirection = (point[0], point[1] + 1)

        elif openedDirection == Maze.DIRECTIONS[1]:
            nextDirection = (point[0] + 1, point[1])

        elif openedDirection == Maze.DIRECTIONS[2]:
            nextDirection = (point[0] - 1, point[1])

        else:
            nextDirection = (point[0], point[1] - 1)

        return nextDirection

    def __formDictWith(self, value, pointsMap, exceptPoint, exceptValue):
        for row in range(1, self.mazeRows + 1):
            for col in range(1, self.mazeCols + 1):
                pointsMap[(row, col)] = value
        pointsMap[exceptPoint] = exceptValue
        return pointsMap

    def update_Maze_Map(self, newMazeMap):
        self.mazeMap = newMazeMap

    def __DFS(self, startPoint, goalPoint):

        mostWestPoints = [startPoint]
        exploredPoints = dict()
        pathToGoalPoint = dict()
        dfsPath = dict()
        exploredPoints = self.__formDictWith(False, exploredPoints, exceptPoint=startPoint, exceptValue=1)

        while mostWestPoints :
            currentPoint = mostWestPoints.pop()

            if currentPoint == goalPoint:
                break

            for direction in Maze.DIRECTIONS:
                if self.__getMazeMap()[currentPoint][direction]:
                    child = self.__findNextDirection(currentPoint, direction)

                    if exploredPoints[child]:
                        continue
                    exploredPoints[child] = 1
                    mostWestPoints.append(child)
                    dfsPath[child] = currentPoint

        current = goalPoint
        while current != startPoint:
            pathToGoalPoint[dfsPath[current]] = current
            current = dfsPath[current]
        return pathToGoalPoint , len(pathToGoalPoint)

    def __traceGoal(self, agent, path, maze):
        maze.tracePath({agent: path}, delay=50)

    def startGame(self):

        self.testMaze = maze(self.mazeRows, self.mazeCols)

        self.startPoint, self.destination = self.__validatePath(
            (
                self.randomStart
            ),

            (
                self.randomEnd
            )
        )

        self.testMaze.CreateMaze(self.destination[0], self.destination[1], pattern=random.choice(Maze.MAZE_LINES))
        self.testAgent = agent(self.testMaze, self.startPoint[0], self.startPoint[1], shape='square',
                               color=COLOR.red,
                               goal=self.destination, footprints=True, filled=True)

        self.update_Maze_Map(self.testMaze.maze_map)

        pathFromPointToPoint , totalPathLength = self.__DFS(startPoint=self.startPoint, goalPoint=self.destination)

        self.__applyLabels("Total Cells","Path Length" , totalPathLength, "Algorithm Used")

        self.__traceGoal(self.testAgent, pathFromPointToPoint, self.testMaze)
        self.testMaze.run()


if "__main__" == __name__:
    sampleMaze = Maze("Maze Solver", (15, 15), "DFS")
    sampleMaze.startGame()
