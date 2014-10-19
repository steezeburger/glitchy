__author__ = 'js'

import random
import argparse
from PIL import Image

# creates random start and end locations
def random_start_end(photo_data):
    start = random.randint(2500, len(photo_data))
    end = start + random.randint(0, len(photo_data) - start)

    return start, end

# copy/pastes chucnk of data addressed by random_start_end
# a random number of times
def splice_file(photo_data):
    start, end = random_start_end(photo_data)
    splice = photo_data[start:end]
    repeat = ''

    for i in range(1, random.randint(1,10)):
        repeat += splice

    newStart, newEnd = random_start_end(photo_data)
    photo_data = photo_data[:newStart] + repeat + photo_data[newEnd:]
    return photo_data

# opens picture
def glitch(image):
    image_file = open(image, 'r')
    data = image_file.read()
    image_file.close() 

    for i in range (1, random.randint(1,10)):
        data = splice_file(data)

    new_file = 'glitched_' + image

    image_file = open(new_file, 'w')
    image_file.write(data)
    image_file.close

    return new_file

# will run script if ran from same directory
if __name__ == '__main__':

    # argument parsing
    parser = argparse.ArgumentParser(description='python jpg glitcher')
    parser.add_argument('-f', action='store', dest='filename', help='name of .jpg file')
    parse_results = parser.parse_args()


    print(parse_results.filename)

    # passes filename to glitch function
    image_file = parse_results.filename
    glitched_image = glitch(image_file)

    # convert to jpg (even though it's already jpg)
    # this seems to get rid of excess data that was
    # creating really large file sizes and sometimes
    # causing corruption issues
    try:
        Image.open(glitched_image).save(glitched_image)
        print outfile
    except IOError:
        print("cannot convert", glitched_image)
