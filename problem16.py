import requests
from PIL import Image, ImageChops


def download_image():
    with open('mozart.gif', 'wb') as f:
        username = 'huge'
        password = 'file'
        url = 'http://www.pythonchallenge.com/pc/return/mozart.gif'
        r = requests.get(url, auth=(username, password))
        f.write(r.content)


def main():
    image = Image.open("mozart.gif")

    for y in range(image.size[1]):
        box = 0, y, image.size[0], y + 1
        
        row = image.crop(box)
        bytes = row.tobytes()
        i = bytes.index(195)
        
        row = ImageChops.offset(row, -i)
        
        image.paste(row, box)

    image.save("p16.gif")


if __name__ == '__main__':
    # download_image()
    main()
