import pygame
import sys

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
        num_cols = width // cell_size
        num_rows = height // cell_size
        self.grids = (
                [[0] * num_rows] * num_cols, 
                [[0] * num_rows] * num_cols
                )
        self.active_grid = 0

        self.game_grid_active = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.game_grid_inactive = []
   
    def draw_grid(self):
        # circle = pygame.draw.circle(self.screen, alive_color, (50, 50), 5, 0)
        pygame.display.update()  # or pygame.display.flip() but they have diffrence .update() can be faster
        
        
    
    def clear_screen(self):
        self.screen.fill(dead_color)
    
   
    def update_generation(self):
        # Inspect the current active generation
        # update the inactive grid to store next generation
        # swap out the active grid
        pass

            
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


if __name__ == "__main__":
    game = Lifegame()
    game.run()