import ffmpeg
from pprint import pprint
import cv2
import numpy as np
import os

def converter(input_file_path, output_file_path):
    try:
        stream = ffmpeg.input(input_file_path)
        stream = ffmpeg.output(stream, output_file_path)
        ffmpeg.run(stream)

        print('Converting video successful')
    except FileNotFoundError as error:
        print(error)

def get_metadata(file_path):
    try:
        video = ffmpeg.probe(str(file_path))
        meta = video['streams']

        pprint(meta)
    except FileNotFoundError as error:
        print(error)

# sample images from video
def sample_images(video_file_path, data_folder_path):
    video = cv2.VideoCapture(video_file_path)
    video.set(cv2.CAP_PROP_FPS, 10)

    try:
        if not os.path.exists(data_folder_path):
            os.makedirs(data_folder_path)

    except OSError:
        print ('Error: Creating directory of data')

    current_frame = 0
    # factor = video.get(cv2.CAP_PROP_FPS)
    # print(factor)
    i = 0

    while True:
        if i%2 == 0:
            ret, frame = video.read()

            file_name = str(data_folder_path) + '/frame' + str(current_frame) + '.jpg'
            print('Creating...' + file_name)
            cv2.imwrite(file_name, frame)

            # current_frame += 1 * factor
            current_frame += 1

            i += 1

    video.release()
    cv2.destroyAllWindows()

# get sample images
sample_images('C:/Users/richa/Videos/small.mp4', 'C:/Users/richa/Videos/data')


# converter('C:/Users/richa/Videos/small.webm', 'C:/Users/richa/Videos/small.mp4')
# get_metadata('C:/Users/richa/Videos/small.mp4')



