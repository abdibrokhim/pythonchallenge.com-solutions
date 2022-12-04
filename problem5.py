from bs4 import BeautifulSoup
import requests
import pickle
from urllib.request import urlopen

# Get the HTML from the URL
r = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")
html = r.text

# Parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Get the text from the HTML
text = soup.get_text()

text = text.replace("\n", "")
print(text)

# Decode the text
d = pickle.loads(urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read())
print(d)

# Loop through the data
for i in d:
    for j in i:
        print(j[0] * j[1], end="")
    print()