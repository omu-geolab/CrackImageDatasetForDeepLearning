from logging import root
import shutil
import os
import glob

rootpath = r"D:\komi\YOLOR\datasets\originaldata\Kishiwada\annotation/"
txt_path = r"D:\komi\YOLOR\datasets\originaldata\Kishiwada\cracklabels/*"
jpg_path = rootpath + "*.JPG"

for txt_file in glob.glob(txt_path):
    txtname_without_ext = os.path.splitext(os.path.basename(txt_file))[0]
    for jpg_file in glob.glob(jpg_path):
        jpgname_without_ext = os.path.splitext(os.path.basename(jpg_file))[0]
        if jpgname_without_ext == txtname_without_ext :
            shutil.copy(jpg_file,"D:\komi\YOLOR\datasets\originaldata\Kishiwada\cracklabels")

print("Done!")