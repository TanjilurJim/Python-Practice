def decorator(fun):
    def wrapper(msg):
        print('*'*10)
        fun(msg)
        print('*'*10)
    return wrapper

@decorator
def display(msg):
    print(msg)

# d = decorator(display)
# d('welcome')

# display = decorator(display)
display('welcome')