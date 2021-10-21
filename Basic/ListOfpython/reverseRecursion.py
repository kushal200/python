number=int(input("Enter the numebr:"))
Reverse = 0
while(number > 0):
 Reminder = number %10
 Reverse = (Reverse *10) + Reminder
 number = number//10
print("Reverse of input number is = %d" %Reverse)
