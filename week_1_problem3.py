
def convert(text):

   #  convert the text into emoji

    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    
    #ask for input, use function convert on text then print the value
    Text = input("Please enter some text: ")
    cText = convert(Text)
    print(cText)
# Call main

if __name__ == "__main__":
    
    main()



