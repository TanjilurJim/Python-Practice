class English:
    def __init__(self):
        pass

    def greeting(self):
        return "Hello"


class French:
    def __init__(self):
        pass



    def greeting(self):
        return 'Bonjur'


def greet(language):
    return language.greeting()


e = English()
f = French()

print(greet(e))
print(greet(f))

