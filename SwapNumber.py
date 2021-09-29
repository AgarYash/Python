# Python program to swap two variables

# x = 5
# y = 10

# To take inputs from the user
x = input('Enter value of x: ')
y = input('Enter value of y: ')

# create a temporary variable and swap the values
x,y=y,x

print("The value of x after swapping: ",x)
print("The value of y after swapping: ",y)


#Second Method
# Python program to swap two variables

# x = 5
# y = 10

# To take inputs from the user
x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))

# create a temporary variable and swap the values
x=x^y
y=y^x
x=x^y

print("The value of x after swapping: ",x)
print("The value of y after swapping: ",y)
