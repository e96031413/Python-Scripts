import os
import glob
from pydub import AudioSegment
 
wenjianjia = []
path = input('請輸入要轉成.mp3的資料夾路徑：')
for root, dirs, files in os.walk(path): 
    wenjianjia.append(root)
wjj = wenjianjia
 
for dir in wjj:
    video_dir = dir
    extension_list = ('*.mp4', '*.flv',')
    i=1
 
    os.chdir(video_dir)
    for extension in extension_list:
        for video in glob.glob(extension):
            mp3_filename = os.path.splitext(os.path.basename(video))[0] + '.mp3'
            AudioSegment.from_file(video).export(mp3_filename, format='mp3')
            print('已轉換', str(i) ,'個影片！')
            i += 1
             
    for infile in glob.glob(os.path.join(video_dir, '*.mp4')):
        os.remove(infile)