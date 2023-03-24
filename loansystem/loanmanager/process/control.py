class Manager:

    def loan_profit(self, amount):
        return int(float(amount) * .08)
    
    def staff_profit(self, amount):
        return int(float(amount) * .02)
    
    def loan_method(self, loan_type):
        if(loan_type):
            return "daily"
        else:
            return "monthly"
    
if __name__=="__main__":
    print(Manager.loan_profit(1000))
    print(Manager.staff_profit(1000))