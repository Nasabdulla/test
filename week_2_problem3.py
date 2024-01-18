def main():
   
    fileName = input("Enter the name of the file: ")

   
    if fileName.lower().endswith((".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip")):
        
        print(mediaType(fileName))
    else:
        print("application/octet-stream")

def mediaType(file_name):
 
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    
    file_extension = file_name.lower().split(".")[-1]

    return media_types.get("." + file_extension, "application/octet-stream")

if __name__ == "__main__":

    main()
