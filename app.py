# stock market investoment tool
def percentage_to_cash(invest_amount, equity):
   '''convert % asset allocation to cash value'''
   asset_investable = invest_amount*equity/100
   round_asset_investable = round(asset_investable,2)
   return round_asset_investable 

def get_allocation(age):
    '''function to return equity, gold'''
    if age <= 20:
       equity =90 ; gold =10 
    elif age<=30:
       equity=70 ; gold = 30
    elif age <= 40:
       equity=80 ; gold = 20 
    elif age<= 50:
       equity=65 ; gold = 35
    elif age<= 60:
       equity =45 ; gold=55
    else:
       equity=95; gold = 5 
    return equity, gold

def main():
   print("welcome to stock market tool")
   age = int (input ("enter age: "))
   salary = int(input("enter salary: "))
   expense = int(input("enter expense: "))

   invest_amount = salary - expense
   print("investable amount is: ", invest_amount)
   equity, gold = get_allocation(age)

   print("recomendded asset allocation: ")
   print("equity: rs",percentage_to_cash(invest_amount, equity))
   print("gold: rs",percentage_to_cash (invest_amount, gold))


if __name__ == "__main__":
   main()


