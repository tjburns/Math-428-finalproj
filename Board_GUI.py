import pygame

# This is modified matrix to graphic code sourced from http://programarcadegames.com/python_examples/f.php?file=array_backed_grid.py

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 8
HEIGHT = 8

# This sets the margin between each cell
MARGIN = 1

def board_gui(board, cells):
    
    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    rowT = len(board)
    columnT = len(board[0])
    WINDOW_SIZE = [(WIDTH+MARGIN)*rowT+1, (HEIGHT+MARGIN)*columnT+1]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    
    # Set title of screen
    pygame.display.set_caption("Epidemic Visualization")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():    # User did something
            if event.type == pygame.QUIT:   # If user clicked close
                done = True     # Flag that we are done so we exit this loop

        # Set the screen background
        screen.fill(BLACK)

        for row in range(rowT):
            for col in range(columnT):
                color = WHITE
                if cells[row][col].color == "green": # alive
                    color = GREEN
                if cells[row][col].color == "red": # infected
                    color = RED
                if cells[row][col].color == "black": # dead
                    color = BLACK
                if cells[row][col].color == "blue": # recovered
                    color = BLUE
                if cells[row][col].color == "magenta": # tbd
                    color = MAGENTA
                if cells[row][col].color == "yellow": # adaptive path
                    color = YELLOW
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * col + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])


        # Limit to 60 frames per second
        clock.tick(60)
    
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()