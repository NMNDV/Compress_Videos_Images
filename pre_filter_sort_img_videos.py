from fileinput import filename
import os, shutil

basepath = 'Files\\Jigar\\'
try: os.mkdir(basepath + "videos")
except: pass
try: os.mkdir(basepath + "photos")
except: pass


for file_name in os.listdir(basepath):
    if file_name.endswith(".mp4") or file_name.endswith(".MOV"):
        shutil.move(basepath + file_name, basepath + "videos")
    elif file_name.endswith(".jpg") or file_name.endswith(".HEIC"):
        shutil.move(basepath + file_name, basepath + "photos")