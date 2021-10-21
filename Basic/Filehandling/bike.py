#f = open("bike.txt", "w")
print("\t\tDepartment of Transport Management\n\t\t\tBaneswor, Kathmandu\n\t\t Welcome to DOTM Bike Renewal System\n\t\t\tFisacal Year 2020/21\n")
name = input("Enter Customer Name: ")
address = input("Enter Customer Address: ")
bike_cc = int(input(" Enter Customer Bike in cc: "))
phone = int(input(" Enter Phone No: "))
tax_amt = 0
if bike_cc < 125:
    tax_amt = 2800
elif 126 < bike_cc <= 160:
    tax_amt = 2800 + 4500
elif 161 < bike_cc <= 250:
    tax_amt = 5500 + 2800 + 4500
elif 251 < bike_cc <= 400:
    tax_amt = 9000 + 5500 + 2800 + 4500
elif 401 < bike_cc <= 650:
    tax_amt = 20000 + 9000 + 5500 + 2800 + 4500
elif 651 < bike_cc:
    tax_amt = 30000 + 20000 + 9000 + 5500 + 2800 + 4500
else:
    ("Invalid choice")
("\t\tDepartment of Transport Management\n\t\t\tBaneswor, Kathmandu\n\t\t Welcome to DOTM Bike Renewal System\n\t\t\tFisacal Year 2020/21\n")
("Customer name:  {name}\t\t\tCustomer address: {address}\n")
("Customer Bike[cc]:  {bike_cc}\t\t\tPhone No: {phone}\n")
("{name} with Bike_cc {bike_cc}cc have to pax Tax to [Rs.]= {tax_amt}\n")
("\t\t\t***Thank You***")
