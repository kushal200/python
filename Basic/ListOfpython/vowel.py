userinput=input("Enter the Sentence:")
print(userinput)
vowel=0
for i in userinput:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowel+= 1
print(vowel)


if vowel%i==0:
    print("The given number is a prime number.")
  

else:
    
    print("The number is not a prime number.")
    print("%d * %d = %d"%(vowel,i,vowel*i))