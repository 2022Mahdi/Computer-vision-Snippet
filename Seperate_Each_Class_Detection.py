import os
import shutil


labels = 'labels/'
images = 'images/'
os.makedirs("classes",exist_ok = True)
def Classes():
    "Find class names"
    with open('classes.txt','r') as f:
        classes = f.read().split()
        f.close()
    for cls in classes:
                os.makedirs("classes/" + cls,exist_ok = True)
    return classes


def Find(pathlabel,pathimage,classes):
    
    "copy  & remove each file at own folder"

    with open(pathlabel,'r') as f:
            predicted = f.read().split()
            index = int(predicted[0])
            f.close()
    
    shutil.copy(pathlabel,f'{"classes/" + classes[index]}/')
    os.remove(pathlabel)
    
    if os.path.exists(pathimage):
        
        shutil.copy(pathimage,f'{"classes/" + classes[index]}/')
        os.remove(pathimage)

    else:
        shutil.copy(pathimage.replace("jpeg","jpg"),f'{"classes/" + classes[index]}/')
        os.remove(pathimage.replace("jpeg","jpg"))


                            
                            
    
for label in os.listdir(labels):
    
    classes = Classes()
    pathlabel = "labels/" + label
    pathimage = "images/" + label.replace("txt","jpeg")
    Find(pathlabel,pathimage,classes)
    print(label)

os.rmdir("labels/")
shutil.move("images/","classes/background")
