def annual_income( status, total_income):
    if status == 'Y':
        if annual <= 450000:
             a = annual * 0.01
            total = a
            tax = 1

        elif 450000 < annual <= 550000:
            a = 450000 * 0.01
            b = (annual - 450000) * 0.1
            tax = (1 + 10)
            total = a + b

        elif 550000 < annual <= 650000:
            a = 450000 * 0.01
            b = (550000 - 450000) * 0.1
            c = (annual - 550000) * 0.2
            tax = (1 + 10 + 20)
            total = a + b + c

        elif 650000 < annual <= 1250000:
            a = 450000 * 0.01
            b = (550000 - 450000) * 0.1
            c = (650000 - 550000) * 0.2
            d = (annual - 650000) * 0.3
            tax = (1 + 10 + 20 + 30)
            total = a + b + c + d

        elif 2000000 <= annual:
            a = 450000 * 0.01
            b = (550000 - 450000) * 0.1
            c = (650000 - 550000) * 0.2
            d = (1250000 - 650000) * 0.3
            e = (annual - 1250000) * 0.36
            tax = (1 + 10 + 20 + 30 + 36)
            total = a + b + c + d + e

    elif status == 'N':
        if annual <= 400000:
            a = annual * 0.01
            total = a
            tax = 1

        elif 400000 < annual <= 500000:
            a = 400000 * 0.01
            b = (annual - 400000) * 0.1
            tax = (1 + 10)
            total = a + b

        elif 500000 < annual <= 600000:
            a = 400000 * 0.01
            b = (500000 - 400000) * 0.1
            c = (annual - 500000) * 0.2
            tax = (1 + 10 + 20)
            total = a + b + c

      elif 600000 < annual <= 1300000:
            a = 400000 * 0.01
            b = (500000 - 400000) * 0.1
            c = (600000 - 500000) * 0.2
            d = (annual - 600000) * 0.3
            tax = (1 + 10 + 20 + 30)
            total = a + b + c + d

        elif 2000000 <= annual:
            a = 400000 * 0.01
            b = (500000 - 400000) * 0.1
            c = (600000 - 500000) * 0.2
            d = (1300000 - 600000) * 0.3
            e = (annual - 1300000) * 0.36
            tax = (1 + 10 + 20 + 30 + 36)
            total = a + b + c + d + e


        



def main():
    print("\n\t\t\t\t\tInland Revenue Department")
    print("\t\t\t\tWelcome to Integrated Tax System")
    name = input("\nEnter your name: ")
    address = input("Address: ")
    status = input("Enter 'Y' for Married and 'N' for Unmarried: ").upper()
    pan = int(input("Enter your PAN No.: "))
    income = int(input("Enter your per month income[Rs.]: "))
    total_income=income*12
    annual_income( status, total_income)



        



    main()


