class Computer():
    def __init__(self,name,cpu_make,os_name):
        self.name = name
        self.cpu = self.CPU(cpu_make)
        self.os = self.OS(os_name)

    def __str__(self):
        return f"Name: {self.name}, CPU Make: {self.cpu.get_make()}, OS Name: {self.os.get_name()}"

    class CPU:
        def __init__(self,make):
            self.make = make

        def get_make(self):
            return self.make


    class OS:
        def __init__(self,name):
            self.name = name
        def get_name(self):
            return self.name

c1 = Computer('MyComputer','Intel','Windows')
# print(c1.cpu.get_make())
# print(c1.os.get_name())
print(c1)