filename = input('Enter the file name: ')
fhand = open(filename)
for line in fhand:
    singleline = line.strip()
    print(singleline.upper())