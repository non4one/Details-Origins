import os
from PIL import Image



path = 'E:\meta test'
files = os.listdir(path)
i = 1

for file in files:
    file = path+ "/"+ file
  
    img = Image.open(file)
    exifdata = img._getexif()
    try:
        exif = exifdata[0x9003]
        print("Skiped this file because already has exifdata[0x9003]")
        
    except:
        gmt = os.path.getmtime(file)
        print(gmt)
        i += 1