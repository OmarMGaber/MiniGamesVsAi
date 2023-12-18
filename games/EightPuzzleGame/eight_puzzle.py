import copy
import random
from games.MiniGame import MiniGame
from heapq import heappush, heappop

# initial = [[2, 8, 3],
#            [1, 6, 4],
#            [7, 0, 5]]
initial = [[1, 2, 3],
           [4, 0, 5],
           [6, 7, 8]]

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

# 3 -> 8 Tiles, 4 -> 15 Tiles and so on..
game_size = 3

# 4 possible directions -> up, left, down, right
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]

empty_tile_pos = [1, 1]


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, k):
        heappush(self.heap, k)

    def pop(self):
        return heappop(self.heap)

    def empty(self):
        return not self.heap


class Node:
    def __init__(self, parent, matrix, new_empty_tile_pos, heuristic, level):
        self.parent = parent
        self.matrix = matrix
        self.empty_tile_pos = new_empty_tile_pos
        self.heuristic = heuristic
        self.previous_choice = ""
        self.level = level

    # This method is defined so that the priority queue is formed based on the fn(x) short for less than
    def __lt__(self, nxt):
        return (self.heuristic + self.level) < (nxt.heuristic + nxt.level)


class EightPuzzle(MiniGame):
    def __init__(self, title):
        super().__init__(title)

    def getTitle(self):
        return self.title

    @staticmethod
    def printMatrix(matrix):
        for i in range(game_size):
            for j in range(game_size):
                print("%d " % (matrix[i][j]), end=" ")
            print()

    @staticmethod
    # heuristic function
    def h(matrix) -> int:
        count = 0
        for i in range(game_size):
            for j in range(game_size):
                if (matrix[i][j]) and (matrix[i][j] != goal[i][j]):
                    count += 1
        return count

    @staticmethod
    def newNode(matrix, min_empty_tile_pos, new_empty_tile_pos, level, parent) -> Node:
        # Copy data from parent matrix to current matrix
        new_matrix = copy.deepcopy(matrix)

        # Move tile by 1 position
        x1, y1 = min_empty_tile_pos[0], min_empty_tile_pos[1]
        x2, y2 = new_empty_tile_pos[0], new_empty_tile_pos[1]
        new_matrix[x1][y1], new_matrix[x2][y2] = new_matrix[x2][y2], new_matrix[x1][y1]

        # Set number of misplaced tiles
        heuristic = EightPuzzle.h(new_matrix)

        return Node(parent, new_matrix, new_empty_tile_pos, heuristic, level)

    @staticmethod
    # Function to check if (x, y) is a valid move
    def safeMove(x, y):
        return 0 <= x < game_size and 0 <= y < game_size

    @staticmethod
    def updateEmptyTilePos(numbers):
        global empty_tile_pos
        for i in range(game_size):
            for j in range(game_size):
                if numbers[i][j] == 0:
                    empty_tile_pos = [i, j]
                    return

    @staticmethod
    def generate_random_puzzle():
        numbers = list(range(game_size * game_size))
        random.shuffle(numbers)
        matrix = [numbers[i:i + game_size] for i in range(0, (game_size * game_size), game_size)]
        EightPuzzle.updateEmptyTilePos(matrix)
        return matrix

    @staticmethod
    def printPath(root):
        if root is None:
            return
        EightPuzzle.printPath(root.parent)
        EightPuzzle.printMatrix(root.matrix)
        print()

    @staticmethod
    def count_inversions(board):
        flat_board = [val for Row in board for val in Row if val != 0]
        inversions = sum(1 for i in range(len(flat_board)) for j in range(i + 1, len(flat_board)) if flat_board[i] > flat_board[j])
        return inversions

    @staticmethod
    def notSolvable(initial_state):
        return EightPuzzle.count_inversions(initial_state) & 1

    @staticmethod
    def greedy():
        if EightPuzzle.notSolvable(initial):
            print("\nThis Puzzle Not Solvable!")
            return

        pq = PriorityQueue()

        # Create the root Node
        heuristic = EightPuzzle.h(initial)
        root = Node(None, initial, empty_tile_pos, heuristic, 0)

        pq.push(root)

        while not pq.empty():
            minimum = pq.pop()

            # If minimum is the answer Node
            if minimum.heuristic == 0:
                EightPuzzle.printPath(minimum)
                return

            # Generate all possible children
            for i in range(4):
                new_tile_pos = [minimum.empty_tile_pos[0] + row[i], minimum.empty_tile_pos[1] + col[i]]

                if EightPuzzle.safeMove(new_tile_pos[0], new_tile_pos[1]):
                    # Create a child Node
                    child = EightPuzzle.newNode(minimum.matrix, minimum.empty_tile_pos, new_tile_pos, minimum.level + 1, minimum)

                    # Add child to list of live nodes
                    pq.push(child)

    @staticmethod
    def Astar():
        if EightPuzzle.notSolvable(initial):
            print("\nThis Puzzle Not Solvable!")
            return

        pq = PriorityQueue()

        # Create the root Node
        heuristic = EightPuzzle.h(initial)
        root = Node(None, initial, empty_tile_pos, heuristic, 0)

        pq.push(root)

        while not pq.empty():
            minimum = pq.pop()

            # If minimum is the answer Node
            if minimum.heuristic == 0:
                EightPuzzle.printPath(minimum)
                print("Reached Goal State")
                return

            # Generate all possible children
            for i in range(4):
                new_tile_pos = [minimum.empty_tile_pos[0] + row[i], minimum.empty_tile_pos[1] + col[i]]

                if EightPuzzle.safeMove(new_tile_pos[0], new_tile_pos[1]):
                    child = EightPuzzle.newNode(minimum.matrix, minimum.empty_tile_pos, new_tile_pos, minimum.level + 1,
                                                minimum)
                    pq.push(child)

    @staticmethod
    def availableMoves():
        available_moves = []
        x1, y1 = empty_tile_pos[0] + row[0], empty_tile_pos[1] + col[0]
        x2, y2 = empty_tile_pos[0] + row[1], empty_tile_pos[1] + col[1]
        x3, y3 = empty_tile_pos[0] + row[2], empty_tile_pos[1] + col[2]
        x4, y4 = empty_tile_pos[0] + row[3], empty_tile_pos[1] + col[3]
        if EightPuzzle.safeMove(x1, y1):
            available_moves.append([x1, y1])
        if EightPuzzle.safeMove(x2, y2):
            available_moves.append([x2, y2])
        if EightPuzzle.safeMove(x3, y3):
            available_moves.append([x3, y3])
        if EightPuzzle.safeMove(x4, y4):
            available_moves.append([x4, y4])
        return available_moves

    @staticmethod
    def find_element_2d(lst, value):
        for i, Row in enumerate(lst):
            for j, element in enumerate(Row):
                if element == value:
                    return [i, j]
        return None

    @staticmethod
    def userPart():
        global initial, empty_tile_pos
        initial = EightPuzzle.generate_random_puzzle()
        while True:
            EightPuzzle.printMatrix(initial)
            moves = EightPuzzle.availableMoves()
            print("Which Tile You want to move, Enter a number between ", end=" ")
            moves.sort()
            available_moves = []
            for i in moves:
                print(initial[i[0]][i[1]], end=", ")
                available_moves.append(initial[i[0]][i[1]])
            print()
            number = input()
            if int(number) in available_moves:
                k = EightPuzzle.find_element_2d(initial, int(number))
                initial[empty_tile_pos[0]][empty_tile_pos[1]] = initial[k[0]][k[1]]
                initial[k[0]][k[1]] = 0
                empty_tile_pos = [k[0], k[1]]
                if initial == goal:
                    print("You Reached Goal State!")
                    return
            else:
                print("You Should Enter on of the given Tiles!")

    def startGame(self):
        print("Welcome to 8 Puzzle!")
        print("1- user\n2- AI")
        S = input("Which one you want to play the game?: ")
        if S == "1":
            EightPuzzle.userPart()
        elif S == "2":
            print("1- Greedy\n2- A*")
            A = input("Enter Which Algorithm you want to apply?: ")
            if A == 1:
                EightPuzzle.greedy()
            elif A == 2:
                EightPuzzle.Astar()
            else:
                print("Error in input!!")
        else:
            print("Error in input!!")