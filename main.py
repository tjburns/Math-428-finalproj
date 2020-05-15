from Board import Board, Person
from Board_GUI import board_gui 
import random

"""
Value on Board : State of Coordinate : Color
--------------------------------------------
1 : # dead               : BLACK
2 : # recovered          : BLUE
3 : # living             : GREEN
4 : # infected           : RED
5 : # quarantine         : MAGENTA
"""

# SIMULATION PARAMETERS
num_days = 10000
infection_rate = .15      # infection rate
incubation_period = 3  # time before cell becomes infectious
infection_duration = 4    # how long the cell remains infectious
fatality_rate = .02  # fatality rate among infected
immunity_rate = .5   # immunity rate to re-infection after recovery
medicine_intro = 0
medicine_effectiveness = 0
quarantine_intro = 0
quarantine_effectiveness = 0



city = Board(101, 101)
row = len(city.board)
col = len(city.board[0])

population = [[Person(i,j,0,0,False,0,0,False,False,"green") for j in range(col)] for i in range(row)]

# place initial infection on the board - this person will serve as the vector for all following infections
infection_epicenter = population[50][50]
infection_epicenter.infect(incubation_period,infection_duration)

board_gui(city.board, population)

# main simulation loop
for day in range(num_days):

    for i in range(row):
        for j in range(col):
            if not population[i][j].is_infected:
                continue

            population[i][j].process(fatality_rate, immunity_rate)

            # check if recovered or in incubation period
            if not population[i][j].is_infected or population[i][j].incubation_period > 0:
                continue

            # TODO medicine

            # TODO quarantine

            # infect neighbors if persons are not quarantined
            neighbors = population[i][j].getNeighbors(population, i, j, row, col)
            for person in neighbors:
                if person.is_infected:
                    continue
                    
                # check for potential immunity
                if random.random() > person.immunity_rate:
                    if random.random() < infection_rate:
                        person.infect(incubation_period, infection_duration)

            """
            population[0][0].infect(incubation_period, infection_duration)
            population[0][100].infect(incubation_period, infection_duration)
            population[100][0].infect(incubation_period, infection_duration)
            population[100][100].infect(incubation_period, infection_duration)
            """
    
    print("Day " + str(day))
    #board_gui(city.board, population)

print("Number of Infected: " + str(population[0][0].num_infected))
print("Number of Recovered: " + str(population[0][0].num_recovered))
print("Number of Dead: " + str(population[0][0].num_dead))
board_gui(city.board, population)

