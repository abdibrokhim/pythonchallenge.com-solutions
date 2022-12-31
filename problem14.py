from PIL import Image
import requests


# while downloading image we also specified the username and password
# cause after level 7 it requires authentication
# with open("wire.png", "wb") as f:
    # username = 'huge'
    # password = 'file'
    # url = 'http://www.pythonchallenge.com/pc/return/wire.png'
    # r = requests.get(url, auth=(username, password))  
    # f.write(r.content)


im = Image.open("wire.png")
print(im.size)
# it is 10000x1

# Based on all the clues, our assumption is to use the 10000 points from the given image, 
# create another image of 100*100, by walkingpython -c 'import PIL; print PIL.PILLOW_VERSION' around the square from outside to inside, 
# so we go right for 100 pixels, then down 99 pixels, then left 99 pixels, then up 98 pixels(clue 1).

# im = Image.open('wire.png')
delta = [(1,0), (0,1), (-1,0), (0,-1)]
out = Image.new('RGB', [100, 100])
x, y, p = -1, 0, 0
d = 200
while d / 2 > 0:
    for v in delta:
        steps = d // 2
        for s in range(steps):
            x, y = x + v[0], y + v[1]
            out.putpixel((x, y), im.getpixel((p,0)))
            p += 1
        d -= 1
out.save('p14.jpg')