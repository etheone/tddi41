import subprocess
from random import randint
import random
import string
import time
import os

def readExistingUsernames():
    usersLocal = []
    bashCommand = "cat /etc/passwd"
    #process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    #output = output.split('\n')
    output = os.popen(bashCommand).read()
    #print(output)
    for line in output:
        usersLocal.append(line.split(':', 1)[0])
    return usersLocal

def generateUsername(name):
    """Generates a unique username"""
    name = name.lower()
    namelist = name.split()
    firstPart = namelist[0][:3] + namelist[-1][:2]
    numbers = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
    userName = firstPart + numbers
    existingUsernames = readExistingUsernames()
    found = False
    while not found:
        if userName in existingUsernames:
            numbers = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
            userName = firstPart + numbers
        else:
            found = True

    return userName
    
def generatePassword():
    return ''.join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for _ in range(8))

def addUser(fullname):
    username = generateUsername(fullname)
    password = generatePassword()
    home = randint(1,2)
    bashCommand = "adduser " + username + " --no-create-home" + " --gecos '" + fullname + "' --disabled-password"
    output = os.popen(bashCommand).read()
    #process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    #output, error = process.communicate()
    time.sleep(2)
    print("User created with \nusername: " + username + " \nand password: " + password)
    
    bashCommand = "mkdir /home" + str(home) + "/" + username
    output = os.popen(bashCommand).read()

    time.sleep(0.5)
    #bashCommand = "usermod -m -d /home/" + username
    #output = os.popen(bashCommand).read()
    
    
    bashCommand = "echo " + username + ":" + password + " | chpasswd"
    #process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    #output, error = process.communicate()
    output = os.popen(bashCommand).read()

    time.sleep(0.3)
    
    bashCommand = "chown " + username + ":" + username + " /home" + str(home) + "/" + username
    output = os.popen(bashCommand).read()
    
    time.sleep(0.2)
    bashCommand = "chmod 700 /home" + str(home) + "/" + username    
    #process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    #output, error = process.communicate()
    
    time.sleep(0.3)
    
    with open("/etc/auto.home", "a") as myfile:
        myfile.write(username + " -fstype=nfs,nfsvers=3,rw,sync server:/home" + str(home) + "/" + username + "\n")



def createUsers():
    f = open('users.txt', 'r')
    lines = [line.strip('\n') for line in open('users.txt', 'r')]

    for line in lines:
        if line != '':
            addUser(line)
        
    bashCommand = "exportfs -v -r"
    output = os.popen(bashCommand).read()
    
    time.sleep(0.5)
    
    bashCommand = "make -C /var/yp"
    #process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    #output, error = process.communicate()
    os.popen(bashCommand).read()
    time.sleep(1)
    print("DONE : ALL USERS ADDED")



createUsers()

#print(generatePassword())
"""Main"""

"""
adduser USERNAME --home /homeX/USERNAME --gecos 'fullNAME' --disabled-password
echo USERNAMEa:PASSWORD | chpasswd
chmod 700 /homeX/USERNAME
modify auto.home
make -C /var/yp"""
