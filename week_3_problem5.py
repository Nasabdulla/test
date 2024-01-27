def main():

    fruit = input("Enter a fruit: ")
  # get caloris for what user entered for fruit
    calorie = get(fruit)
 # print the calories, if none, print invalid
    if calorie is not None:
        print("It has", calorie, "calories" )
    else:
        print("Invalid ")

def get(fruit):
        #dictionary of fruits
    calories = {"Apple": 95,"Banana": 105,"Orange": 62,"Strawberries": 50, }

    if fruit in calories:
        return calories[fruit]
    else:
        return None

main()


