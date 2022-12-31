import requests

# tap below to download .gfx file
# http://www.pythonchallenge.com/pc/return/evil2.gfx


def main():
    with open("evil2.gfx", "rb") as f:
        data = f.read()

    for i in range(5):
        with open(f"evil2_{i}.jpg", "wb") as f:
            f.write(data[i::5])

main()

