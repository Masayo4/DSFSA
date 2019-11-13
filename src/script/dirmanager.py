import cv2
import os
import sys
import shutil
import datetime
from time import sleep

def sys_init():
    print("sysinit_function")
    dirpath = "../making_dataset/tempimg/"
    if os.path.exists(dirpath) == True:
        shutil.rmtree(dirpath)
    os.mkdir(dirpath)


def tempdir_cleaner():
    print("dir_cleaning")
    dirpath = "../making_dataset/tempimg/"
    shutil.rmtree(dirpath)
    os.mkdir(dirpath)

def processed_cleaner():
    print("dir_cleaning")
    dirpath = "processed/"
    shutil.rmtree(dirpath)

def processed_cleaner():
    print("dir_cleaning")
    dirpath = "../data/csv/"
    shutil.rmtree(dirpath)
    os.mkdir(dirpath)
