def oddeven(a):
    if a%2==0:
        print( a,"is Even Number")
    else:
        print(a,"is Odd Number")
    
    


def main():
    num=int(input("Enter any number:"))
    oddeven(num)
    
    
main()