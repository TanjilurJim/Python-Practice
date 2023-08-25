terminate = False
while not terminate:
    number1 = input("please enter a number:")
    number2 = input("please enter a number:")
    number1=int(number1)
    number2=int(number2)

    while True:
        operation = input("please enter add/sub or quit to exit: ")
        if operation == "quit":
            print("program exiting")
            terminate=True
            break

        if operation not in ["add", "sub"]:
            print("unknown operation!")
            continue
        if operation =="add" :
            print("result is: ", number1+number2)
            break
        if operation =="sub":
            print("result is: ", number1-number2)
            break

