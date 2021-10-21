import smtplib
class shop:
    def __init__(self, grandtotal='', remain=0, remaining=0, aftertax=0, discount=0, cate=0, product=0, a='', name='', address='', phonenumber='', email='', cid=1):
        print("\n\n\t*==========WELCOME TO Vegetable Shop==========*\n\t")
        self.grandtotal = grandtotal
        self.product = product
        self.discount = discount
        self.aftertax = aftertax
        self.remain = remain
        self.remaining = remaining
        self.cate = cate
        self.a = a
        self.name = name
        self.address = address
        self.phonenumber = phonenumber
        self.email = email
        self.cid= cid


    def inputdata(self):
        print("\t\tCustomer Information\n")
        self.name = input("\t\tEnter your Name:")
        self.address = input("\n\t\tEnter your Address:")
        self.phonenumber = input("\n\t\tEnter your Phone.No:")
        self.email = input("\n\t\tEnter your Email Address:")


    def productpurchased(self):
        print("S.N.\t\tProduct \t\tPrice \t\tQuantity\n 1.\t\t Potato  \t\t Rs.200 \t\t 30\n 2.\t\t Onion \t\t\t Rs.100 \t\t 30\n 3.\t\t Cauliflower \t\t Rs.150 \t\t 30\n 4.\t\t Tomato \t\t Rs.100 \t\t 30\n 5.\t\t Brinjal \t\t Rs.50 \t\t\t 30\n 6. \t\t Exit\n")
        while (1):
            choice = int(input("Enter the number of your choice:"))
            if (choice == 1):
               quantity = int(input("Enter the quantity:"))
               if (quantity > 30):
                   print("Order not confirmed!! Out of stock")
                   continue
               self.remain = 30 - quantity
               if (self.remain < 5):
                   self.stock = (f"Product getting out of stock! Product Remanning is {self.remain}. Add as soon as possible.")
                   self.mail()
               self.product = self.product + 200 * quantity

            elif (choice == 2):
                quantity = int(input("Enter the quantity:"))
                if (quantity > 30):
                    print("Order not confirmed!! Out of stock")
                    continue
                self.remain = 30 - quantity
                if (self.remain < 5):
                    self.stock = (f"Remaining product is {self.remain}. Please Add product")
                    self.mail()
                self.product = self.product + 100 * quantity

            elif (choice == 3):
                quantity = int(input("Enter the quantity:"))
                quantity = self.remain + quantity
                if (quantity > 30):
                    print("Order not confirmed!! Out of stock")
                    continue
                self.remain = 30 - quantity
                if (self.remain < 5):
                    self.stock = (f"Remaining product is {self.remain}. Please Add product")
                    self.mail()
                self.product = self.product + 150 * quantity

            elif (choice == 4):
                quantity = int(input("Enter the quantity:"))
                if (quantity > 30):
                    print("Order not confirmed!! Out of stock")
                    continue
                self.remain = 30 - quantity
                if (self.remain < 5):
                    self.stock = (f"Remaining product is {self.remain}. Please Add product")
                    self.mail()
                self.product = self.product + 100 * quantity
            elif (choice == 5):
                quantity = int(input("Enter the quantity:"))
                if (quantity > 30):
                    print("Order not confirmed!! Out of stock")
                    continue
                self.remain = 30 - quantity
                if (self.remain < 5):
                    self.stock = (f"Remaining product is {self.remain}. Please Add product")
                    self.mail()
                self.product = self.product + 50 * quantity
            elif (choice == 6):
                break
            else:
                print("You've Enter an Invalid Key, Please Enter again")
        print("Total product Cost with tax =Rs.", self.product, "\n")

    def display(self):
        f = open("Vegetableshop.txt", "a")
        print("************Product BillL*******************")
        f.write("\t\t\t*****Product BillL*****\n")
        f.write(f"\t\t******Customer details*******\n")
        f.write(f"\t\tCustomer name: {self.name}\n ")
        f.write(f"\t\tCustomer address: {self.address}\n")
        f.write(f"\t\tCustomer PhoneNumber: {self.phonenumber}\n")
        f.write(f"\t\tCustomer Email: {self.email}\n")
        f.write(f"\t\tYour Discount rate is: {self.discount} \n")
        f.write(f"\t\tYour Product bill is: {self.product} \n")
        print("\t\tCustomer details:")
        print("\tCustomer name: \t", self.name)
        print("\tCustomer address: \t", self.address)
        print("\tCustomer PhoneNumber: \t", self.phonenumber)
        print("\tCustomer Email: \t", self.email)
        self.category()
        print(f"\tYou are our {self.cate} customer. Your Discount rate is: {self.discount}")
        print("\tYour Product bill is:", self.product)
        self.grandtotal = self.product - (self.product * self.discount)
        # print("Your total amount is Rs:", self.grandtotal)
        # print()
        print("\tYour grandtotal Purchased is:", self.grandtotal)
        f.write(f"\tYour grandtotal Purchased is: {self.grandtotal}\n")

        print("")
        self.cid += 1
        f.close()

    def category(self):

        self.aftertax = self.product * 0.13
        amount = self.product + self.aftertax


        if (amount < 15000):
            self.cate = "Normal"
            self.discount = 0.02

        elif (amount < 30000 and amount >= 15000):
            self.cate = "Bronze"
            self.discount = 0.15

        elif (amount < 50000 and amount >= 30000):
            self.cate = "Silver"
            self.discount = 0.25

        elif (amount >= 50000):
            self.cate = "Gold"
            self.discount = 0.40

    def mail(self):
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("commandonepal69@gmail.com", "9803933159")
        server.sendmail("commandonepal69@gmail.com", "commandonepal69@gmail.com", self.stock)



def main():
        a = shop()
        while (1):
            print("\t\t1.Enter Your Information")
            print("\t\t2.Purchased Vegetable product")
            print("\t\t3.Show total information")
            print("\t\t4.EXIT\n")

            b = int(input("\t\tEnter the number of your choice:"))
            if (b == 1):
                a.inputdata()
            if (b == 2):
                a.productpurchased()
            if (b == 3):
               a.display()
            if (b == 4):
                quit()
main()