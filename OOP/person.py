class Person():

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        print("hello")

    def report(self):
        print(f'I am {self.first_name} {self.last_name}')    


# x = Person("John","Smith")
# x.hello()
        
# x.report()


class Agent(Person):
     def report(self): #overriding
         print('i am here')
     
     def reveal(self,passcode):
         
         if passcode == 123:
             print(f"I am a secret agent {self.first_name} {self.last_name}")
         else:
             self.report()


# x = Person("Jim","Boss")
x = Agent("Jim","Boss")

x.reveal(12)
x.reveal(123)

        



