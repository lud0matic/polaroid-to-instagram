from PIL import Image, ImageFilter
import argparse, os, random, string

# Instagram Aspect Ratio
VERTICAL_4_5 = (1080, 1350)
SQUARE = (1080, 1080)

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("file", action="store", help="path of picture to transform")
parser.add_argument("-nb", "--no-blur", action="store_true", dest="no_blur", default=False, help="blur background disable | default: Enable")
parser.add_argument("-sq","--square", action="store_true",dest="square",default=False, help="1:1 aspect ratio | default: 4:5 aspect ratio")
args = parser.parse_args()
no_blur = args.no_blur
square = args.square

FILE_NAME, FILE_EXTENTION = os.path.splitext(args.file)
RANDOM_STRING = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
FILE_EXPORT_NAME = FILE_NAME + "_" + RANDOM_STRING + FILE_EXTENTION

# Open File
def original_photo():     
      original_photo = Image.open(args.file)
      return original_photo      

# New blank image with 1:1 or 4:5 aspect ratio
def blank_image():
      if args.square == True:
            blank_image = Image.new("RGB", SQUARE, color=0)
            blank_image.paste(original_photo(),(-342,-282))    
            return blank_image
      else:
            blank_image = Image.new("RGB",VERTICAL_4_5, color=0)
            blank_image.paste(original_photo(),(-342,-219))
            return blank_image

def original_photo_resize():
      image_resize = original_photo().resize((741, 900), Image.Resampling.LANCZOS)
      return image_resize

# Blur background
def blur_backgroud(image_to_blur):
      image_blur = image_to_blur.filter(ImageFilter.GaussianBlur(12))
      return image_blur

# All possible outcomes
def blur_45():  
      try:
            blur = blur_backgroud(blank_image()).copy()
            blur.paste(original_photo_resize(),(170,227))
            blur.save(FILE_EXPORT_NAME)
            print(f"Image save: {FILE_EXPORT_NAME}")
      except Exception:
            print("Error: Check the file/directory path and try again")

def no_blur_45():
      try:
            no_blur = blank_image().copy()
            no_blur.paste(original_photo_resize(),(170, 227))
            no_blur.save(FILE_EXPORT_NAME)
            print(f"Image save: {FILE_EXPORT_NAME}")
      except Exception:
            print("Error: Check the file/directory path and try again")

def blur_11():
      try:
            blur = blur_backgroud(blank_image()).copy()
            blur.paste(original_photo_resize(),(170, 90))
            blur.save(FILE_EXPORT_NAME)
            print(f"Image save: {FILE_EXPORT_NAME}")
      except Exception:
            print("Error: Check the file/directory path and try again")

def no_blur_11():
      try:
            no_blur = blank_image().copy()
            no_blur.paste(original_photo_resize(),(170, 90))
            no_blur.save(FILE_EXPORT_NAME)
            print(f"Image save: {FILE_EXPORT_NAME}")
      except Exception:
            print("Error: Check the file/directory path and try again")

if __name__ == "__main__":
      if square == True and no_blur == True:
            no_blur_11()
      elif square == True:
            blur_11()
      elif no_blur == True:
            no_blur_45()
      else:
            blur_45()
