import pygame
import sys
import random


class Lifegame:
    def __init__(self, screen_width=800, screen_height=600, cell_size=10, alive_color=(0, 255, 255),
        dead_color=(0, 0, 0), max_fps=10):
        """
        Initialize grid, set default game state, initialize game screen
        :param screen_width: Game Window width
        :param screen_height: Game Window height
        :param cell_size: Diameter of circles
        :param alive_color: RGB tuple e.g (255, 255, 255) for cells
        :param dead_color: RGB tuple e.g (255, 255, 255)
        :param max_fps: frame rate cap for limit game speed
        """

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.alive_color = alive_color
        self.dead_color = dead_color

        pygame.init()
        self.desired_mili_seconds_between_updates = (1.0 / max_fps) * 1000.0
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Game of Life")
        self.last_update_completed = 0 # for frame rate stuff
        self.active_grid = 0 
        self.grids = []
        self.num_cols = self.screen_width // self.cell_size
        self.num_rows = self.screen_height // self.cell_size
        self.paused = False
        self.gameover = False

        self.init_grids()
        self.clear_screen()
        pygame.display.update() #or pygame.display.flip()
        self.set_grid()


    def init_grids(self):
        """
        Create and stores the default active and inactive grid
        :return: None
        """
        def create_grid():
            """
            generate an empty 2 grid
            :return:
            """
            rows = []
            for row_num in range(self.num_rows):
                list_of_columns = [0] * self.num_cols
                rows.append(list_of_columns)
            return rows
        
        grid1 = create_grid() # for active grid
        grid2 = create_grid() # for deactive grid
        self.grids.append(grid1) 
        self.grids.append(grid2) 

        
    def set_grid(self, value=None, grid=0):
        """
        Set an entire grid at once. set to a single value or random 0/1.
        Examples:
            set_grid(0) # all dead
            set_grid(1) # all alive
            set_grid() # random
            set_grid(None) # random
        :param value: Index of grid , for active/inactive  (0 or 1)
        :param grid: Value to set the cell to (0 or 1)
        :return:
        """
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if value is None:
                    cell_value = random.randint(0, 1)
                else:
                    cell_value = value
                self.grids[grid][r][c] = cell_value


    def draw_grid(self):
        """
        Given the grid and cell states, draw the cells on the screen
        :return:
        """
        self.clear_screen()
        for c in range(self.num_cols):
            for r in range(self.num_rows):
                if self.grids[self.active_grid][r][c] == 1:
                    color = self.alive_color
                else:
                    color = self.dead_color
                pygame.draw.circle(self.screen, color, (c * self.cell_size + (self.cell_size//2), 
                                                r * self.cell_size + (self.cell_size // 2)), self.cell_size // 2, 0)
        pygame.display.update()  # or pygame.display.flip() but they have diffrence .update() can be faster
        
        
    
    def clear_screen(self):
        """
        fil whole screen with dead color
        :return:
        """
        self.screen.fill(self.dead_color)
    

    def get_cell(self, r, c):
        """
        Get the alive/dead (0/1) state of specific cell in active grid
        :param r:
        :param c:
        :return: 0 or 1 depending on state of cell. Defaults to 0 (dead)
        """
        try:
            cell_value = self.grids[self.active_grid][r][c]
        except:
            cell_value = 0
        return cell_value

    
    def check_cell_neighbors(self, row_index, col_index):
        """
        Get the number of alive neighbor cell, and determine the state of the cell
        for next generation. Determine whether it lives, dies, survives, or is born.
        :param: row_index: Row number of cell to check
        :param: col_index: Column number of cell to check
        :return: The state the cell shoud be in next generation (0 or 1)
        """
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

        # Rules for life and death
        if self.grids[self.active_grid][row_index][col_index] == 1: # alive
            if num_alive_neighbors > 3: # Overpopulation
                return 0
            if num_alive_neighbors < 2:  #Underpopulation
                return 0
            if num_alive_neighbors == 2 or num_alive_neighbors == 3:
                return 1
        elif self.grids[self.active_grid][row_index][col_index] == 0: # dead
            if num_alive_neighbors == 3:
                return 1 #come to life  
      
        return self.grids[self.active_grid][row_index][col_index]
    
    
    
    def update_generation(self):
        """
        Inspect current generation state, prepare nexr generation 
        :return: 
        """
        self.set_grid(0, self.inactive_grid())
        for r in range(self.num_rows  - 1):
            for c in range(self.num_cols - 1):
                next_gen_state = self.check_cell_neighbors(r, c)
                self.grids[self.inactive_grid()][r][c] = next_gen_state
        self.active_grid = self.inactive_grid()

    def inactive_grid(self):
        """
        Simple helper function to get the index of the inactive grid
        if active grid is 0 wil return 1 and vice-versa
        :return:
        """
        return (self.active_grid + 1) % 2



    def handle_events(self):
        """
        Handle by keypresses
        s - start/stop (pause) the game
        q - quit
        r - randomize grid
        :return:
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # stop and start game
                if event.unicode == 's':
                    print("Toggling pause")
                    if self.paused:
                        self.paused = False
                    else:
                        self.paused = True
                elif event.unicode == 'r':
                    print("Randomizing grid")
                    self.active_grid = 0
                    self.set_grid(None, self.active_grid) # randomize
                    self.set_grid(0, self.inactive_grid()) # set to 0
                    self.draw_grid()
                elif event.unicode == 'q':
                    print("Exiting")
                    self.gameover = True
        # if event is keypress of "s" then toggle game pause
        # if event is keypress of "r" then randomize grid
        # if event is keypress of "q" then quit  
            if event.type == pygame.QUIT:
                sys.exit()
    

    def cap_frame_rate(self):
        """
        If game is running too fast and updating frames too frequently,
        just wait to maintain stable framerate
        :return:
        """
        now = pygame.time.get_ticks()
        mili_seconds_since_last_update = now - self.last_update_completed
        time_to_sleep = self.desired_mili_seconds_between_updates - mili_seconds_since_last_update
        if time_to_sleep > 0:
            pygame.time.delay(int(time_to_sleep))
        self.last_update_completed = now
    
    
    def run(self):
        """
        Kick off the game and loop forever until quit state
        :return:
        """
        while True:
            if self.gameover:
                return
            self.handle_events()
            if self.paused:
                continue
            self.update_generation()
            self.draw_grid()
            self.cap_frame_rate()



if __name__ == "__main__":
    game = Lifegame()
    game.run()
    
