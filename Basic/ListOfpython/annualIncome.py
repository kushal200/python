print("\t\t\t Inland Revenue Department")
print("\t\t Welcome to Integrated Tax System")
name=input("Enter the your name:")
address=input("Address:")
married_status=input("Enter 'Y' for Married and 'N' for Unmarried:")
pan_no=int(input("Enter your Pan No:"))
monthly_income=float(input("Enter your per months income[Rs.]:"))
annual_income=monthly_income*12

if married_status=='Y':
    if annual_income<=450000:
        tax1=annual_income*0.01
        total_tax=tax1

    elif 450000<annual_income<=550000:
        tax1=annual_income*0.01
        tax2=(550000-450000)*0.1
        total_tax=tax1+tax2

    elif 550000<annual_income<=750000:
        tax1=annual_income*0.01
        tax2=(550000-450000)*0.1
        tax3=(750000-550000)*0.2


    
