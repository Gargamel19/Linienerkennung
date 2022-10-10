import math

from PIL import Image
import sys

ammount = 10

matrix_1 = [[ 1,  1, -1, -1]] * ammount

matrix_2 = [[-1, -1,  1,  1]] * ammount
matrix_3 = [
    [ 1] * ammount,
    [ 1] * ammount,
    [-1] * ammount,
    [-1] * ammount
]
matrix_4 = [
    [-1] * ammount,
    [-1] * ammount,
    [ 1] * ammount,
    [ 1] * ammount
]
#matrix_5 = []
#matrix_6 = []
#matrix_7 = []
#matrix_8 = []
#for i in range(ammount + 1):
#    matrix_5.append(([-1] * (ammount-i)) + ([1] * i))
#    matrix_6.append(([1] * (ammount-i)) + ([-1] * i))
#    matrix_7.append(([1] * i) + ([-1] * (ammount-i)))
#    matrix_8.append(([-1] * i) + ([1] * (ammount-i)))

all_martices = [matrix_1, matrix_2, matrix_3, matrix_4]#, matrix_5, matrix_6, matrix_7, matrix_8] #


def two_in_one_pictures(file1, file2):
    new_with = 0
    space_between = 0
    new_with = new_with + file1.width + space_between + file2.width
    new_image = Image.new('RGB', (new_with, image.width))
    old_1_pixels = file1.load()
    old_2_pixels = file2.load()
    new_pixels = new_image.load()
    for i in range(new_image.size[0]):
        for j in range(new_image.size[1]):
            if i < file1.width:
                new_pixels[i, j] = old_1_pixels[i, j]
            else:
                new_pixels[i, j] = old_2_pixels[i-file1.width, j]
    return new_image



def three_in_one_pictures(file1, file2, file3):
    new_with = 0
    new_with = new_with + file1.width + file2.width + file3.width
    new_image = Image.new('RGB', (new_with, image.height))
    old_1_pixels = file1.load()
    old_2_pixels = file2.load()
    old_3_pixels = file3.load()
    new_pixels = new_image.load()
    for i in range(new_image.width):
        for j in range(new_image.height):
            if i < file1.width:
                new_pixels[i, j] = old_1_pixels[i, j]
            elif i < file1.width + file2.width:
                new_pixels[i, j] = old_2_pixels[i-file1.width, j]
            else:
                new_pixels[i, j] = old_3_pixels[i-(file1.width + file2.width), j]
    return new_image


def make_sw_min(image):
    old_pixels = image.load()
    new_image = Image.new('RGB', (image.width, image.height))
    new_pixels = new_image.load()
    for i in range(new_image.size[0]):
        for j in range(new_image.size[1]):
            min_color = 255
            for color in old_pixels[i, j]:
                if color < min_color:
                    min_color = color
            new_pixels[i, j] = (min_color, min_color, min_color)
    return new_image


def make_sw(image):
    old_pixels = image.load()
    new_image = Image.new('RGB', (image.width, image.height))
    new_pixels = new_image.load()
    for i in range(new_image.size[0]):
        for j in range(new_image.size[1]):
            added = 0
            for color in old_pixels[i, j]:
                added = added + color
            new_pixels[i, j] = (int(added/3), int(added/3), int(added/3))
    return new_image


def normalize_pic(old_image):
    new_image = Image.new('RGB', (old_image.width, old_image.height))
    new_pixels = new_image.load()
    old_pixels = image.load()
    max_value = -sys.maxsize + 1
    min_value = sys.maxsize
    for i in range(old_image.size[0]):
        for j in range(old_image.size[1]):
            value = old_pixels[i, j][0]
            if value > max_value:
                max_value = value
            if value < min_value:
                min_value = value
    for i in range(old_image.size[0]):
        for j in range(old_image.size[1]):
            norm = int(((old_pixels[i, j][0] - min_value)/(max_value-min_value))*255)
            new_pixels[i, j] = (norm, norm, norm)
    return new_image


def filter_img_with_matrix(image, matrix):
    thresh_hold = 400
    old_pixels = image.load()
    image_width = image.width
    image_height = image.height
    new_image = Image.new('RGB', (image_width, image_height))
    new_pixels = new_image.load()

    for i in range(image_width):
        for j in range(image_height):
            pixel_window = []
            sum_value = 0
            for i_offset in range(len(matrix)):
                pixel_window.append([])
                for j_offset in range(len(matrix[i_offset])):

                    i_index = i
                    j_index = j
                    bounds = math.floor(i_offset/2)
                    if (i - (i_offset-bounds) < image_width) and (i - (i_offset-bounds) > 0):
                        i_index = i - (i_offset-bounds)
                    if (j - (j_offset-bounds) < image_height) and (j - (j_offset-bounds) > 0):
                        j_index = j - (j_offset-bounds)
                    sum_value = sum_value + old_pixels[i_index, j_index][0] * matrix[i_offset][j_offset]

            if sum_value > thresh_hold:
                value = int((sum_value/(len(matrix) * len(matrix[0])))*255)
                new_pixels[i, j] = (value, value, value)
    return new_image


def process_all_filter(origin_image, all_matrices):
    out_images = []
    i = 0
    print("processing all filters... ")
    for matrix in all_matrices:
        i = i + 1
        print("\r", end="")
        print("processing ... ({}/{})".format(i, len(all_matrices)), end="")
        new_image = filter_img_with_matrix(origin_image, matrix)
        out_images.append(new_image)

    print("\r", end="")
    print("all done...")
    return out_images


def sum_images(images):
    new_image = Image.new('RGB', (images[0].width, images[0].height))
    new_pixels = new_image.load()
    for i in range(images[0].size[0]):
        for j in range(images[0].size[1]):
            sum = 0
            for image in images:
                temp_old_pixels = image.load()
                sum = sum + temp_old_pixels[i, j][0]
            new_pixels[i, j] = (sum, sum, sum)
    return new_image


image = Image.open("image5.jpg")
image_avg_sw = make_sw(image)
print("image sizes:", image.width, image.height)

images_with_matrices = process_all_filter(image_avg_sw, all_martices)
sum_image = sum_images(images_with_matrices)

t_i_o = three_in_one_pictures(image, images_with_matrices[3], sum_image)
#t_i_o = three_in_one_pictures(image_avg_sw, matrix_0_erg, matrix_1_erg)

t_i_o.show()
