import ffmpeg

video = ffmpeg.probe('C:\\Users\\richa\\Videos\\video.mp4')

print(video['streams'])