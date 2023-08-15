# errors
try:
    age = int(input('Age: '))
    income = 2000
    risc = income / age
    print(age)
except ValueError:
    print('Invalid Valueeeeee')
except ZeroDivisionError:
    print("Come on!!! age cannot be Zero")