import pygame
import sys
import random

dead_color = 0, 0, 0
alive_color = 0, 255, 255
board_size = width, height = 640, 480
cell_size = 10

class Lifegame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(board_size)
        pygame.display.set_caption("Game of Life") 
        self.init_grids()
        self.clear_screen()
        pygame.display.update() #or pygame.display.flip()

    def init_grids(self):
        self.num_cols = width // cell_size
        self.num_rows = height // cell_size
        print("Columns: %d\nRows: %d" %(self.num_cols, self.num_rows))

        self.grids = []

        for row in range(self.num_rows):
            self.grids.append([0] * self.num_cols)
        

        self.active_grid = 0
        self.set_grid()
    # set_grid(0) # all alive
    # set_grid(1) # all dead
    # set_grid(None) # random
    # set_grid() # random
    def set_grid(self, value=None):
        # for col in range(self.num_cols):
        #     for row in range(self.num_rows):
        #         if value is None:
        #             cell_value = random.randint(0, 1)
        #         else:
        #             cell_value = value
        #         self.grids[self.active_grid][col][row] = cell_value
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grids[row][col] = random.randint(0, 1)
                 


    def draw_grid(self):
        self.clear_screen()
        # for col in range(self.num_cols):
        #     for row in range(self.num_rows):
        #         if self.grids[self.active_grid][col][row] == 1:
        #             color = alive_color
        #         else:
        #             color = dead_color
        #         pygame.draw.circle(self.screen, color, (col * cell_size + (cell_size//2), 
        #                                         row *cell_size + (cell_size // 2)), cell_size // 2, 0)
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.grids[row][col] == 1:
                    color = alive_color
                else:
                    color = dead_color
                pygame.draw.circle(self.screen, color, (col * cell_size +(cell_size//2),
                                 row * cell_size + (cell_size//2)), cell_size//2, 0)
        
        
        pygame.display.update()  # or pygame.display.flip() but they have diffrence .update() can be faster
        
        
    
    def clear_screen(self):
        self.screen.fill(dead_color)
    
   
    def update_generation(self):
        # Inspect the current active generation
        # update the inactive grid to store next generation
        # swap out the active grid
        self.set_grid(None)

            
    def handle_events(self):
        for event in pygame.event.get():
        # if event is keypress of "s" then toggle game pause
        # if event is keypress of "r" then randomize grid
        # if event is keypress of "q" then quit  
            if event.type == pygame.QUIT:
                sys.exit()

    def run(self):
        while True:
            self.handle_events()
            # time checking?
            self.update_generation()
            self.draw_grid()
            pygame.time.delay(300)

if __name__ == "__main__":
    game = Lifegame()
    game.run()
    