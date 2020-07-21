import ffmpeg
from pprint import pprint

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

converter('C:/Users/richa/Videos/small.webm', 'C:/Users/richa/Videos/small.mp4')
get_metadata('C:/Users/richa/Videos/small.mp4')

