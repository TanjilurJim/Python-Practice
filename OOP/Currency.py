class CurrencyConverter():

    def __init__(self,currency, rate):
        self.currency =currency
        self.rate = rate


    def set_currency(self,name):
        self.currency = name
    
        
    def set_rate(self,name):
        self.rate = name
        
    def get_currency(self):
        return self.currency
        
    def get_rate(self):
        return self.rate
        
    def convert(self,amount):
        return self.currency + 'conversion is ' + self.rate*amount
    
cc = CurrencyConverter('USD',110)
print(cc.convert(100))

        


