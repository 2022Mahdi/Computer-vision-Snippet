import os
from PIL import Image

# Create the Half directory if it doesn't exist
if not os.path.exists("Half"):
    os.makedirs("Half")

# Ask the user for the split direction
direction = input("Enter the split direction (horizontal or vertical): ").lower()

# Iterate through all files in the images folder
for filename in os.listdir("images"):
    # Check if the file is an image
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
        # Open the image
        img = Image.open(os.path.join("images", filename))

        # Calculate the split position
        if direction == "horizontal":
            split_position = img.width // 2
        elif direction == "vertical":
            split_position = img.height // 2
        else:
            print("Invalid direction. Please enter 'horizontal' or 'vertical'.")
            break

        # Split the image
        if direction == "horizontal":
            img1 = img.crop((0, 0, split_position, img.height))
            img2 = img.crop((split_position, 0, img.width, img.height))
        else:
            img1 = img.crop((0, 0, img.width, split_position))
            img2 = img.crop((0, split_position, img.width, img.height))

        # Save the two halves in the Half directory
        img1.save(os.path.join("Half", f"{filename}_half1.png"))
        img2.save(os.path.join("Half", f"{filename}_half2.png"))

        print(f"Processed {filename}")
