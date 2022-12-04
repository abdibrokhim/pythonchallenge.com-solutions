string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def main(s: str) -> str:
    new_s = ""
    for i in s:
        if i == "y":
            new_s += "a"
        elif i == "z":
            new_s += "b"
        elif ord(i) >= 97 and ord(i) <= 120:
            new_s += chr(ord(i) + 2)
        else:
            new_s += i
    return new_s

print(main(string))

print("\n")

# with built-in methods
def main1(s: str) -> str:
    l = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
    return s.translate(l)

print(main1(string))

print("\n")

# now apply to url
print(main("map"))

