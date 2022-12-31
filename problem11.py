import requests
from PIL import Image

im = Image.open("cave.jpg")

(w, h) = im.size

even = Image.new("RGB", (w // 2, h // 2))
odd = Image.new("RGB", (w // 2, h // 2))

# loop through the image and split it into two images
for i in range(w):
    for j in range(h):
        # result (R, G, B, alpha)
        p = im.getpixel((i, j))
        if (i + j) % 2 == 0:
            even.putpixel((i // 2, j // 2), p)
        else:
            odd.putpixel((i // 2, j // 2), p)

# save the images
even.save("even.jpg")
odd.save("odd.jpg")


