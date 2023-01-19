# if name is less than 3 characters long name must be at least 3 characters
# otherwise if it´s more than 50 caracters long name can be a maximum of 50 caracters otherwise name looks good

name = 'Matheus Henrique'

if len(name) < 3:
    print('Name must be at least 3 characters ')
elif len(name) > 50:
    print('Name mus be a maximium of 50 characters')
else:
    print('Name looks good')
#1:16:24