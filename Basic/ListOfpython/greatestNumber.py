a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))
c=int(input("Enter the Third Number:"))
if a>b>c:
    print("%d is a Greatest Number" %a)
elif b>a>c:
    print("%d is a Greatest Number" %b)
else:
    print("%d is a Greatest Number" %c)