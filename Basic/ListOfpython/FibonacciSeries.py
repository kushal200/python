num = int(input("Enter the terms : "))
first=0
second=1
if num<=0:
 print("The requested series is",first)
else:
 print(first,second,end=" ")
 for x in range(2,num):
    next=first + second
 print(next,end=" ")
 first = second
 second = next