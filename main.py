from os import walk
from exif import Image

folder_path = "./photos"
files = []

def getFullPath(filename):
    return f"{folder_path}/{filename}"

# get all filenames in source directory
for (dirpath, dirnames, filenames) in walk(folder_path):
    files.extend(filenames)
    break

# iterate over every image
for filename in files:
    # read date from filename
    parts = filename.split("-")
    year = parts[1]
    month = parts[2]
    day = parts[3]
    datestring = f"{year}:{month}:{day} 12:00:00"
    
    print("writing exif to file ",filename)

    # open image with exif data
    with open(getFullPath(filename), 'rb') as image_file:
        img = Image(image_file)

    # write date tag
    img.set('datetime_original', datestring)

    # save image
    with open(getFullPath(filename), 'wb') as new_image_file:
        new_image_file.write(img.get_file())
