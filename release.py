import os
import getpass
import hashlib
import base64
salt = "saltstring"
pepper = "pepperstring"
supersumiterations = 1000
base64iterations = 10
username = "username"
def base64encodetimes(times,string):
    i = 0
    string = string.encode()
    while i != times:
        string = base64.b64encode(string)
        i = i + 1
    string = string.decode()
    return(string)
def supersum(string):
    i = 0
    string = pepper + string + salt
    while i != supersumiterations:
        string = string.encode()
        string = hashlib.sha512(string).hexdigest()
        i = i + 1
    return(string)

def generateKey():
    os.system("gpg --full-generate-key")
def encryptFile(name):
    os.system("cd ~/.gpgkeys && gpg --output " + name + ".gpg -c --batch --passphrase " + masterpassword + " temp.txt")
    print("\n")
def decryptFile(name):
    os.system("cd ~/.gpgkeys && gpg -d --batch --passphrase "+ masterpassword +" "+ name + ".gpg")
    print("\n")
def encryptPassword(label):
    passwordToEncrypt = getpass.getpass("Password to encrypt (Will not echo): ")
    file = open("/home/"+username+"/.gpgkeys/temp.txt", "w")
    file.write(passwordToEncrypt)
    file.close
    file = open("/home/"+username+"/.gpgkeys/temp.txt", "r")
    encryptFile(label)
    file.close
    os.remove("/home/"+username+"/.gpgkeys/temp.txt")
    print("done")
quit = 0
masterpassword = getpass.getpass("Master Password(will not echo): ")
masterpassword = supersum(masterpassword)
masterpassword = base64encodetimes(base64iterations,masterpassword)
sessionkey = supersum(masterpassword)
print("Session Key: " + sessionkey[-8:])
while quit != 1:
    action = input("What would you like to do?(help for more details): ")
    if action == "quit":
        quit = 1
        os.system("clear")
    if action == "encryptPassword":
        passwordLabel = input("Password Label: ")
        encryptPassword(passwordLabel)
    if action == "decryptPassword":
        passwordLabel = input("Password Label: ")
        decryptFile(passwordLabel)
    if action == "generateKey":
        generateKey()
    if action == "help":
        print("Comamnds: quit, encryptPassword, decryptPassword, generateKey")


