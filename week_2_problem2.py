greeting= input("Hi there: ")
#removes the leading space and convert to lowercase
greeting=greeting.strip().lower()

#checks the user input and puts the amount
if greeting.startswith("hello"):
    print("0")
elif greeting.startswith("h"):
    print("20")
else:
    print("100")

