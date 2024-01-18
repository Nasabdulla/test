def convert(time):

 hours,minute= map(int, time.split(":"))
# calculate the total 
 hourTime = hours + minute/60
 return hourTime


def main():

 time=input("Enter the time: ")
#converts to hours
 hours = convert(time)
# checks and print the result
 if 7.0 <= hours <=8.0:
    print("It's time for breakfast")
 elif 12.0<= hours <=13.0:
    print("It's time for lunch")
 elif 18.0<= hours <=19.0:
    print("It's time for dinner")

#calls the main when run
if __name__=="__main__":

    main()