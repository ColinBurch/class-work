largest = None
smallest = None
total = 0
while True:
    answer = input("Enter a number: ")
    if answer == "done" :
        break
    try:
        num = float(answer)
    except:
        print("Incorrect input")
        continue
    if smallest is None or num < smallest:
            smallest = num
    if largest is None or num > largest:
            largest = num
print("Maximum is", largest)
print("Minimum is", smallest)    