import random
def max(num1,num2):
    if num1>num2:
        result=num1
    else:
        result=num2

    return result

def main():
    i= random.randint(1,100)
    j=random.randint(1,100)
    print(i,j)
    k=max(i,j)
    print("The largest number between {} and {} is {}".format(i,j,k))

main()

