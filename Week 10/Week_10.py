import os

def main():
    direct = input("enter the name of directory: ")
    filename = input("enter the name of file: ")
    username = input("Please enter your name: ")
    useraddress = input("Please enter your address: ")
    userphonenum = input("Please enter your phone number : ")

    if os.path.isdir(direct):
        writefile = open(os.path.join(direct, filename), 'w')

        writefile.write(username + ' ' + useraddress + ' ' + userphonenum + '\n')

        writefile.close()

        print("Contents of the file: " + '\n')

        filehandle = open(os.path.join(direct, filename), 'r')

        for line in filehandle:
            print(line)
        filehandle.close()
    else:
        print("The directory doesnt exist! try again!")
main()
