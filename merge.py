import os
import shutil

dest_dir = './train/'

def copy_files(d):
    for (dirpath, dirname, filenames) in os.walk(d):
        dirname = dirpath[2:-1]
        for filename in filenames:
            if filename.split('.')[1] != 'txt':
                src = dirpath + filename
                dst = dest_dir + dirname + '_' + filename
                shutil.copy(src, dst)
                src = dirpath + filename.split('.')[0] + '.txt'
                dst = dest_dir + dirname + '_' + filename.split('.')[0] + '.txt'
                shutil.copy(src, dst)

dirs = ['./keshavarzi/', './mellat/', './melly/', './refah/', './saderat/', './saman/', './tejarat/']
for d in dirs:
    copy_files(d)