import os
import shutil 
import zipfile

source_dir = 'F:\\google photos'
destination_dir = 'F:\\GooglePhotosLinear'
folder_name = "temp"

#go to a designated directory
try:
    os.chdir(source_dir)
    print(f"Changed to {source_dir} directory.")
except OSError:
    print(f"Error: Could not change to {source_dir} directory.")

for root, dirs, files in os.walk(source_dir):
    for file in files:
        #create a temporary directory
        try:
            os.mkdir(folder_name)
            print(f"{folder_name} folder created.")
        except OSError:
            print(f"Error: {folder_name} folder not created.")

        if file.endswith(".zip"):
            #if zipped file unzip it to temp
             with zipfile.ZipFile(os.path.join(root, file), "r") as zip_ref:
                zip_ref.extractall(folder_name)
             
                #copy the jpegs to dest
             for root, dirs, pics in os.walk(folder_name):
                for pic in pics:
                    if pic.endswith(".jpeg") or pic.endswith(".jpg"):
                        shutil.copy(os.path.join(root, pic), destination_dir)
             print(f"{file} file processed.")
       
        #go to a designated directory
        try:
            os.chdir(source_dir)
            print(f"Changed to {source_dir} directory.")
        except OSError:
            print(f"Error: Could not change to {source_dir} directory.")
        #delete temporary directory
        try:
            shutil.rmtree(folder_name)
            print(f"{folder_name} folder deleted.")
        except OSError:
            print(f"Error: {folder_name} folder not deleted.")
        root=source_dir