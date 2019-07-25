import pygame
import sys
import random
import datetime
import time

dead_color = 0, 0, 0
alive_color = 0, 255, 255
board_size = width, height = 640, 480
cell_size = 10
MAX_FPS = 2


class Lifegame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(board_size)
        pygame.display.set_caption("Game of Life") 
        self.init_grids()
        self.clear_screen()
        pygame.display.update() #or pygame.display.flip()
        self.last_update_completed = 0 # for frame rate stuff 


    def init_grids(self):
        self.num_cols = width // cell_size
        self.num_rows = height // cell_size
        print("Columns: %d\nRows: %d" %(self.num_cols, self.num_rows))
        # self.grids = [
        #         [[0] * self.num_rows] * self.num_cols, 
        #         [[0] * self.num_rows] * self.num_cols]
        self.grids = []
        rows = []
        for row_num in range(self.num_rows):
            list_of_columns = [0] * self.num_cols
            rows.append(list_of_columns)

        self.grids.append(rows)

        self.active_grid = 0
        self.set_grid()
        # print(self.grids[0])
    # set_grid(0) # all alive
    # set_grid(1) # all dead
    # set_grid(None) # random
    # set_grid() # random
    def set_grid(self, value=None):
        # for r in range(self.num_rows):
        #     for c in range(self.num_cols):
        #         if value is None:
        #             cell_value = random.randint(0, 1)
        #         else:
        #             cell_value = value
        #         self.grids[self.active_grid][col][row] = cell_value
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self.grids[self.active_grid][r][c] = random.randint(0, 1)


    def draw_grid(self):
        self.clear_screen()
        for c in range(self.num_cols):
            for r in range(self.num_rows):
                if self.grids[self.active_grid][r][c] == 1:
                    color = alive_color
                else:
                    color = dead_color
                pygame.draw.circle(self.screen, color, (c * cell_size + (cell_size//2), 
                                                r *cell_size + (cell_size // 2)), cell_size // 2, 0)
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
            desired_mili_seconds_between_updates = (1.0 / MAX_FPS) * 1000.0
            self.handle_events()
            self.update_generation()
            self.draw_grid()
            # =========================
            # cap framerate at 60fps
            # if time since the last frame draw < 1/60th of a second, sleep for remaining time
            now = pygame.time.get_ticks()
            mili_seconds_since_last_update = now - self.last_update_completed
            time_to_sleep = desired_mili_seconds_between_updates - mili_seconds_since_last_update
            if time_to_sleep > 0:
                pygame.time.delay(int(time_to_sleep))
            self.last_update_completed = now
            # self.last_update_completed = now
            # now = datetime.datetime.now().microsecond
            # time_since_last_update = now - self.last_update_completed
            # print(time_since_last_update)
            # if (time_since_last_update < micro_seconds_between_update):
            #     time.sleep((1 / 1000000) * (micro_seconds_between_update - time_since_last_update))
            # self.last_update_completed = now
            
            


if __name__ == "__main__":
    game = Lifegame()
    game.run()
    