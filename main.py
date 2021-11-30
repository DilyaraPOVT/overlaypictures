import glob
import os
import sys
import path as path
from PIL import Image
import PIL
import itertools as it
import pathlib
import inspect, os.path


def startRename(directory):
    directory1=directory.replace('/', '\\')
    files=sorted([path for path in os.listdir(directory) if os.path.isfile(directory+path)])
    i=1

    while files:
        file=files[0]
        ext=file.split('.')[-1]
        if not os.path.isfile(f'{directory}{i}.{ext}'):
            name = f'y_{i}.{ext}'
            os.rename(directory1+file, directory1+name)
            del files[0]
        i+=1


#path = "C:\\Users\\galya\\PycharmProjects\\overlaypictures\\1k\\"

def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)
for root, dirs, files in os.walk('.'):
   dirs[:]= [d for d in dirs if d[:4]!='main']
   for file in files:
      if file[-4:]=='.png':
        print (os.path.join(root, file))

path = get_script_dir()+"\\"
print(get_script_dir())


folderName = os.path.split(os.path.split(path)[0])[1]
alpha = 1
#startRename(path)

list_of_imgs = sorted(os.listdir(path))


lst = sorted(os.listdir(path))
if 'main.bat' in lst:
    lst.remove('main.bat')
if 'main.py' in lst:
    lst.remove('main.py')
if 'main.exe' in lst:
    lst.remove('main.exe')
print (lst)
for k,g in it.groupby(lst, key=lambda x: x.split('Base_')[0]):
    img = Image.open(path +'{}'.format(next(g)),'r')
    x, y = img.size
    g_list = list(g) 
    for i,item in enumerate(g_list):
        next_img = Image.open(path+'{}'.format(item))
        if i == 0:
            new_img = Image.alpha_composite(next_img,img) 
        else: 
            new_img = Image.alpha_composite(next_img,new_img) 
        next_img.paste(new_img, (x,y), mask=new_img)
new_img.save(path + 'Base_out.png', format='png')
for k,g in it.groupby(lst, key=lambda x: x.split('AORM_')[0]):
    img = Image.open(path +'{}'.format(next(g)),'r')
    x, y = img.size
    g_list = list(g)
    for i,item in enumerate(g_list):
        next_img = Image.open(path+'{}'.format(item))
        if i == 0:
            new_img = Image.alpha_composite(next_img,img)
        else:
            new_img = Image.alpha_composite(next_img,new_img)
        next_img.paste(new_img, (x,y), mask=new_img)
new_img.save(path +'AORM_out.png',format='png')
for k,g in it.groupby(lst, key=lambda x: x.split('Normal_')[0]):
    img = Image.open(path +'{}'.format(next(g)),'r')
    x, y = img.size
    g_list = list(g)
    for i,item in enumerate(g_list):
        next_img = Image.open(path+'{}'.format(item))
        if i == 0:
            new_img = Image.alpha_composite(next_img,img)
        else:
            new_img = Image.alpha_composite(next_img,new_img)
        next_img.paste(new_img, (x,y), mask=new_img)
new_img.save(path +'Normal_out.png',format='png')
print(folderName)
