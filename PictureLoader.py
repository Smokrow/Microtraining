# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 09:46:39 2018

@author: melnicenko
"""

import argparse
import numpy as np
import glob
import os
import cv2 as cv


class PictureLoader:

    def __init__(self):
        # ./fokus-1' Folder
        self.list1 = []
        self.pix_data_1 = None
        # ./fokus+2 Folder
        self.list2 = []
        self.pix_data_2 = None

    def LoadPictures(self):
        """
        Loads pictures from both folders (fokus-1 and fokus+2) and returns two
        numpy arrays containing pixeldata.
        Return data format: [number_of_pictures, resolution_x, resolution_y]
        """
        paths = ['./fokus-1', './fokus+2']
        for arg in paths:
            #parser = argparse.ArgumentParser(description='Loading image data')
            #parser.add_argument("-i","--input", default=arg, help="Input directory")
            #_args = parser.parse_args()
            #path = _args.input
            print(arg)
            path = arg
            picture_counter = 0
            print('Loading from folder: ', arg)
            for infile in glob.glob(os.path.join(path, '*.*')):
                img = cv.imread(infile, 1)
                img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                # load data from folder ./fokus-1
                if arg == paths[0]:
                    # add pixel data from pictures to a python list
                    # (faster than adding it to a numpy array)
                    self.list1.append(img_gray.tolist())
                    if picture_counter % 1999 == 0 and picture_counter > 0:
                        # convert python list to a numpy array
                        self.pix_data_1 = np.asarray(self.list1)
                        print('fokus-1 data shape: ', self.pix_data_1.shape)

                # load data from folder ./fokus+2
                if arg == paths[1]:
                    # add pixel data from pictures to a python list
                    # (faster than adding it to a numpy array)
                    self.list2.append(img_gray.tolist())
                    if picture_counter % 1999 == 0 and picture_counter > 0:
                        # convert python list to a numpy array
                        self.pix_data_2 = np.asarray(self.list2)
                        print('fokus+2 data shape: ', self.pix_data_2.shape)
                # print feedback after every 100th picture was loaded
                if picture_counter % 100 == 0:
                    print(infile, ' loaded')
                picture_counter = picture_counter + 1

        return self.pix_data_1, self.pix_data_2



# Testing PictureLoader
if __name__ == '__main__':
    PLoader = PictureLoader()
