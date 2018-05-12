def chop(c):
    del c[-1]
    del c[0]

letters = ["a", "b", "c", "d", "e", "f"]
chop(letters)
print(letters)