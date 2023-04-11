import os
import shutil

# To avoid path issues,both image and labels folder must be located in current working directory

#here is an example:

#COCO2017/
#├── cococustom.py
#├── images/
#└── labels/

#2 directories, 1 file


names =["person",
        "bicycle",
        "car",
        "motorcycle",
        "airplane",
        "bus",
        "train",
        "truck",
        "boat",
        "traffic light",
        "fire hydrant",
        "stop sign",
        "parking meter",
        "bench",
        "bird",
        "cat",
        "dog",
        "horse",
        "sheep",
        "cow",
        "elephant",
        "bear",
        "zebra",
        "giraffe",
        "backpack",
        "umbrella",
        "handbag",
        "tie",
        "suitcase",
        "frisbee",
        "skis",
        "snowboard",
        "sports ball",
        "kite",
        "baseball bat",
        "baseball glove",
        "skateboard",
        "surfboard",
        "tennis racket",
        "bottle",
        "wine glass",
        "cup",
        "fork",
        "knife",
        "spoon",
        "bowl",
        "banana",
        "apple",
        "sandwich",
        "orange",
        "broccoli",
        "carrot",
        "hot dog",
        "pizza",
        "donut",
        "cake",
        "chair",
        "couch",
        "potted plant",
        "bed",
        "dining table",
        "toilet",
        "tv",
        "laptop",
        "mouse",
        "remote",
        "keyboard",
        "cell phone",
        "microwave",
        "oven",
        "toaster",
        "sink",
        "refrigerator",
        "book",
        "clock",
        "vase",
        "scissors",
        "teddy bear",
        "hair drier",
        "toothbrush"]
        
        
        
for index,name in enumerate(names):
    print(index," ==> ",name)

print()
iclasses = input("Enter class numbers that you would like to save (or press e for an example): ")

if iclasses == "e" or iclasses == "E":
    print(iclasses)
    print("imagine Label would like to save class human and car (seperate class numbers by space) ==> Label will enter:0 2 ==> then press enter")
    print()
    iclasses = input("Enter class numbers that you would like to save (or press e for an example): ")

iclasses = iclasses.split()
print(iclasses)



LabelsDir = 'labels/'
ImagesDir = 'images/'

os.makedirs('CustomDataset',exist_ok = True)
os.makedirs('CustomDataset/labels',exist_ok = True)
os.makedirs('CustomDataset/images',exist_ok = True)

def CheckExist(Path):
    with open(Path,'r') as f:
            Found = []
            lines=[line.rstrip() for line in f]
            for Line in lines:
                CLS = Line.split()
                for _ in iclasses:
                    if CLS[0] == _:
                        Found.append(Line)
    return Found



progress = len(os.listdir(LabelsDir))
counter = 1

for Label in os.listdir(LabelsDir):

    print(f"{counter} / {progress}")
    counter += 1
    Path = LabelsDir + Label
    Founded = CheckExist(Path)
    if Founded: 
        wr = open(f'CustomDataset/labels/{Label}','w')
        wr.writelines(Founded)
        wr.close()
        ImageDir = "images/" + Label.replace("txt","jpg")
        shutil.copy(ImageDir,'CustomDataset/images/')
    
print()
print()
print(f"{len(os.listdir('CustomDataset/images'))} saved in CustomDataset Folder")
