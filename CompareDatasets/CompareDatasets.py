import os
import hashlib
from pathlib import Path
from shutil import copy2

def get_image_files(folder):
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')
    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(image_extensions):
                yield os.path.join(root, file)

def get_file_hash(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
        return hashlib.md5(file_data).hexdigest()

def main(src_folder, des_folder):
    src_hashes = set()
    
    for image_file in get_image_files(src_folder):
        file_hash = get_file_hash(image_file)
        src_hashes.add(file_hash)
    
    for image_file in get_image_files(des_folder):
        file_hash = get_file_hash(image_file)
        if file_hash in src_hashes:
            #os.remove(image_file)
            print(f"Deleted {image_file}")

if __name__ == "__main__":
    src_folder = input("Enter the source folder path: ")
    des_folder = input("Enter the destination folder path: ")
    main(src_folder, des_folder)
