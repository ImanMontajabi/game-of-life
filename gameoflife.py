import pygame
import sys
import random
import datetime
import time

dead_color = 0, 0, 0
alive_color = 0, 255, 255
board_size = width, height = 640, 480
cell_size = 10
MAX_FPS = 8


class Lifegame:
    def __init__(self):
        pygame.init()
        self.desired_mili_seconds_between_updates = (1.0 / MAX_FPS) * 1000.0
        self.screen = pygame.display.set_mode(board_size)
        pygame.display.set_caption("Game of Life")
        self.last_update_completed = 0 # for frame rate stuff
        self.active_grid = 0 
        self.grids = []
        self.num_cols = width // cell_size
        self.num_rows = height // cell_size
        
        self.init_grids()
        self.clear_screen()
        pygame.display.update() #or pygame.display.flip()
        self.set_grid()


    def init_grids(self):
        def create_grid():
            rows = []
            for row_num in range(self.num_rows):
                list_of_columns = [0] * self.num_cols
                rows.append(list_of_columns)
            return rows
        
        grid1 = create_grid() # for active grid
        grid2 = create_grid() # for deactive grid
        self.grids.append(grid1) 
        self.grids.append(grid2) 

        
    # set_grid(0) # all alive
    # set_grid(1) # all dead
    # set_grid(None) # random
    # set_grid() # random
    def set_grid(self, value=None):
        """
        Examples:
        set_grid(0) # all dead
        set_grid(1) # all alive
        set_grid() # random
        set_grid(None) # random

        :param value:
        :return:
        """
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if value is None:
                    cell_value = random.randint(0, 1)
                else:
                    cell_value = value
                self.grids[self.active_grid][r][c] = cell_value


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
    

    def get_cell(self, r, c):
        cell_value = 0
        try:
            cell_value = self.grids[self.active_grid][r][c]
        except:
            cell_value = 0
        return cell_value

    
    def check_cell_neighbors(self, row_index, col_index):
        # implement 4 rules, too populated, underpopulated, death, birth
        # self.grids[self.active_grid][r][c]  #current cell
        # Get the number of alive cells surrounding current cell
        # Check all 8 neighbors, add up alive count
        num_alive_neighbors = 0
        num_alive_neighbors += self.get_cell(row_index - 1, col_index - 1)
        num_alive_neighbors += self.get_cell(row_index - 1, col_index - 1)
        num_alive_neighbors += self.get_cell(row_index - 1, col_index)
        num_alive_neighbors += self.get_cell(row_index - 1, col_index + 1)
        num_alive_neighbors += self.get_cell(row_index, col_index - 1)
        num_alive_neighbors += self.get_cell(row_index, col_index + 1)
        num_alive_neighbors += self.get_cell(row_index + 1, col_index - 1)
        num_alive_neighbors += self.get_cell(row_index + 1, col_index)
        num_alive_neighbors += self.get_cell(row_index + 1, col_index + 1)

        # Come to life
        if self.grids[self.active_grid][row_index][col_index] == 0 and num_alive_neighbors == 3:
            return 1
        if num_alive_neighbors > 4:    #Overpopulation  
            return 0
        if num_alive_neighbors < 3:  #Underpopulation
            return 0
        if (num_alive_neighbors == 3 or num_alive_neighbors == 4) and self.grids[self.active_grid][row_index][col_index] == 1:
            return 1
        else:
            return 0

    
    def update_generation(self):
        for r in range(self.num_rows  - 1):
            for c in range(self.num_cols - 1):
                next_gen_state = self.check_cell_neighbors(r, c)
                self.grids[self.inactive_grid()][r][c] = next_gen_state
        self.active_grid = self.inactive_grid()

    def inactive_grid(self):
        return (self.active_grid + 1) % 2



    def handle_events(self):
        for event in pygame.event.get():
        # if event is keypress of "s" then toggle game pause
        # if event is keypress of "r" then randomize grid
        # if event is keypress of "q" then quit  
            if event.type == pygame.QUIT:
                sys.exit()
    

    def cap_frame_rate(self):
            now = pygame.time.get_ticks()
            mili_seconds_since_last_update = now - self.last_update_completed
            time_to_sleep = self.desired_mili_seconds_between_updates - mili_seconds_since_last_update
            if time_to_sleep > 0:
                pygame.time.delay(int(time_to_sleep))
            self.last_update_completed = now
    
    
    def run(self):
        while True:
            self.handle_events()
            self.update_generation()
            self.draw_grid()
            self.cap_frame_rate()
            # =========================
           


if __name__ == "__main__":
    game = Lifegame()
    game.run()
    