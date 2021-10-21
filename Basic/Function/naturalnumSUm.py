number = int(input("Enter any Number: ")) 
total = 0 
value = 1 
display = "" 
while (value <= number): 
    temp = value
    display = display + "+"+str(temp) 
    total = total + value 
    value = value + 1 
    print(display)
    
    
    
    
print("The Sum of Natural Numbers from 1 to {0} = {1}".format(number, total))