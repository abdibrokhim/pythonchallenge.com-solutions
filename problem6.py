import zipfile
import re
import os


# unzip the file
with zipfile.ZipFile("channel.zip", 'r') as zip_ref:
    zip_ref.extractall("channel")

# open the readme file
with open("channel/readme.txt", 'r') as f:
    print(f.read())

comments = []
def main(dir: str, number: list):
    while number:
        try:
            # open the file
            with open(dir + "/" + number[0] + ".txt", 'r') as f:
                # read the file
                text = f.read()

                # collect comments
                comments.append(zipfile.ZipFile("channel.zip").getinfo(number[0] + ".txt").comment.decode("utf-8"))
                # print(comments, end="")

                # write to file
                try:
                    with open("comments.txt", 'a') as f:
                        f.write(text + "\n")
                except:
                    pass

                # get the number from the text
                number = re.findall(r'\d+', text)

                if number:
                    # print the number
                    print(number[0])

        except FileNotFoundError as e:
            print(e)
            return

# call the main function
main("channel", ["90052"])

# print the comments
print("".join(comments))


# find length of channel.zip (interesting)
c=0
for i in os.listdir("channel"):
    j = i.split(".")
    c+=1
    # print(i)

print(c)
