#################################################################
# FILE : image_editor.py
# WRITER : Afek Aharoni , afek.aharoni , 214143414
# EXERCISE : intro2cs ex6 2025
# DESCRIPTION: In this file I made an image editor program
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: Python isinstance() function - https://shorturl.at/PtK4w
#                   Python string isnumeric() method - https://shorturl.at/nXfiK
# NOTES: None
#################################################################

##############################################################################
#                                   Imports                                  #
##############################################################################
from ex6_helper import *
from typing import Optional
from copy import deepcopy
from math import floor
import sys
import PIL # Used only to one exception
##############################################################################
#                                  CONSTANTS                                 #
##############################################################################
RED_INDEX = 0
GREEN_INDEX = 1
BLUE_INDEX = 2
RED_MULT = 0.299
GREEN_MULT = 0.587
BLUE_MULT = 0.114
BLACK = 0
WHITE = 255
NUMBER_OPTIONS_TO_CHOOSE = ["1", "2", "3", "4", "5", "6", "7", "8"]
OPTIONS_TO_DIRECTIONS = "RL"
NUM_OF_ARGS_NOT_VALID = "Invalid number of arguments, try: python3 image_editor.py <image_path>"
ERROR_MSG_FILE_DOESNT_EXIST = "Invalid file path!"
ERROR_MSG_FILE_EXTENSION = "Invalid image extension!"
OPTIONS_TO_CHOOSE = """    Hello!
    Welcome to the Image Editor! What would you like to do with your image?
    1. Convert ColoredImage to GrayScaleImage
    2. Blur the image
    3. Resize the image
    4. Rotate the image in 90 degrees
    5. Create an outline (edges) image of the original image
    6. Quantize the image
    7. Show the image
    8. Exit the program
    Please insert a number of option: 
    """
ERROR_MSG_WRONG_INPUT_OF_OPTION = "Invalid number of option, try again: "
ERROR_MSG_IMAGE_ALREADY_GRAYSCALED = "Image is already grayscaled! Image didn't changed."
BLUR_IMG_INPUT_MSG = "Please enter the number of kernel size you want to blur with: "
ERROR_MSG_FOR_KERNEL_SIZE = "Invalid input for kernel size, kernel size need to be an odd positive number!"
RESIZE_IMG_INPUT_MSG = "Please enter the new sizes for the image by the format: (height,width): "
ERROR_MSG_FOR_RESIZE_SIZES = "Invalid input for new sizes, the format is (new height,new width)!"
ROTATE_INPUT_MSG = "Please enter a direction you want to rotate your pic, R (right) or L (left): "
ERROR_MSG_FOR_ROTATE_INPUT = "Invalid input for rotation direction, must be R or L!"
EDGES_INPUT_MSG = "Please enter blur size, block size and c, the format is (blur size,block size,c): "
ERROR_MSG_FOR_EDGES = "Invalid input for edges, the format is (blur size,block size,c)!"
QUANTIZE_INPUT_MSG = "Please enter number of scales after quantize: "
ERROR_MSG_FOR_QUANTIZE = "Invalid input for number of scales, must be an integer that is greater than one!"
IMAGE_PATH_INPUT_MSG = "Plase enter the path you want the image in: "
ERROR_MSG_IMAGE_PATH = "Can't save the image in this path, try again: "
##############################################################################
#                                  Functions                                 #
##############################################################################
def separate_channels(image: ColoredImage) -> List[SingleChannelImage]:
    """
    This function gets an image (rows X culumns X channels) and returns new image (channels X rows X columns)
    """
    new_image = []
    channel_in_new_image = []
    column_in_new_image = []
    for i in range(len(image[0][0])):
        for row in range(len(image)):
            for col in range(len(image[row])):
                column_in_new_image.append(image[row][col][i]) # new pixel in row
            channel_in_new_image.append(column_in_new_image) # new cell in row
            column_in_new_image = []
        new_image.append(channel_in_new_image) # new row in image
        channel_in_new_image = []
    return new_image

def combine_channels(channels: List[SingleChannelImage]) -> ColoredImage:
    """
    This function gets an image seperated to channels (channels X rows X culumns) and return the combination of them ( rows X columns X channels)
    """
    new_image = []
    cell_in_new_row = []
    row_in_new_image = []
    for col in range(len(channels[0])):
        for cell in range(len(channels[0][0])):
            for channel in range(len(channels)):
                cell_in_new_row.append(channels[channel][col][cell]) # new pixel in row
            row_in_new_image.append(cell_in_new_row) # new cell in row
            cell_in_new_row = []
        new_image.append(row_in_new_image) # new row in image
        row_in_new_image = []
    return new_image

def calculate_colored_to_grayscale(pixel: List[int]) -> int:
    """
    This function gets pixel (in RGB mode) and returns the pixel in grayscale mode
    """
    return round(pixel[RED_INDEX] * RED_MULT + pixel[GREEN_INDEX] * GREEN_MULT + pixel[BLUE_INDEX] * BLUE_MULT)

def RGB2grayscale(colored_image: ColoredImage) -> SingleChannelImage:
    """
    This function gets RGB image and converts it to grayscaled, with specific formula
    The formula is: RED * 0.299 + GREEN * 0.587 + BLUE * 0.114
    """
    grayscaled_image = []
    row_in_grayscaled_image = []
    for row in range(len(colored_image)):
        for column in range(len(colored_image[row])):
            row_in_grayscaled_image.append(calculate_colored_to_grayscale(colored_image[row][column]))
        grayscaled_image.append(row_in_grayscaled_image)
        row_in_grayscaled_image = []
    return grayscaled_image

def blur_kernel(size: int) -> Kernel:
    """
    This function gets a size and converts it to a kernel, which is a matrix (size X size)
    And each cell is 1/(size^2)
    The function assumes that size is a positive odd int
    """
    value_of_each_cell = (1/(size*size))
    kernel_mat = []
    row_in_kernal_mat = []
    for i in range(size):
        for j in range(size):
            row_in_kernal_mat.append(value_of_each_cell)
        kernel_mat.append(row_in_kernal_mat)
        row_in_kernal_mat = []
    return kernel_mat

def is_out_of_original_range(image: SingleChannelImage, row: int, col: int) -> bool:
    """
    This function checks if the row and the col is out of range, and return False if so
    This function is used only to create_kernel_for_pixel() in order to remove conditions from the function
    """
    if row >= 0 and row < len(image) and col >= 0 and col < len(image[0]):
        return False
    return True

def create_kernel_for_pixel(image: SingleChannelImage, size: int, pixel_row: int, pixel_col: int) -> Kernel:
    """
    This function gets image, size of kernel and pixel location and creates a kernel around the pixel given
    """
    kernel_mat = []
    new_row_in_kernel = []
    size_divided = size // 2
    for row in range(-size_divided, size_divided + 1): # run all indexes of rows in the new matrix
        for col in range(-size_divided, size_divided + 1): # run all indexes of columns in the new matrix
            next_row_in_new_matrix = pixel_row + row # the next row
            next_col_in_new_matrix = pixel_col + col # the next col
            if not is_out_of_original_range(image, next_row_in_new_matrix, next_col_in_new_matrix):
                # if it's not out of range, add to the row the cell from the image
                new_row_in_kernel.append(image[next_row_in_new_matrix][next_col_in_new_matrix])
            else: 
                # it's out of range, so add to the row the cell from the middle (pixel_row, pixel_col)
                new_row_in_kernel.append(image[pixel_row][pixel_col])
        kernel_mat.append(new_row_in_kernel) # add row to the new kernel
        new_row_in_kernel = []
    return kernel_mat
    
def sum_kernel_for_pixel_and_kernel(kernel_for_pixel: Kernel, kernel: Kernel) -> int:
    """
    This function gets a kernel for specific pixel and a kernel, and convolve them
    """
    sum = 0
    for row in range(len(kernel)): # could be kernel_for_pixel because they have the same length
        for column in range(len(kernel[row])): # could be kernel_for_pixel because they have the same length
            sum += kernel[row][column] * kernel_for_pixel[row][column]
    if sum < 0: # each pixel is in range of 0 to 255
        return 0
    elif sum > 255: # each pixel is in range of 0 to 255
        return 255
    return round(sum) # round the sum and return it

def apply_kernel(image: SingleChannelImage, kernel: Kernel) -> SingleChannelImage:
    """
    This function gets image and kernel, and apply the kernel into the image
    The function doesn't change the original image, and returns new one
    """
    new_image = deepcopy(image)
    size_of_kernel = len(kernel)
    for row in range(len(image)):
        for column in range(len(image[row])):
            # run every pixel in the image
            kernel_for_pixel = create_kernel_for_pixel(image, size_of_kernel, row, column) # creates a kernel to this specific pixel
            new_image[row][column] = sum_kernel_for_pixel_and_kernel(kernel_for_pixel, kernel) # add to the new image their convolve
    return new_image

def pixel_value_calculator(a_pixel: int, b_pixel: int, c_pixel: int, d_pixel: int, delta_x: float, delta_y: float) -> int:
    """
    This function calculate a value for pixel by a specific formula and returns the round of it
    Formula: a(1-△x)(1-△y) + b△y(1-△x) + c△x(1-△y) + d△x△y
    """
    a_calculate = a_pixel * (1 - delta_x) * (1 - delta_y)
    b_calculate = b_pixel * delta_y * (1 - delta_x)
    c_calculate = c_pixel * delta_x * (1 - delta_y)
    d_calculate = d_pixel * delta_x * delta_y
    return round(a_calculate + b_calculate + c_calculate + d_calculate)

def bilinear_interpolation(image: SingleChannelImage, y: float, x: float) -> int:
    """
    This function gets an image, y (row number) and x (column number) and returns the bilinear interpolation for image[y][x]
    """
    if (y == 0 or y == len(image)-1) and (x == 0 or x == len(image[0])-1):
        return image[int(y)][int(x)]
    rounded_x = int(x // 1)
    rounded_y = int(y // 1)
    if rounded_x == x and rounded_x == len(image[0])-1:
        rounded_x -= 1
    if rounded_y == y and rounded_y == len(image)-1:
        rounded_y -= 1
    if rounded_y == len(image)-1:
        rounded_y -= 1
    if rounded_x == len(image[0]) -1:
        rounded_x -= 1
    delta_x = x - rounded_x
    delta_y = y - rounded_y
    a_pixel = image[rounded_y][rounded_x]
    b_pixel = image[rounded_y + 1][rounded_x]
    c_pixel = image[rounded_y][rounded_x + 1]
    d_pixel = image[rounded_y + 1][rounded_x + 1]
    return pixel_value_calculator(a_pixel, b_pixel, c_pixel, d_pixel, delta_x, delta_y)

def calculate_relative_location(source_image_row_size: int, source_image_col_size: int, dest_image_row_size: int, dest_image_col_size: int, pixel_row: int, pixel_col: int) -> tuple[float, float]:
    """
    This function calculates the relative location of a pixel from the destination image to the source image
    """
    relative_row = (pixel_row / dest_image_row_size) * source_image_row_size
    relative_col = (pixel_col / dest_image_col_size) * source_image_col_size
    return relative_row, relative_col

def resize(image: SingleChannelImage, new_height: int, new_width: int) -> SingleChannelImage:
    """
    This function gets an image, new height and new width and returns a new image, after resizing it
    The function uses bilinear_interpolation() calculation
    """
    dest_image = [] # the destination image
    row_in_dest_image = []
    for row in range(new_height): # creates new_image with defaultive values, which I decided - zero
        for col in range(new_width):
            row_in_dest_image.append(0)
        dest_image.append(row_in_dest_image)
        row_in_dest_image = []
    # Set the corners of the destination image by the source image values
    dest_image[0][0] = image[0][0]
    dest_image[0][len(dest_image[0])-1] = image[0][len(image[0])-1]
    dest_image[len(dest_image)-1][0] = image[len(image)-1][0]
    dest_image[len(dest_image)-1][len(dest_image[0])-1] = image[len(image)-1][len(image[0])-1]
    # Run all the pixels and change them by bilinear_interpolation calculation, except the corners
    for row in range(len(dest_image)):
        for col in range(len(dest_image[0])):
            if not((row == 0 and col == 0) or (row == 0 and col == len(dest_image[0])-1) or (row == len(dest_image)-1 and col == 0) or (row == len(dest_image)-1 and col == len(dest_image[0])-1)):
                relative_row, relative_col = calculate_relative_location(len(image)-1, len(image[0])-1, new_height-1, new_width-1, row, col)
                bilinear_interpolation_for_pixel = bilinear_interpolation(image, relative_row, relative_col)
                dest_image[row][col] = bilinear_interpolation_for_pixel
    return dest_image

def rotate_90(image: Image, direction: str) -> Image:
    """
    This function gets image and direction ('R' or 'L') and roates the image in 90 degrees to the direction given
    The function rotates to R direction only, and for L doing the direction in R mode 3 times
    """
    if direction == 'L':
        return rotate_90(rotate_90(rotate_90(image, 'R'), 'R'), 'R') # If the direction is L, do R three times (do 270 and not -90, it's the same)
    # The function assumes that the direction is 'R' or 'L', so if got here - the direction is 'R' for sure
    image_rotated = []
    new_row_in_rotated_image = []
    for col in range(len(image[0])): # for every column in the image from the start to the end
        for row in range(len(image)-1, -1, -1): # for every row in the image from the end to the start
            new_row_in_rotated_image.append(image[row][col]) # add to the new row
        image_rotated.append(new_row_in_rotated_image) # add the new row to the image
        new_row_in_rotated_image = [] # reset the row for next loop
    return image_rotated

def calculate_threshold_for_pixel(kernel_for_pixel: Kernel, c: float) -> float:
    """
    This function calculate the threshold value for pixel and returns it
    """
    sum = 0.0
    for row in range(len(kernel_for_pixel)):
        for col in range(len(kernel_for_pixel[row])):
            sum += kernel_for_pixel[row][col]
    return (sum / (len(kernel_for_pixel)*len(kernel_for_pixel))) - c

def get_edges(image: SingleChannelImage, blur_size: int, block_size: int, c: float) -> SingleChannelImage:
    """
    This function gets an image, blur_size, block_size and a constant and returns new image that shows only the lines around the object, black (0) or white (255)
    """
    kernel = blur_kernel(blur_size) # creates a kernel from blur_size
    blurred_image = apply_kernel(image, kernel) # create a blurred image from the original
    kernel_for_pixel = []
    edges_image = []
    for row in range(len(blurred_image)):
        edges_image.append([])
        for col in range(len(blurred_image[row])):
            kernel_for_pixel = create_kernel_for_pixel(blurred_image, block_size, row, col)
            threshold = calculate_threshold_for_pixel(kernel_for_pixel, c)
            if threshold > blurred_image[row][col]:
                edges_image[row].append(BLACK)
            else:
                edges_image[row].append(WHITE)
    return edges_image

def quantize_for_rgb_image(image: ColoredImage, N: int) -> ColoredImage:
    """
    This function gets an image and a number and quantize the image from rgb
    """
    if isinstance(image[0][0], int): # its SingleChannelImage
        return quantize(image, N)
    seperated_channels_image = separate_channels(image)
    quantize_channels = []
    for channel in seperated_channels_image:
        quantize_channels.append(quantize(channel, N))
    combined_channels_image = combine_channels(quantize_channels)
    return combined_channels_image

def quantize(image: SingleChannelImage, N: int) -> SingleChannelImage:
    """
    This function gets an image and a number and quantize the image
    """
    if isinstance(image[0][0], list): # Its ColoredImage
        return quantize_for_rgb_image(image, N)
    quantize_img = deepcopy(image)
    for row in range(len(quantize_img)):
        for col in range(len(quantize_img[row])):
            quantize_value_for_pixel = round(floor(quantize_img[row][col] * N / 256) * 255 / (N - 1))
            quantize_img[row][col] =  quantize_value_for_pixel
    return quantize_img

def check_validity_args_for_edges_func(values: str) -> bool: # CONTINUE THIS FUNC
    """
    This function checks the validity of the arguments got to edges function
    """
    try:
        splitted_values = values.split(",") 
        if len(splitted_values) != 3: # if there is more than 3 args splittes by ","
            return False
        blur_size = splitted_values[0]
        block_size = splitted_values[1]
        c = splitted_values[2]
        if " " in c: # spaces not allowed
            return False
        # blur_size and block_size need to be positive-odd integers
        if not blur_size.isnumeric():
            return False
        if not block_size.isnumeric():
            return False
        blur_size = int(blur_size)
        block_size = int(block_size)
        if blur_size <= 0:
            return False
        if block_size <= 0:
            return False
        if blur_size % 2 == 0:
            return False
        if block_size % 2 == 0:
            return False
        # c needs to be non-negative
        c = float(c)
        if c < 0:
            return False        
        return True
    except: # if an error was raised, its probably because can't split 'values' or convert to int/false - invalid input
        return False

def check_validity_args_for_quantize_func(number_of_scales: str) -> bool:
    """
    This function check the validity of the arguments given to quantize function
    """
    try:
        if not number_of_scales.isnumeric():
            return False
        number_of_scales = int(number_of_scales)
        if number_of_scales <= 1:
            return False
        return True
    except:
        return False

if __name__ == '__main__': 
    if len(sys.argv) != 2:
        sys.exit(NUM_OF_ARGS_NOT_VALID)
    image_path = sys.argv[1]
    try:
        loaded_img = load_image(image_path)
        img = deepcopy(loaded_img)
    except FileNotFoundError:
        sys.exit(ERROR_MSG_FILE_DOESNT_EXIST)
    except PIL.UnidentifiedImageError:
        sys.exit(ERROR_MSG_FILE_EXTENSION)
    is_grayscaled_img = isinstance(img[0][0], int) # True -> GrayScaled, False -> ColoredImage
    if not is_grayscaled_img:
        seperated_channels_img = separate_channels(img)
    option_chose = input(OPTIONS_TO_CHOOSE)
    new_img = []
    want_to_exit = False # a flag which point on if the user want to exit the program or not
    while not want_to_exit:
        while not (option_chose in NUMBER_OPTIONS_TO_CHOOSE): # run until the option is valid
            print(ERROR_MSG_WRONG_INPUT_OF_OPTION)
            option_chose = input(OPTIONS_TO_CHOOSE)
        if option_chose == NUMBER_OPTIONS_TO_CHOOSE[0]: # Change ColoredImage to GracyScaled
            if is_grayscaled_img: # Can't converu GrayScaledImage to GrayScaledImage
                print(ERROR_MSG_IMAGE_ALREADY_GRAYSCALED)
            else: # Its ColoredImage
                img = RGB2grayscale(img)
        elif option_chose == NUMBER_OPTIONS_TO_CHOOSE[1]: # Blur the image
            kernel_size = input(BLUR_IMG_INPUT_MSG)
            if not kernel_size.isnumeric() or int(kernel_size) <= 0 or isinstance(kernel_size, float) or int(kernel_size) % 2 == 0:
                print(ERROR_MSG_FOR_KERNEL_SIZE)
            else:
                if is_grayscaled_img:
                    img = apply_kernel(img, blur_kernel(int(kernel_size)))
                else: # Its ColoredImage
                    for channel in seperated_channels_img: # Blur every channel
                        new_img.append(apply_kernel(channel, blur_kernel(int(kernel_size))))
                    img = combine_channels(new_img) # Combine the channel to RGB 
        elif option_chose == NUMBER_OPTIONS_TO_CHOOSE[2]: # Resize the image
            new_sizes = input(RESIZE_IMG_INPUT_MSG)
            try:
                height_and_width = new_sizes.split(",")
                if len(height_and_width) != 2:
                    print(ERROR_MSG_FOR_RESIZE_SIZES)
                if not (height_and_width[0].isnumeric() and height_and_width[1].isnumeric()):
                    print(ERROR_MSG_FOR_RESIZE_SIZES)
                elif isinstance(height_and_width[0], float) or isinstance(height_and_width[1], float):
                    print(ERROR_MSG_FOR_RESIZE_SIZES)
                else:
                    new_height = int(height_and_width[0])
                    new_width = int(height_and_width[1])
                    if new_height < 1 or new_width < 1:
                        print(ERROR_MSG_FOR_RESIZE_SIZES)
                    elif is_grayscaled_img:
                        img = resize(img, new_height, new_width)
                    else: # Its ColoredImage
                        for channel in seperated_channels_img: # Resize every channel
                            new_img.append(resize(channel, new_height, new_width))
                        img = combine_channels(new_img)
            except:
                print(ERROR_MSG_FOR_RESIZE_SIZES)
        elif option_chose == NUMBER_OPTIONS_TO_CHOOSE[3]: # Rotate in 90 degrees
            direction = input(ROTATE_INPUT_MSG)
            if direction not in OPTIONS_TO_DIRECTIONS or len(direction) != 1:
                print(ERROR_MSG_FOR_ROTATE_INPUT)
            else:
                if is_grayscaled_img:
                    img = rotate_90(img, direction)
                else: # Its ColoredImage
                    for channel in seperated_channels_img:
                        new_img.append(rotate_90(channel, direction))
                    img = combine_channels(new_img)
        elif option_chose == NUMBER_OPTIONS_TO_CHOOSE[4]: # Create Edges
            values_for_edges = input(EDGES_INPUT_MSG)
            if not check_validity_args_for_edges_func(values_for_edges):
                print(ERROR_MSG_FOR_EDGES)
            else:
                splitted_values = values_for_edges.split(",")
                blur_size = int(splitted_values[0])
                block_size = int(splitted_values[1])
                c = float(splitted_values[2])
                if is_grayscaled_img:
                    img = get_edges(img, blur_size, block_size, c)
                else: # Its ColoredImage
                    grayscaled_img = RGB2grayscale(img)
                    img = get_edges(grayscaled_img, blur_size, block_size, c)
        elif option_chose == NUMBER_OPTIONS_TO_CHOOSE[5]: # Quantize
            number_of_scales = input(QUANTIZE_INPUT_MSG)
            if not check_validity_args_for_quantize_func(number_of_scales):
                print(ERROR_MSG_FOR_QUANTIZE)
            else:
                number_of_scales = int(number_of_scales)
                if is_grayscaled_img:
                    img = quantize(img, number_of_scales)
                else: # Its ColordImage
                    img = quantize_for_rgb_image(img, number_of_scales)
        elif option_chose == NUMBER_OPTIONS_TO_CHOOSE[6]: # Show the image
            show_image(img)
        elif option_chose == NUMBER_OPTIONS_TO_CHOOSE[7]: # Exit the program
            path_to_save = input(IMAGE_PATH_INPUT_MSG)
            cant_save = True
            want_to_exit = True
            while cant_save:
                try:
                    save_image(img, path_to_save)
                    cant_save = False
                except Exception as e:
                    path_to_save = input(ERROR_MSG_IMAGE_PATH)
            break
        option_chose = input(OPTIONS_TO_CHOOSE.replace("Hello!\n", ""))
        new_img = []
        is_grayscaled_img = isinstance(img[0][0], int) # True -> GraySclaed, False -> ColordImage
        if not is_grayscaled_img:
            seperated_channels_img = separate_channels(img)

