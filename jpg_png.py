import sys, os
from PIL import Image

# Grab the first and second argument
arguments = sys.argv
image_folder = arguments[1]
output_folder = arguments[2]
path = f"{output_folder}"

# Check if new/ exists, if not create it
if not os.path.isdir(path):
    os.mkdir(path)


# Loop through images, 
for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}\\{filename}")
    clean_name = os.path.splitext(filename)[0]
    img.save(f"{output_folder}\\{clean_name}.png", "png")
    print("All Done")
    