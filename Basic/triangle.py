a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
s=(a+b+c)/2
print("s=",s)
Area_Of_Triangle=(s*(s-a)*(s-b)*(s-c))-0.5
print("The area of taingle is :%0.2f" %Area_Of_Triangle)