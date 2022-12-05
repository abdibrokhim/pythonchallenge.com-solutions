import requests
from PIL import Image
import re

# download image
with open("oxygen.png", 'wb') as f:
    f.write(requests.get("http://www.pythonchallenge.com/pc/def/oxygen.png").content)


im = Image.open("oxygen.png")

print(im.width, im.height)

# we will get (R, G, B, alpha) as a result
print(im.getpixel((0, 0)))

g_row = [im.getpixel((x, im.height / 2)) for x in range(im.width)]  # type: ignore

# remove duplicates
g_row = g_row[::7]
print(g_row)

# let's remove noises at the end
ords = [r for r, g, b, a in g_row if r == g == b]

# use ASCII table
print("".join(map(chr, ords)))

nums = re.findall(r"\d+", "".join(map(chr, ords)))
print(nums)

# print last word
print("".join(map(chr, map(int, nums))))