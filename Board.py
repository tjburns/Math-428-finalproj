import random

# Defines board that visualization is created on.
# Board is a 2d array of Coordinates - our "city"
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        for i in range(self.width):
            self.board.append([])
            for j in range(self.height):
                self.board[i].append([])
                self.board[i][j].append(-1)

    def getCoord(self, x, y):
        if 0 <= x <= self.width and 0 <= y <= self.height:
            return -1
        else:
            return self.board[x][y]

    """
    def getNeighbors(self, coord):
        x = coord.x
        y = coord.y
        neighbors = [Coordinate(x+1, y), Coordinate(x, y-1), Coordinate(x-1, y), Coordinate(x, y+1)]
        if (x+y)%2 == 0:
            neighbors.reverse()
        neighbors = filter(lambda inGrid: 0 <= inGrid.x < self.width and 0 <= inGrid.y < self.height, neighbors)
        return neighbors
    """

# Defines a coordinate for each person within the population.
class Person:
    
    # run stats - shared by all people
    num_infected = 0
    num_recovered = 0
    num_dead = 0

    def __init__(self, x, y, infection_rate, incubation_period, is_infected, duration, immunity_rate, medicated, quarantined, color):
        self.x = x
        self.y = y
        self.infection_rate = infection_rate
        self.incubation_period = incubation_period
        self.is_infected = is_infected
        self.duration = duration
        self.immunity_rate = immunity_rate
        self.medicated = medicated
        self.quarantined = quarantined
        self.color = color

    def infect(self, incubation_period, duration):
        self.is_infected = True
        self.incubation_period = incubation_period
        self.duration = duration
        self.color = "red"

        self.num_infected += 1

    def recover(self, immunity_rate):
        self.is_infected = False
        self.incubation_period = 0
        self.duration = 0
        self.immunity_rate = immunity_rate
        self.color = "blue"

        self.num_recovered += 1
    
    def die(self):
        self.is_infected = False
        self.duration = 0
        self.immunity_rate = 1
        self.color = "black"

        self.num_dead += 1

    def quarantine(self):
        self.quarantined = True
        self.color = "magenta"

    def medicate(self, medication_effectiveness, immunity_rate):
        if random.random() < medication_effectiveness:
            self.recover(immunity_rate)
        else:
            # person was medicated and it did not work
            self.medicated = True

    def process(self, fatality_rate, immunity_rate):
        if self.is_infected:
            if self.incubation_period > 0:
                self.incubation_period = self.incubation_period - 1
            else:
                if self.duration > 0:
                    self.duration = self.duration - 1
                else:
                    if random.random() > fatality_rate:
                        self.recover(immunity_rate)
                    else:
                        self.die()
    
    def getNeighbors(self, population, x, y, row, col):
        row = row - 1
        col = col -1
        # CORNER CASES first
        # top right
        if x+1 > row and y+1 > col:
            neighbors = [population[x-1][y], population[x][y-1],
                        population[x-1][y-1]]
        # bottom right
        elif x+1 > row and y-1 < 0:
            neighbors = [population[x-1][y], population[x][y+1],
                        population[x-1][y+1]]
        # top left
        elif x-1 < 0 and y+1 > col:
            neighbors = [population[x+1][y], population[x][y-1],
                        population[x+1][y-1]]
        # bottom left
        elif x-1 < 0 and y-1 < 0:
            neighbors = [population[x][y+1], population[x+1][y],
                        population[x+1][y+1]]
        # SIDE CASES
        # top
        elif y+1 > col:
            neighbors = [population[x-1][y], population[x+1][y], population[x][y-1],
                        population[x-1][y-1], population[x+1][y-1]]
        # right 
        elif x+1 > row:
            neighbors = [population[x][y-1], population[x][y+1], population[x-1][y],
                        population[x-1][y-1], population[x-1][y+1]]
        # left 
        elif x-1 < 0:
            neighbors = [population[x][y-1], population[x][y+1], population[x+1][y],
                        population[x+1][y-1], population[x+1][y+1]]
        # bottom
        elif y-1 < 0:
            neighbors = [population[x-1][y], population[x+1][y], population[x][y+1],
                        population[x-1][y+1], population[x+1][y+1]]
        else:
            neighbors = [population[x+1][y], population[x][y-1], population[x-1][y], population[x][y+1],
                        population[x-1][y-1], population[x+1][y+1], population[x-1][y+1], population[x+1][y-1]]
        
        return neighbors

    # case where diagonal neighbors are not considered as infection vectors
    def get4Neighbors(self, population, x, y, row, col):
        # corner cases first
        # top right
        if x+1 > row and y+1 > col:
            neighbors = [population[x-1][y], population[x][y-1]]
        # bottom right
        elif x+1 > row and y-1 < col:
            neighbors = [population[x-1][y], population[x][y+1]]
        # top left
        elif x-1 < row and y+1 > col:
            neighbors = [population[x+1][y], population[x][y-1]]
        # bottom left
        elif x-1 < row and y-1 < row:
            neighbors = [population[x][y+1], population[x+1][y]]
        # not a corner
        else:
            neighbors = [population[x+1][y], population[x][y-1], population[x-1][y], population[x][y+1]]
        
        return neighbors