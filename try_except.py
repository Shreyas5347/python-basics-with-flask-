'''Only put risky code inside try.
Not everything.
try = risky work
except = failure handling
else = success handling
there are different types of error like valueerrors used for different reasons '''
try:
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    c=(a/b)
except ZeroDivisionError as err:
    print("cannot be divided by zero")
except ValueError:
    print("The input is not a valid number.")
else:
    print(c)
