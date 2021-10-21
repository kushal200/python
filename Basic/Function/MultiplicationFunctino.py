def multiplication_table(a):
    for i in range(1,11):
        print("%d * %d = %d" %(a,i,a*i))





def main():
    num=int(input("Enter the number"))
    multiplication_table(num)
main()
