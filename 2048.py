"""
Clone of 2048 game.
"""

#import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
FOUR_THRESHOLD = 0.10

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    
    mod_line = []
    mod_number = 0
        
    for dummy_i in range(0, len(line)):
        mod_line.append(0)
        if line[dummy_i] <> 0:
            mod_line[mod_number] = line[dummy_i]
            mod_number +=1
    
    for dummy_i in range(0, len(mod_line)-1):
        if mod_line[dummy_i] == mod_line[dummy_i + 1]:
            mod_line[dummy_i] *= 2
            mod_line[dummy_i + 1] = 0
            if dummy_i + 1 < len(mod_line)-1:
                for dummy_j in range(dummy_i + 1, len(mod_line)):
                    if dummy_j == len(mod_line) - 1:
                        mod_line[dummy_j] = 0
                    else:
                        mod_line[dummy_j] = mod_line[dummy_j + 1]
            
    return mod_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    height = 0
    width = 0
    grid = []
    cells_dict = {}
    
    def __init__(self, grid_height, grid_width):
        """
        Initiates the grid height and width then resets the game
        """
        self.height = grid_height
        self.width = grid_width
        
        start_cells = []
        for dummy_i in range(0,self.width):
            start_cells.append([0,dummy_i])
        self.cells_dict[UP] = start_cells
        
        start_cells = []
        for dummy_i in range(0,self.width):
            start_cells.append([self.height-1,dummy_i])
        self.cells_dict[DOWN] = start_cells

        start_cells = []
        for dummy_i in range(0,self.height):
            start_cells.append([dummy_i,0])
        self.cells_dict[LEFT] = start_cells
        
        start_cells = []
        for dummy_i in range(0,self.height):
            start_cells.append([dummy_i,self.width-1])
        self.cells_dict[RIGHT] = start_cells
        
        print self.cells_dict
        
        self.reset()
    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """

        self.grid = []
        
        for dummy_h in range(0,self.height):
            row = []
            for dummy_w in range(0,self.width):
                row.append(0)
            self.grid.append(row)
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return self.grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        cell_change = False
        
        initial_tiles = self.cells_dict[direction]
        offset_calc = OFFSETS[direction]
        
        if direction == 1 or direction == 2:
            length = self.height
        else:
            length = self.width
        
        for dummy_i in range(0, len(initial_tiles)):
            intermediate_tile = []
            start_values = []
            merged_values = []
            for dummy_j in range(0, length):
                intermediate_tile.append((initial_tiles[dummy_i][0]+dummy_j*offset_calc[0],initial_tiles[dummy_i][1]+dummy_j*offset_calc[1]))
            for dummy_j in range(0, len(intermediate_tile)):   
                start_values.append(self.get_tile(intermediate_tile[dummy_j][0],intermediate_tile[dummy_j][1]))
            merged_values = merge(start_values)
            if start_values <> merged_values:
                cell_change = True
                for dummy_j in range(0, len(intermediate_tile)):
                    self.set_tile(intermediate_tile[dummy_j][0], intermediate_tile[dummy_j][1], merged_values[dummy_j])
        
        if cell_change:
            self.new_tile()
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        zero_exist = False
        
        for dummy_col, dummy_row in enumerate(self.grid):
            if 0 in dummy_row:
                zero_exist = True
        if zero_exist:
            new_row = random.randint(0,self.height-1)
            new_col = random.randint(0,self.width-1)
            if self.get_tile(new_row,new_col) == 0:
                if random.random() < 0.10:
                    self.set_tile(new_row,new_col,4)
                else:
                    self.set_tile(new_row,new_col,2)
            else:
                self.new_tile()
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]
 
    
#poc_2048_gui.run_gui(TwentyFortyEight(5, 6))
