def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # must start with two letters
    if len(s) < 2 or not s[:2].isalpha():
        return False
    # the maximum of 6 and minimum of2
    if not (2 <= len(s) <= 6):
        return False
    # can't use numbers in middle instead in the end
    if any(char.isdigit() for char in s[2:-1]):
        return False
    #the first one can't be 0
    if s[2:].find('0') == 0:
        return False
    # No periods, spaces, punctuation
    if any(char in ". ,;:!?" for char in s):
        return False
    # if everything is true, the plate is vaild
    return True

main()