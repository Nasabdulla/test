

def coke():

    amount =50
    insert =0

    #while loop that gets 50 cent

    while insert<amount:
        cent=int(input("insert a coin:"))

        if cent in [5,10,25]:
            insert+=cent
            print(insert)
        else:
            print("invaild, enter again")

coke()
     