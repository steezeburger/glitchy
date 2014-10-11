__author__ = 'js'

import random

import argparse

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

    image_file = open(image, 'w')
    image_file.write(data)
    image_file.close

    return image

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='python jpg glitcher')
    parser.add_argument('-s', action='store', dest='filename', help='input jpg filename')
    parse_results = parser.parse_args()

    print(parse_results.filename)

    for i in range(0,3):
        glitched_image = glitch(parse_results.filename)
    print glitched_image