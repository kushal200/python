import smtplib

class myCollege:
    def __init__(self, IUKLcode = 0, collegeName = '', totalStu = 0, area = 0, density = 0, presence = 0, email = ''):

        self.IUKLcode = IUKLcode
        self.collegeName = collegeName
        self.totalStu = totalStu
        self.area = area
        self.density = density
        self.presence = presence
        self.email = email


    def CalculateDensity(self):
        self.density = self.totalStu/self.area


    def InputInformation(self):
        self.IUKLcode = int(input("IUKLCode: "))
        self.collegeName = input("CollegeName: ")
        self.totalStu = int(input("TotalStudent: "))
        self.area = int(input("AreaOfCollege: "))
        self.CalculateDensity()
        self.DensityInformation()


    def DensityInformation(self):
        print("**********************************************")
        print(f'''
                IUKLCode: {self.IUKLcode}
                CollegeName: {self.collegeName}
                TotalStudent: {self.totalStu}
                AreaOfCollege: {self.area}
                DensityOfCollege: {self.density}
        ''')
        if(self.totalStu > 1500 and self.totalStu < 5000):
            self.presence = "Highly Presence of Student"
            self.email = "admin1@iukl.com.np"
            self.mail()
            print("Email Notification Sent")

        elif(self.totalStu > 500 and self.totalStu <= 1500):
            self.presence = "Average Presence in the college"
            self.email = "admin2@iukl.com.np"
            self.mail()
            print("Email Notification Sent")

        elif(self.totalStu < 500):
            self.presence = "Too less student in the college"
            self.email = "info@iukl.com.np"
            self.mail()
            print("Email Notification Sent")

    def mail(self):
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("commandonepal69@gmail.com", "9803933159")
        server.sendmail("commandonepal69@gmail.com", self.email, self.presence)



def main():
    college = myCollege()
    college.InputInformation()

main()