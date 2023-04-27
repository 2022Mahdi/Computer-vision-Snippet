import os
from PIL import Image

def convert_to_yolo_format(input_labels_dir, output_labels_dir, images_dir):
    for label_file in os.listdir(input_labels_dir):
        input_file_path = os.path.join(input_labels_dir, label_file)
        output_file_path = os.path.join(output_labels_dir, label_file)
        image_file_path = os.path.join(images_dir, label_file.replace('.txt', '.jpg'))

        # Get image dimensions
        img = Image.open(image_file_path)
        image_width, image_height = img.size

        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
            for line in input_file:
                class_name, left, top, right, bottom = line.strip().split()

                # Convert the coordinates to YOLO format
                x_center = (float(left) + float(right)) / (2 * image_width)
                y_center = (float(top) + float(bottom)) / (2 * image_height)
                width = (float(right) - float(left)) / image_width
                height = (float(bottom) - float(top)) / image_height

                # Assuming you have a dictionary to map class names to class IDs
                class_id = class_name_to_id[class_name]

                output_file.write(f"{class_id} {x_center} {y_center} {width} {height}\n")

# Example usage
input_labels_dir = "path/to/input/labels"
output_labels_dir = "path/to/output/labels"
images_dir = "path/to/images"

# Define the class_name_to_id dictionary
class_name_to_id = {
    "class1": 0,
    "class2": 1,
    # Add more classes as needed
}

convert_to_yolo_format(input_labels_dir, output_labels_dir, images_dir)
