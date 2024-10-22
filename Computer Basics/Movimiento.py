t= float(input("Enter time: "))
a= float(input("Enter acceleration: "))
x0= float(input("Enter initial position: "))
v0= float(input("Enter initial velocity: "))
x = x0+v0*t+0.5*a*t**2
v=v0+a*t

print("The final position is: ",x)
print("The final velocity is: ",v)
