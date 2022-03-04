from userClass import User
from objectClass import Object

# import numpy

subList = []
objList = []
subDict = {}
objDict = {}

fileReadin = open("actions.txt", "r")
lines = fileReadin.readlines()
fileReadin.close()
my_list = ["addsub", "addobj", "status", "write", "read"]

for line in lines:
    print(line, end="")

print('\n\n\n')

# here the whole read-in sentence is being treated as a string. However, each split that happens occupies
# a different index, so if the line is an addsub action, addsub will be at i = 0, the euid at i = 1, and
# the priority at i = 2

for line in lines:
    line = line.strip()
    line = line.split(" ")

    # the following lines will do different actions depending on what the action was in the actions.txt file
    # line[0] is the action that is to be done.

    if line[0] == my_list[0]:  # addsub
        newUser = User(line[1])
        subList.append(newUser)
        subDict[newUser.getName()] = line[2]
        print("addsub", subDict)  # this shows the key value pairs with name : level pairs

    elif line[0] == my_list[1]:  # addobj
        # this follows the same principle as the addsub if branch above
        newObj = Object(line[1])
        objList.append(newObj)
        objDict[newObj.getName()] = line[2]
        print("addobj", objDict)  # this prints the contents of the obj dictionary

    elif line[0] == my_list[2]:  # status

        print("+--------current state--------+")
        print("|-subject-|--level--|--value--|")
        for users in subList:
            print("|" + '{:^9}'.format(users.getName()) + "|" + '{:^9}'.format(subDict[users.getName()]) + "| " + '{:^8}'.format(str(
                users.getVal())) + "|")
        print("|--object-|--level--|--value--|")
        for objects in objList:
            print("|" + '{:^9}'.format(objects.getName()) + "|" + '{:^9}'.format(objDict[objects.getName()]) + "| " + '{:^8}'.format(str(
                objects.getVal())) + "|")
        print("+-----------------------------+")
    elif line[0] == my_list[3]:  # write
        print(line[0])

    elif line[0] == my_list[4]:  # read
        print(line[0])

    else:
        print("Invalid Operation")

# newUser = User()
# newObj = Object()
