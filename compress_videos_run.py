from fileinput import filename
import os
import shutil
from compressor import c1, c2
basepath = "D:\\temp\\Files\\Jigar\\videos\\"
try: 
    os.mkdir(basepath + "compressedv")
except:
    pass
# os.mkdir(basepath + "b")
# os.mkdir(basepath + "c")

def proc11(x, f):
    if f == 1:
        return int(x*0.40//1024)
    if f == 2:
        return int(x*0.30//1024)
    return int(x*0.20//1024)

for file_name in os.listdir(basepath):
    if not file_name.endswith('.mp4') and not file_name.endswith('.MOV'):
        continue
    size = os.path.getsize(basepath + file_name)
    print(file_name, size)
    try:
    # continue
        if size < 50:
            c2(basepath + file_name, proc11(size, 1), filename_suffix="_compressed")
            # shutil.move(basepath + file_name, basepath + "a\\")
        elif size < 100:
            c2(basepath + file_name, proc11(size, 2), filename_suffix="_compressed")
            # shutil.move(basepath + file_name, basepath + "b\\")
        else:
            c2(basepath + file_name, proc11(size, 3), filename_suffix="_compressed")
            # shutil.move(basepath + file_name, basepath + "c\\")
        # shutil.move(basepath + "*.".join(filename.split(".")), basepath + "compressedv")
    except:
        print("Could not process: ", file_name, )
    

