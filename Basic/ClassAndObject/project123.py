class vegetable_shop:

    def __init__(self, grandtotal='', cat=0, p=0, product=0, t=0, a=1000, name='', address='', phonenumber='', email=''):

        print("\n\n*****WELCOME TO VEGETABLE SHOP*****\n")

        self.grandtotal = grandtotal

        self.product = product

        self.t = t

        self.p = p

        self.cat = cat
        self.a = a
        self.name = name
        self.address = address
        self.phonenumber = phonenumber
        self.email = email



    def inputdata(self):
        self.name = input("\nEnter your Name:")
        self.address = input("\nEnter your address:")
        self.phonenumber = input("\nEnter your Phone number:")
        self.email = input("\nEnter your Email:")

    def category(self):  

        print("We have following category for our Customer:-")

        print("1.  Gold---->40%")

        print("2.  Silver---->25%")

        print("3.  Bronze---->15%")

        print("4.  Normal---->2%")

        x = int(input("Enter the Category number>"))

        if (x == 1):

            print("Gold category")

            self.cat = 40 / 100

        elif (x == 2):

            print("Silver category")

            self.cat = 25 / 100

        elif (x == 3):

            print("Bronze category")

            self.cat = 15 / 100

        elif (x == 4):
            print("Normal category")

            self.cat = 2 / 100

        else:

            print("please choose your category")

        print("your category is =", self.cat, "\n")

    def productpurchased(self):

        print("***Vegetable MENU***")

        print("1.Potato----->100\n", "2.Tomato----->80\n", "3.Onion--->200\n", "4.Cauliflower---->50\n", "5.Brinjal--->100\n",
              "6.Exit")

        while (1):

            choice = int(input("Enter the number of your choice:"))

            if (choice == 1):
                quantity = int(input("Enter the quantity:"))
                self.product = self.product + 100 * quantity

            elif (choice == 2):
                quantity = int(input("Enter the quantity:"))
                self.product = self.product + 80 * quantity

            elif (choice == 3):
                quantity = int(input("Enter the quantity:"))
                self.product = self.product + 200 * quantity

            elif (choice == 4):
                quantity = int(input("Enter the quantity:"))
                self.product = self.product + 50 * quantity

            elif (choice == 5):
                quantity = int(input("Enter the quantity:"))
                self.product = self.product + 100 * quantity

            elif (choice == 6):
                break;

            else:
                print("You've Enter an Invalid Key")

        print("Total product Cost=Rs", self.product, "\n")

    def display(self):
        print("****Product BillL of Customer****")
        print("Customer details:")
        print("Customer name:", self.name)
        print("Customer address:", self.address)
        print("Customer PhoneNumber:", self.phonenumber)
        print("Customer Email:", self.email)
        print("Your Discount rate is:", self.cat)
        print("Your Product bill is:", self.product)

        self.grandtotal = self.product - (self.cat * self.product)
        print()
      
        print("Your grandtotal Purchased is:", self.grandtotal, "\n")
        


def main():
    a = vegetable_shop()

    while (1):
        print("1.Enter Customer Information")

        print("2.Choose your category")

        print("3.Calculate Your Purchased")

        print("4.Show total information of Cusstomer")

        print("5.EXIT")

        b = int(input("\nEnter the number of your choice:"))
        if (b == 1):
            a.inputdata()

        if (b == 2):
            a.category()

        if (b == 3):
            a.productpurchased()

        if (b == 4):
            a.display()

        if (b == 5):
            quit()


main()