import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = [ [] for row in range(len(grid))]
    
    
    
    for grid_row in range(len(grid)):
        new_element_row_probability=[]
        for grid_column in range(len(grid[0])):
            grid_element=grid[grid_row][grid_column]
            hit=(color==grid_element)
            new_element_probability=beliefs[grid_row][grid_column]*(hit*p_hit+(1-hit)*p_miss)
            #new_beliefs[grid_row][grid_column]=new_element_probability
            new_element_row_probability.append(new_element_probability)
        new_beliefs[grid_row]=new_element_row_probability    
        
       
            
    s = 0
    for row in new_beliefs:
        row_sum=sum(row);
        s=s+row_sum
    
    for grid_row in range(len(grid)):
        for grid_column in range(len(grid[0])):
            new_beliefs[grid_row][grid_column]= new_beliefs[grid_row][grid_column]/s
        
        

    #
    # TODO - implement this in part 2
    #

    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            
            new_G[i][j] = beliefs[(i+dx) % height][(j+dy) % width ]
           
    return blur(new_G, blurring)