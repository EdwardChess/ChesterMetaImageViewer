# coding=utf-8

import sys, argparse
from PIL import Image
from PIL.ExifTags import TAGS
from termcolor import colored

def get_data(exif,field):
    for (k,v) in exif.items():
        if field.lower() == 'all':
            print(colored(TAGS.get(k) + ": ", 'cyan'),colored(v, 'green'))
        elif TAGS.get(k) == field:
            print(colored(TAGS.get(k) + ": ", 'cyan'),colored(v, 'green'))
            break

parser = argparse.ArgumentParser(description='Get metadata from photo')
parser.add_argument('-i','--image', help='Path to image', required=True)
parser.add_argument('-p','--parameter', help='Use one parameter or type \'all\'', required=True)
args = vars(parser.parse_args())

if args['image'] and args['parameter']:
    image = args['image']
    param = args['parameter']
    try:
        image = Image.open(args['image'])._getexif()
        error = False
        if image != None:
            for (k,v) in image.items():
                if TAGS.get(k) == param or param.lower() == 'all':
                    error = False
                    break
                else:
                    error = True
            if error:
                print(colored("[Error] Parameter not found", 'red'))
            else:
                get_data(image,param)
        else:
            print(colored("[Error] Metadata not found...", 'red'))
    except:
        print(colored("[Error] Can\'t open image", 'red'))
