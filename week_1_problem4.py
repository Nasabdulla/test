def physic (mass):

    # the speed of light 
    speed = 300000000
    
    # e=mc^2
    e =mass * (speed ** 2)
    
    return e

def main():

   # ask user for mass for kilograms
    mass = int(input("enter number: "))
    
    # Calculating using the function
    e = physic (mass)
    
    # then we print 
    print( str(e) + " Joules")

if __name__ == "__main__":

    main()
