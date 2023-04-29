import json
from PIL import Image
import os

def sanitize_filename(filename):
    return filename

def odgt_to_yolo(odgt_file, output_folder, class_id, img_folder):
    with open(odgt_file, 'r') as infile:
        for line in infile:
            data = json.loads(line)
            image_id = data['ID']
            sanitized_image_id = sanitize_filename(image_id)
            gtboxes = data['gtboxes']

            img_path = f"{img_folder}/{image_id}.jpg"
            img = Image.open(img_path)
            img_width, img_height = img.size

            yolo_annotations = []
            for gtbox in gtboxes:
                if gtbox['tag'] == 'person':
                    vbox = gtbox['vbox']
                    x, y, w, h = vbox
                    center_x = (x + w / 2) / img_width
                    center_y = (y + h / 2) / img_height
                    norm_w = w / img_width
                    norm_h = h / img_height
                    yolo_annotation = f"{class_id} {center_x} {center_y} {norm_w} {norm_h}"
                    yolo_annotations.append(yolo_annotation)

            output_file = f"{output_folder}/{os.path.splitext(sanitized_image_id)}.txt"
            with open(output_file, 'w') as outfile:
                outfile.write("\n".join(yolo_annotations))


odgt_file = "annotation_train.odgt"
output_folder = "train/labels"
class_id = 0  # Assuming 'person' class has an ID of 0
img_folder = "train/Images"
odgt_to_yolo(odgt_file, output_folder, class_id, img_folder)

#*******************************************************************************
#Either execute the command below using the command line or remove the comment from the line below
#cmd = "rename "s/\('(.*)', ''\)/\$1/" *"
#os.system(cmd)
