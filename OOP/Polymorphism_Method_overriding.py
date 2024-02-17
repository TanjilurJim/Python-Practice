class iPhone6:
    def home(self):
        print('home button ')


class iPhoneX(iPhone6):
    def home(self):
        print("no home button")
        super().home() # to call the method of parent class in child class
        


i6 = iPhone6()

i6.home()

ix = iPhoneX()
ix.home()

