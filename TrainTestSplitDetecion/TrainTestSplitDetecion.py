import os
import shutil
from tqdm import tqdm

def split_images_and_labels(threshold):
    """
    This function splits the images and labels into training and validation sets.
    It moves the validation images and labels to separate folders.
    """
    counter = 0
    split_threshold = len(os.listdir('images/')) * threshold

    # Create directories for validation and training sets
    os.makedirs('val_images', exist_ok=True)
    os.makedirs('val_labels', exist_ok=True)
    os.makedirs('val', exist_ok=True)
    os.makedirs('train', exist_ok=True)

    # Iterate through the images directory
    for image_file in tqdm(os.listdir("images/")):
        if counter < int(split_threshold):
            image_path = "images/" + image_file
            label_path = "labels/" + image_file[:-3] + "txt"

            # Check if both image and label exist
            if os.path.exists(image_path) and os.path.exists(label_path):
                counter += 1

                # Copy image and label to validation folders
                shutil.copy(image_path, "val_images/")
                shutil.copy(label_path, "val_labels/")

                #print(counter)

                # Remove the original image and label
                os.remove(image_path)
                os.remove(label_path)

# Get threshold value as input
threshold = float(input("Enter the Split rate for validation value (e.g., 0.4): "))

# Call the function with the input threshold value
split_images_and_labels(threshold)
