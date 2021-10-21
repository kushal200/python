
string=str(input("Enter a sentence:"))
count=0
prime=0
for i in string:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count=count+1
if count==2:
    for i in range(1,count+1):
        if count%i==0:
            prime=prime+1
    if prime<=2:
        print("%d is a prime number"%count)
    else:
         for i in range(1,11):
            print("%d X %d =  %d"%(count,i,count*i))