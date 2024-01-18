def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #gets rid of the dollar sign and convert to float
    return float (d[1:])


def percent_to_float(p):
    #gets rid of the percentage sign and covert and then divide to get decimal
    return float (p[:-1])/100


main()