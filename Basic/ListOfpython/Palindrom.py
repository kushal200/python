num=int(input("Enter number:"))
temp=num
a=0
while(num>0):
 rem=num%10
 a=a*10+rem
 num=num//10
if(temp==a):
 print(a," is a palindrome.")
else:
 print(a," is not a palindrome.")