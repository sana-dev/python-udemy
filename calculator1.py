print("Welcome to my calculator")
x = input("put your first value: ")
y = input("put the second value:")
x = (float(x))
y = (float(y))
s = input ("enter the desired operator(+,-,*,/):")
if (s == "+"):
 print(x+y)
elif (s=="-"):
  print(x-y)
elif (s=="/"):
  print(x/y)
elif (s=="*"):
  print(x*y)
else:
  print("Invalid value, Add the number or operator again:")

