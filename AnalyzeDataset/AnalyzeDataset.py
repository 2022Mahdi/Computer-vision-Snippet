import os
from collections import Counter
import matplotlib.pyplot as plt
from tqdm import tqdm

# Read all labels in the label folder
label_folder = "labels"
label_files = [os.path.join(label_folder, f) for f in os.listdir(label_folder) if os.path.isfile(os.path.join(label_folder, f))]

# Gather all unique classes and their counts
class_counts = Counter()
for label_file in tqdm(label_files):
    if label_file.endswith('classes.txt'):
    	pass
    else:
    	with open(label_file, 'r') as f:
        	for line in f:
            		class_number = int((line.split())[0])
            		class_counts[class_number] += 1

# Plot the number of instances per class
classes, counts = zip(*class_counts.items())
plt.bar(classes, counts)
plt.xlabel('Class')
plt.ylabel('Number of Instances')
plt.title('Number of Instances per Class')
plt.xticks(classes)  # Set the x-axis tick labels explicitly
plt.show()
