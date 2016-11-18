import subprocess

def readExistingUsernames():

    bashCommand = "cat /etc/passwd"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    output = output.split('\n')
    for line in output:
        usersLocal.append(line.split(':', 1)[0])
        




"""Main"""
usersLocal = []

