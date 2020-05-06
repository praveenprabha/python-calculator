def add_value(x,y):
  return x + y

def substract_value(x,y):
  return ( max(x,y) - min(x,y) )

def multiply_value(x,y):
  return x * y

def divide_value (x,y):
  pass

def square_value (x):
  pass


x = int(input('Enter Value for X : ' ))
y = int(input('Enter Value for Y : ' ))
print(x,y)

print("Addition Value {}".format(add_value(x,y)))
print("Subtraction  Value {}".format(substract_value(x,y)))
print("Multiiplication Value {}".format(multiply_value(x,y)))