from bs4 import BeautifulSoup
import requests
import re

# Get the HTML from the URL
r = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579")
html = r.text

# Parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Get the text from the HTML
text = soup.get_text()

# Get the number from the text
number = re.findall(r'\d+', text)

# Loop through the numbers
while number:
    # Get the HTML from the URL
    r = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + number[0])
    html = r.text

    # Parse the HTML
    soup = BeautifulSoup(html, "html.parser")

    # Get the text from the HTML
    text = soup.get_text()

    # Get the number from the text
    number = re.findall(r'\d+', text)

    # Print the number
    print(number[0])

# Print the text
# print(text)