
# f=open("odd.txt","w")
# num1=int(input("Enter the value of num1:"))
# if(num1%2)==0:
#     f.write("{0} is Even number".format(num1))
# else:
#     f.write("{0} is Odd number".format(num1))

#     f.close()


f=open("add.txt","w")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
add=a+b
f.write(f'Addition of two number is {add}')
f.close()