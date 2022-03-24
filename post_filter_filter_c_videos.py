from fileinput import filename
import os, shutil

basepath = 'Files\\Jigar\\videos\\'
try: os.mkdir(basepath + "compressed_videos")
except: pass


for file_name in os.listdir(basepath):
    if "_compressed" in file_name and file_name.endswith(".mp4"):
        shutil.move(basepath + file_name, basepath + "compressed_videos")
        #os.rename(basepath + "compressed_videos" + file_name, basepath + "compressed_videos" + file_name.replace("_compressed", ""))