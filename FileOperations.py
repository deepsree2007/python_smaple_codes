from FileMethods import *

filename = input("Enter filename:")
mode = input("Enter the mode (r-read, w-write, a-append)")
if mode=='w' or 'r' or 'a':
    try:
        file = openFile(filename,mode)
        if mode=='r':
            chars = input("do you want to read a specific number of characters? (y/n)")
            if chars == 'y':
                noOfChars = int(input("Enter the number of characters"))
                print( readFile(file,noOfChars) )
            else:
                line = input("do you want to read line by line? (y/n)")
                if line=='y':
                    lines = readLines(file);
                    for li in lines:
                        print(li)
                else:
                    print(readFile(file))
        else:
            lines=[]
            data = input("enter the data to be entered. type 0 when u are done!!!")
            while data!='0':
                lines.append(data+"\n")
                data = input()
            writeFile(file,lines)
            
    
    except Exception as e:
            print("Error occured " ,e)
    else:
        file.close()
        print("All file operations are completed")
    
else:
    print("Invalid mode")
