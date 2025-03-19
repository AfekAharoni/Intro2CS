#################################################################
# FILE : game_of_life.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex8 2025
# DESCRIPTION: In this file I created the 'game of life' using numpy
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: Conway's Game Of Life - Wiki - https://shorturl.at/6AjtU
#                   Kernel (Image Processing) - Wiki - https://shorturl.at/J8fQc
# NOTES: None
#################################################################

# CONSTANTS
LIVE_CELL = 1 # represent the value of a live cell
DEAD_CELL = 0 # represent the value of a dead cell
DEATH_FROM_LONELINESS_LIMIT = 2 # represent the threshold of loneliness 
DEATH_FROM_OVERCROWDING_LIMIT = 3 # represent the threshold of overcrowding
REPRODUCTION_LIMIT = 3 # represent the threshold of reproduction

import numpy

def is_out_of_range(cell_row: int, cell_col: int, rows_in_board: int, cols_in_board: int) -> bool:
    """
    This function gets a cell location (row, col) and shape of board (rows, cols) and check whether the location is out of range of the board
    """
    if cell_row < 0 or cell_row >= rows_in_board:
        return True
    if cell_col < 0 or cell_col >= cols_in_board:
        return True
    return False

def count_live_cells(board: numpy.ndarray, cell_row: int, cell_col: int) -> int:
    """
    This function gets a board and cell location, and return the number of live cells around the cell given (maximum 8 neighbors)
    """
    rows_in_board, cols_in_board = board.shape[0], board.shape[1]
    count_live_cells_around = 0
    for row in range(cell_row - 1, cell_row + 2):
        for col in range(cell_col - 1, cell_col + 2):
            if not is_out_of_range(row, col, rows_in_board, cols_in_board):
                if row != cell_row or col != cell_col: # check only the neighbors and not the current cell
                    if board[row][col] == LIVE_CELL:
                        count_live_cells_around += 1
    return count_live_cells_around

def game_of_life(board:numpy.ndarray, gen_num: int) -> numpy.ndarray:
    """
    This function gets a board and number of generations, and returns a new board after gen_num generations with the rules:
    • Live cell with less than 2 alive neighbor cells, will die from loneliness
    • Live cell with two or 3 alive neighbor cells, will survive
    • Live cell with more than 3 alive neighbor cells, will die from overcrowding
    • Cell with exactly 3 alive neighbor cells will become alive
    The function assumes that gen_num >= 0
    """
    if gen_num == 0:
        return board
    new_board = board.copy() # deepcopy of the board
    board_to_work_on = board.copy()
    rows_in_board, cols_in_board = board.shape[0], board.shape[1]
    while gen_num > 0:
        # for every cell in the board:
        for row in range(rows_in_board):
            for col in range(cols_in_board):
                count_of_live_cells_around = count_live_cells(board_to_work_on, row, col) # count the live cells *in the original board!*
                if board_to_work_on[row][col] == LIVE_CELL: # live cell
                    if count_of_live_cells_around < DEATH_FROM_LONELINESS_LIMIT:
                        new_board[row][col] = DEAD_CELL # dead from loneliness
                    elif count_of_live_cells_around > DEATH_FROM_OVERCROWDING_LIMIT:
                        new_board[row][col] = DEAD_CELL # dead from overcrowding
                    # if the counter not bigger than 'overcrowding' limit or lower than 'loneliness' limit, the cell will survive
                elif board_to_work_on[row][col] == DEAD_CELL: # dead cell
                    if count_of_live_cells_around == REPRODUCTION_LIMIT:
                        new_board[row][col] = LIVE_CELL # become alive 
        gen_num -= 1
        board_to_work_on = new_board.copy() # next generation has new board to work on 
    return new_board
    
def is_out_of_original_range(board: numpy.ndarray, row: int, col: int) -> bool:
    """
    This function gets a board, and a location (row and column) and returns whether the location is out of range
    """
    rows_in_board, cols_in_board = board.shape[0], board.shape[1]
    if row >= 0 and row < rows_in_board and col >= 0 and col < cols_in_board:
        return False
    return True

def create_kernel_for_cell(board: numpy.ndarray, size: int, cell_row: int, cell_col: int) -> numpy.ndarray:
    """
    This function gets board, size of kernel and cell location and creates a kernel around the cell given
    """
    kernel = []
    new_row_in_kernel = []
    size_divided = size // 2
    for row in range(-size_divided, size_divided + 1): # run all the indexes of rows in the new kernel
        for col in range(-size_divided, size_divided + 1): # run all the indexes of columns in the new kernel
            next_row_in_new_kernel = cell_row + row # the next row
            next_col_in_new_kernel = cell_col + col # the next col
            if not is_out_of_original_range(board, next_row_in_new_kernel, next_col_in_new_kernel):
                # if it's not out of range, add to the row the cell from the board
                new_row_in_kernel.append(board[next_row_in_new_kernel][next_col_in_new_kernel])
            else:
                # it's out of range, so add to the row zero
                new_row_in_kernel.append(0) # padding
        kernel.append(new_row_in_kernel)
        new_row_in_kernel = []
    return numpy.array(kernel)

def calculate_density_scale_around_cell(board: numpy.ndarray, kernel: numpy.ndarray, cell_row: int, cell_col: int) -> float:
    """
    This function gets a board, kernel, and a cell location and returns the calculation of the density scale around the cell
    """
    kernel_size = kernel.shape[0] # same as kernel.shape[1] because its square
    kernel_for_cell = create_kernel_for_cell(board, kernel_size, cell_row, cell_col) # create kernel from the original board around the cell
    sum = 0.0 # kernel values can be float
    for row in range(kernel_size):
        for col in range(kernel_size):
            sum += kernel[row][col] * kernel_for_cell[row][col]
    return sum

def game_of_life_kernel(board:numpy.ndarray, kernel:numpy.ndarray, gen_num: int,
     life_threshold=2, overcrowding_threshold=4) -> numpy.ndarray:
    """
    This function gets a board, a kernel, number of generations need to simulate, life threshold and overcrowding threshold
    The function returns the board after gen_num generations with the rules:
    A density value will be calculated for each cell and:
    • If density < life threshold -> live cell will become dead
    • If density > overcrowding threshold -> live cell will become dead
    • If life threshold < density <= overcrowding threshold -> dead cell will become alive
    The function assumes that the kernel is square (k X k) and k < n, and odd
    In addition, the function assumes that life threshold < overcrowding threshold
    """
    if gen_num == 0: # no generations to apply
        return board
    new_board = board.copy() # deepcopy of the board
    board_to_work_on = board.copy()
    rows_in_board, cols_in_board = board.shape[0], board.shape[1]
    while gen_num > 0:
        # for every cell in the board:
        for row in range(rows_in_board):
            for col in range(cols_in_board):
                density_scale = calculate_density_scale_around_cell(board_to_work_on, kernel, row, col) # calculate the density for every cell
                if density_scale < life_threshold:
                    if board_to_work_on[row][col] == LIVE_CELL:
                        new_board[row][col] = DEAD_CELL 
                elif density_scale > overcrowding_threshold:
                    if board_to_work_on[row][col] == LIVE_CELL:
                        new_board[row][col] = DEAD_CELL 
                elif density_scale > life_threshold and density_scale <= overcrowding_threshold:
                    if board_to_work_on[row][col] == DEAD_CELL:
                        new_board[row][col] = LIVE_CELL
                # else: the cell will be the same cell the next generation
        gen_num -= 1
        board_to_work_on = new_board.copy() # next generation has new board to work on 
    return new_board
