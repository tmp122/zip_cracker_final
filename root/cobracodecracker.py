import pyzipper
from time import time
 
def main():
    path_zip=input("Enter path of the zip file: ")
    path_pass=input("Enter path of the password file: ")
    try:
        with pyzipper.AESZipFile(path_zip) as myZip:
            myZip.pwd=None
    except pyzipper.BadZipfile:
        print("[!] There was an error opening your zip file.")
        return
 
    password = ''
 
    timeStart = time()
    with open(path_pass, "r") as f:
        passes = f.readlines()
        for pass_count, x in enumerate(passes):
            password = x.strip()
            try:
                with pyzipper.AESZipFile(path_zip) as myZip:
                    myZip.pwd=password.encode('utf-8')
                    myZip.extractall()
                totalTime = time() - timeStart
                print("\nPassword cracked: %s\n" % password)
                print("%i password attempts per second." % (pass_count / totalTime))
                return
            except Exception as e:
                print(e)
                continue 
        else:
            print("Sorry, password not found.")
 
if __name__ == '__main__':
    main()


