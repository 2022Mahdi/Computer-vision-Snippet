# pip install pyheif pillow

import os
import pyheif
from PIL import Image

def convert_heic_to_jpg(heic_folder, jpg_folder):
    for filename in os.listdir(heic_folder):
        if filename.endswith(".HEIC"):
            heif_file = pyheif.read(os.path.join(heic_folder, filename))
            image = Image.frombytes(
                heif_file.mode, 
                heif_file.size, 
                heif_file.data,
                "raw",
                heif_file.mode,
                heif_file.stride,
            )
            image.save(os.path.join(jpg_folder, filename.replace(".HEIC", ".jpg")), format="JPEG")
            print(f"{filename} Succesfully Convert.")

convert_heic_to_jpg("heic_folder", "jpg_folder_destination")
