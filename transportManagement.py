
def bike_cc_calculation(bike_cc):
    tax_amt=0
    
    if bike_cc<=125:
         tax_amt=2800
    elif bike_cc>125 and bike_cc<=160:
        tax_amt=2800+4500
    elif bike_cc>160 and bike_cc<=250:
        tax_amt=2800+4500+5500
    elif bike_cc>250 and bike_cc<=400:
        tax_amt=2800+4500+5500+9000
    elif bike_cc>400 and bike_cc<=650:
        tax_amt=2800+4500+5500+9000+20000
    elif bike_cc>650:
        tax_amt=2800+4500+5500+9000+20000+30000
    else:
        print("No Bike CC recorded.")
    
    

    


def main():
    print("\t\t\t Department of Transport Management")
    print("\t\t\t Banshwor, Kathmandu")
    print("\t\t Welcome to DOTM Bike Renewal System")
    print("\t\t\t Fiscal Year 2020/21")
    name=input("Customer Name:")
    address=input("Customer Address:")
    bike_cc=int(input("Customer Bike in cc:"))
    phone_no=int(input("Phone No:"))
    tax_amt
    bike_cc_calculation(bike_cc)




    print("\t\t Department of Transport Management")
    print("\t\t\t Baneshwor, Kathmandu")
    print("\t\t Welcome to DOTM Bike Renewal System")
    print("\t\t\t Fiscal Year 2020/21")
    print(f"Customer Name:{name}\t\t Address:{address}")
    print(f"Customer Bike[cc]:{bike_cc}\t\t\t Phone No:{phone_no}")
    print(f"{name} with {bike_cc} cc bike have to pay tax to [Rs.]={tax_amt}")
main()





