def camel(camel):
    snake = ''
    for char in camel:
        if char.isupper():
            snake += '_' + char.lower()
        else:
            snake += char
    
    return snake.lstrip('_')
# turn it into snake case
def main():
   
    put= input("Enter variable name in camel case:")
     #takes the variable, goes though the function
    snake = camel(put)

    print(snake)

main()