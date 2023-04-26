import os
import shutil

labels = 'labels/'
images = 'images/'
os.makedirs("classes", exist_ok=True)

def Classes():
    """
    Find class names from a text file and create corresponding directories.
    
    Returns:
        list: A list of class names.
    """
    with open('classes.txt', 'r') as f:
        classes = f.read().split()
        f.close()

    # Create directories for each class
    for cls in classes:
        os.makedirs("classes/" + cls, exist_ok=True)

    return classes

def Find(pathlabel, pathimage, classes):
    """
    Copy and remove each file to its own folder based on the class index.
    
    Args:
        pathlabel (str): Path to the label file.
        pathimage (str): Path to the image file.
        classes (list): List of class names.
    """
    with open(pathlabel, 'r') as f:
        predicted = f.read().split()
        index = int(predicted)
        f.close()

    # Copy and remove label file
    shutil.copy(pathlabel, f'{"classes/" + classes[index]}/')
    os.remove(pathlabel)

    # Copy and remove image file
    if os.path.exists(pathimage):
        shutil.copy(pathimage, f'{"classes/" + classes[index]}/')
        os.remove(pathimage)
    else:
        shutil.copy(pathimage.replace("jpeg", "jpg"), f'{"classes/" + classes[index]}/')
        os.remove(pathimage.replace("jpeg", "jpg"))
