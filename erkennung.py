from PIL import Image
import matplotlib.pyplot as plt
import sys


matrix_1 = [
    [ 1,  0, -1],
    [ 1,  0, -1],
    [ 1,  0, -1]
]
matrix_2 = [
    [-1,  0,  1],
    [-1,  0,  1],
    [-1,  0,  1]
]
matrix_3 = [
    [ 1,  1,  1],
    [ 0,  0,  0],
    [-1, -1, -1]
]
matrix_4 = [
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
]
matrix_5 = [
    [-1, -1,  0],
    [-1,  0,  1],
    [ 0,  1,  1]
]
matrix_6 = [
    [ 0, -1, -1],
    [ 1,  0, -1],
    [ 1,  1,  0]
]
matrix_7 = [
    [ 1,  1,  0],
    [ 1,  0, -1],
    [ 0, -1, -1]
]
matrix_8 = [
    [ 0,  1,  1],
    [-1,  0,  1],
    [-1, -1,  0]
]

all_martices = [matrix_3, matrix_4, matrix_5, matrix_6, matrix_7, matrix_8] #, matrix_1, matrix_2


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


def filter_img_with_matrix(image, matrix):
    old_pixels = image.load()
    new_image = Image.new('RGB', (image.width, image.height))
    new_pixels = new_image.load()
    treshhold = 100
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel_window = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]
            if i == 0:
                if j == 0:
                    pixel_window[0][0] = old_pixels[i, j][0]
                    pixel_window[0][1] = old_pixels[i, j][0]
                    pixel_window[0][2] = old_pixels[i, j][0]
                    pixel_window[1][0] = old_pixels[i, j][0]
                    pixel_window[2][0] = old_pixels[i, j][0]

                    pixel_window[1][1] = old_pixels[i, j][0]
                    pixel_window[1][2] = old_pixels[i, j+1][0]
                    pixel_window[2][1] = old_pixels[i+1, j][0]
                    pixel_window[2][2] = old_pixels[i+1, j+1][0]
                elif j == image.size[1]-1:
                    pixel_window[0][0] = old_pixels[i, j][0]
                    pixel_window[0][1] = old_pixels[i, j][0]
                    pixel_window[0][2] = old_pixels[i, j][0]
                    pixel_window[1][2] = old_pixels[i, j][0]
                    pixel_window[2][2] = old_pixels[i, j][0]

                    pixel_window[1][0] = old_pixels[i, j-1][0]
                    pixel_window[1][1] = old_pixels[i, j][0]
                    pixel_window[2][0] = old_pixels[i+1, j-1][0]
                    pixel_window[2][1] = old_pixels[i+1, j][0]
                else:
                    pixel_window[0][0] = old_pixels[i, j][0]
                    pixel_window[0][1] = old_pixels[i, j][0]
                    pixel_window[0][2] = old_pixels[i, j][0]

                    pixel_window[1][2] = old_pixels[i, j + 1][0]
                    pixel_window[2][2] = old_pixels[i + 1, j + 1][0]
                    pixel_window[1][0] = old_pixels[i, j-1][0]
                    pixel_window[1][1] = old_pixels[i, j][0]
                    pixel_window[2][0] = old_pixels[i+1, j-1][0]
                    pixel_window[2][1] = old_pixels[i+1, j][0]
            elif i == image.size[0]-1:
                if j == 0:
                    pixel_window[0][0] = old_pixels[i, j][0]
                    pixel_window[1][0] = old_pixels[i, j][0]
                    pixel_window[2][0] = old_pixels[i, j][0]
                    pixel_window[2][1] = old_pixels[i, j][0]
                    pixel_window[2][2] = old_pixels[i, j][0]

                    pixel_window[0][1] = old_pixels[i - 1, j][0]
                    pixel_window[0][2] = old_pixels[i - 1, j + 1][0]
                    pixel_window[1][1] = old_pixels[i, j][0]
                    pixel_window[1][2] = old_pixels[i, j + 1][0]
                elif j == image.size[1]-1:
                    pixel_window[2][0] = old_pixels[i, j][0]
                    pixel_window[2][1] = old_pixels[i, j][0]
                    pixel_window[2][2] = old_pixels[i, j][0]
                    pixel_window[1][2] = old_pixels[i, j][0]
                    pixel_window[0][2] = old_pixels[i, j][0]

                    pixel_window[0][0] = old_pixels[i - 1, j - 1][0]
                    pixel_window[0][1] = old_pixels[i - 1, j][0]
                    pixel_window[1][0] = old_pixels[i, j - 1][0]
                    pixel_window[1][1] = old_pixels[i, j][0]
                else:
                    pixel_window[2][0] = old_pixels[i, j][0]
                    pixel_window[2][1] = old_pixels[i, j][0]
                    pixel_window[2][2] = old_pixels[i, j][0]

                    pixel_window[0][0] = old_pixels[i - 1, j - 1][0]
                    pixel_window[0][1] = old_pixels[i - 1, j][0]
                    pixel_window[1][0] = old_pixels[i, j - 1][0]
                    pixel_window[1][1] = old_pixels[i, j][0]
                    pixel_window[1][2] = old_pixels[i, j + 1][0]
                    pixel_window[0][2] = old_pixels[i - 1, j + 1][0]
            elif j == 0:
                pixel_window[0][0] = old_pixels[i, j][0]
                pixel_window[1][0] = old_pixels[i, j][0]
                pixel_window[2][0] = old_pixels[i, j][0]

                pixel_window[2][1] = old_pixels[i + 1, j][0]
                pixel_window[2][2] = old_pixels[i + 1, j + 1][0]
                pixel_window[0][1] = old_pixels[i - 1, j][0]
                pixel_window[0][2] = old_pixels[i - 1, j + 1][0]
                pixel_window[1][1] = old_pixels[i, j][0]
                pixel_window[1][2] = old_pixels[i, j + 1][0]
            elif j == image.size[1]-1:

                pixel_window[2][2] = old_pixels[i, j][0]
                pixel_window[1][2] = old_pixels[i, j][0]
                pixel_window[0][2] = old_pixels[i, j][0]

                pixel_window[2][0] = old_pixels[i + 1, j - 1][0]
                pixel_window[2][1] = old_pixels[i + 1, j][0]
                pixel_window[0][0] = old_pixels[i - 1, j - 1][0]
                pixel_window[0][1] = old_pixels[i - 1, j][0]
                pixel_window[1][0] = old_pixels[i, j - 1][0]
                pixel_window[1][1] = old_pixels[i, j][0]
            else:
                pixel_window[0][0] = old_pixels[i - 1, j - 1][0]
                pixel_window[0][1] = old_pixels[i - 1, j][0]
                pixel_window[0][2] = old_pixels[i - 1, j + 1][0]
                pixel_window[1][0] = old_pixels[i, j - 1][0]
                pixel_window[1][1] = old_pixels[i, j][0]
                pixel_window[1][2] = old_pixels[i, j + 1][0]
                pixel_window[2][0] = old_pixels[i + 1, j - 1][0]
                pixel_window[2][1] = old_pixels[i + 1, j][0]
                pixel_window[2][2] = old_pixels[i + 1, j + 1][0]
            sum_value = 0

            for i_temp in range(len(pixel_window)):
                for j_temp in range(len(pixel_window[i_temp])):
                    sum_value = sum_value + (pixel_window[i_temp][j_temp] * matrix[i_temp][j_temp])
            if sum_value > treshhold:
                new_pixels[i, j] = (sum_value, sum_value, sum_value)

    return new_image


def process_all_filter(image, all_matrices):
    out_images = []
    i = 0
    print("processing all filters... ")
    for matrix in all_matrices:
        i = i + 1
        print("processing ... ({}/{})".format(i, len(all_matrices)))
        out_images.append(filter_img_with_matrix(image, matrix))
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


def sum_images_norm(images):
    new_image = Image.new('RGB', (images[0].width, images[0].height))
    new_pixels = new_image.load()
    max_value = -sys.maxsize + 1
    min_value = sys.maxsize
    for i in range(images[0].size[0]):
        for j in range(images[0].size[1]):
            sum = 0
            for image in images:
                temp_old_pixels = image.load()
                sum = sum + temp_old_pixels[i, j][0]
                avr = int(sum / len(images))
                if avr > max_value:
                    max_value = avr
                if avr < min_value:
                    min_value = avr

            new_pixels[i, j] = (avr, avr, avr)
    for i in range(images[0].size[0]):
        for j in range(images[0].size[1]):
            norm = int(((new_pixels[i, j][0] - min_value)/(max_value-min_value))*255)
            new_pixels[i, j] = (norm, norm, norm)
    return new_image


image = Image.open("image6.jpg")
image_avg_sw = make_sw(image)

#matrix_0_erg = filter_img_with_matrix(image, matrix_7)
#matrix_1_erg = filter_img_with_matrix(image, matrix_8)
images_with_matrices = process_all_filter(image_avg_sw, all_martices)
sum_image = sum_images(images_with_matrices)
sum_image2 = sum_images_norm(images_with_matrices)

t_i_o = three_in_one_pictures(image, sum_image, sum_image2)
#t_i_o = three_in_one_pictures(image_avg_sw, matrix_0_erg, matrix_1_erg)

t_i_o.show()
