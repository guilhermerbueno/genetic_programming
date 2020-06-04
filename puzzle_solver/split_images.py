from PIL import Image
import os
import sys
import numpy as np

def main(image_path, x_blocks=5, y_blocks=5, target_dir='./puzzles/'):
    ''' receives the path of original image, the number of blocks on x-axis, 
    number of blocks on y-axis and the target directory to save the pieces'''
    image = Image.open(image_path)
    print('The image size is {}'.format(image.size))
    image_width, image_height = image.size
    block_height = image_height / float(y_blocks)
    block_width = image_width / float(x_blocks)
    k = 1
    for i in np.arange(0, image_width, block_width):
        for j in np.arange(0, image_height, block_height):
            block = (j, i, j+block_height, i+block_width)
            a = image.crop(block)
            try:
                a.save(os.path.join(target_dir, "%s.png" % k))
            except:
                pass
            k += 1


main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])