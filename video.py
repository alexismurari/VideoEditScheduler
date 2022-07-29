import moviepy.editor as mp
from os import listdir
from os.path import isfile, join

new_videos_path = "new/"

new_videos = [f for f in listdir(new_videos_path) if isfile(join(new_videos_path, f))]

print(new_videos)

for vid in new_videos:

    video = mp.VideoFileClip("new/" + vid)
    video = video.resize(height=1920)
    video = video.crop(x1=1166.6,y1=0,x2=2246.6,y2=1920)

    start = vid[1:3]
    end = vid[4:6]

    if end == "30":
        print("No end")
        end = None

    video = video.subclip(start, end)
    video.write_videofile("edit/" + vid[6:])