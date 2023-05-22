from PIL import Image, ImageFilter

img = Image.open("./images/astro.jpg")
# filtered_img = img.convert("L")
# crooked = filtered_img.rotate(90)


# crooked.save("gray.png", "png")

# crooked.show() # show the image

# resized_img = img.resize((650, 650))
img.thumbnail((400, 400)) # maintains the aspect ratio
img.save("new-img.png", "png")
