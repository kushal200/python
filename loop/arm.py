num=int(input("Enter the number:"))
temp=0
sum=num
while num>0:
    rem=num%10
    temp=temp+10**3
    sum=sum//10
if temp==num:
    print(num, "It is armstrong number.")
else:
    print(num, "It is not armstrong number.")