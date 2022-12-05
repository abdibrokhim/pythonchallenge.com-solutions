# a = [1, 11, 21, 1211, 111221, ... ]


def A005150(n):
    p = "1"
    seq = ["1"]
    while (n > 1):
        q = ''
        idx = 0 # Index
        l = len(p) # Length
        while idx < l:
            start = idx
            idx = idx + 1
            while idx < l and p[idx] == p[start]:
                idx = idx + 1
            q = q + str(idx-start) + p[start]
        n, p = n - 1, q
        seq.append(p)
    return seq

a = A005150(31)
print(a)

print(len(a[30]))


# Tap the link below to learn more about the integer sequences
# https://oeis.org/A005150