from PIL import Image, ImageFilter

img = Image.open("./images/pikachu.jpg")
filtered_img = img.convert("L")
crooked = filtered_img.rotate(90)
crooked.save("gray.png", "png")

crooked.show() # show the image
