import os, shutil
from PIL import Image

basepath = 'Files\\Umang\\photos\\'
try: os.mkdir(basepath + "done")
except: pass
try: os.mkdir(basepath + "compressed")
except: pass
quality = 60

for file_name in os.listdir(basepath):
    if not file_name.endswith(".jpg") and not file_name.endswith(".JPG"):
        continue
    picture = Image.open(basepath + file_name)
    picture.save(basepath + "compressed\\" + file_name,optimize=True,quality=50)
    shutil.move(basepath + file_name, basepath + "done")
