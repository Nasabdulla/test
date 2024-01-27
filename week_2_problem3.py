def main():
    file=input("Enter the file name: ")

    mediaT = get(file)
# prints the results 
    print(mediaT)

def get(file):
    # dictionary files
    type= { ".gif": "image/gif",".jpg": "image/jpeg",".jpeg": "image/jpeg",".png": "image/png",".pdf": "application/pdf", ".txt": "text/plain",".zip": "application/zip"}

    #case insensitive
    extension = file.lower().split('.')[-1]

    # looks inside dictionary
    return type.get(f".{extension}", "application/octet-stream")

main()

