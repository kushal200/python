num = [3, 4, 5, 7, 8]

number = int(input("Enter any number: "))
print("list: " + str(num))

count = 0
for i in num:
    if i > number:
        count += 1

print("numbers greater than {0} are : {1}".format(str(number), str(count)))
