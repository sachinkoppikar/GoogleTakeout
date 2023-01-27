import os
import shutil
from datetime import datetime
from PIL import Image

src_dir = 'F:\\GooglePhotosLinear'

for filename in os.listdir(src_dir):
    if filename.endswith('.jpeg') or filename.endswith(".jpg"):
        file_path = os.path.join(src_dir, filename)
        with Image.open(file_path) as img:
            exif_data = img._getexif()
            if exif_data:
                date_taken = exif_data.get(36867)
                if date_taken:
                    try:
                        date_taken = datetime.strptime(date_taken, '%Y:%m:%d %H:%M:%S')
                    except OSError:
                        print(f"Error: Could not get dateTaken for {file_path}.")
                       
                    month_year = date_taken.strftime('%Y-%m')
                    dst_dir = os.path.join(src_dir, month_year)
                    if not os.path.exists(dst_dir):
                        os.makedirs(dst_dir)
                   
                    img.close()
                    shutil.move(file_path, dst_dir)
