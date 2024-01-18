expression = input("Enter an expression please: ")
# this is a component
x,y,z = expression.split()

x= int(x)
z= int(z)

final=0.0
# this sees what operation is used and then does it 

if y =="+":
    final=x+z
elif y=="-":
    final = x-z
elif y=="*":
    final= x*z
elif y=="/":
    if z!=0:
        final= x/z
    else:
        print("Try again")

print(f"final: {final:.1f}")     
