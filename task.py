import random as r
print("                              Welcome Our Shopping World                             ")
class Shopping:
    def Basic_Info(self, name, pm, generated_otp):
        self.name = name
        self.pm = pm
        self.generated_otp = generated_otp

    def generate_otp(self):
        otp = r.randint(1000, 9999)
        return otp

class ValidOTP(Shopping):
    def validate_otp(self, user_input, generated_otp, amount, payment_mode, balance):
        if user_input == generated_otp:
            print("OTP is valid")

            if payment_mode.upper() == "GPAY":
                d = balance - amount
                print("Balance remaining in Bank Of Maharastra:", d)
            elif payment_mode.upper() == "PAYTM":
                e = balance - amount
                print("Balance remaining in Bank Of India:", e)
        else:
            print("Invalid OTP")

class Banks(Shopping):
    def __init__(self):
        self.Maharastra_Bank = 200000
        self.India_Bank = 500000

class Amazon(Shopping):
    def am(self):
        print("Amazon")

class Messho(Shopping):
    def me(self):
        print("Messho")

class Flipkart(Shopping):
    def fk(self):
        print("Flipkart")

class Code(Shopping):
    def main(self):
        self.email = input("Enter your email: ")
        self.password = input("Enter your password: ")
        self.product = input("Enter a Product Name: ")
        self.amount = int(input("Enter Your Product Amount: "))

        if self.email == "ss@gmail.com" and self.password == "1234":
            self.pm = input("Enter a payment mode (PAYTM/GPAY): ")

            if self.pm.upper() == "PAYTM" or self.pm.upper() == "GPAY":
                shop_choice = input("Enter a shop choice (Amazon/Messho/Flipkart): ")
                if shop_choice.upper() == "AMAZON":
                    self.shop = Amazon()
                elif shop_choice.upper() == "MESSHO":
                    self.shop = Messho()
                elif shop_choice.upper() == "FLIPKART":
                    self.shop = Flipkart()
                else:
                    print("Invalid shop choice")
                    exit()
                generated_otp = self.generate_otp()
                print("Generated OTP:", generated_otp)
                user_input = int(input("Enter the OTP: "))
                balance = Banks().Maharastra_Bank if self.pm.upper() == "GPAY" else Banks().India_Bank
                ValidOTP().validate_otp(user_input, generated_otp, self.amount, self.pm, balance)
            else:
                print("Invalid payment mode")
        else:
            print("Invalid Email and Password")

c = Code()
c.main()
