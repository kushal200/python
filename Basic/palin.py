num=int(input("Enter the number:"))
temp=num
numbers=0
while num>0:
    rem=num%10
    numbers=numbers*10+rem
    num=num//10

if( temp==numbers):
    print( numbers," is a palindrome")
else:
    print("Not palindrome.")