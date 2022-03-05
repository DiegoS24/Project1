from userClass import User
from objectClass import Object
from enums import Levels

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
    line = line.strip()
    print(line)

print('\n\n\n')

# here the whole read-in sentence is being treated as a string. However, each split that happens occupies
# a different index, so if the line is an addsub action, addsub will be at i = 0, the euid at i = 1, and
# the priority at i = 2

for line in lines:
    line = line.strip()
    line = line.split(" ")

    # the following lines will do different actions depending on what the action was in the actions.txt file
    # line[0] is the action that is to be done.

    # addsub
    if line[0] == my_list[0]:
        newUser = User(line[1])
        subList.append(newUser)
        subDict[newUser.getName()] = Levels[line[2]]
        print("Subject Added   : " + line[0] + " " + newUser.getName() + " " + str(subDict[newUser.getName()].name))

    # addobj
    elif line[0] == my_list[1]:
        # this follows the same principle as the addsub if branch above
        newObj = Object(line[1])
        objList.append(newObj)
        objDict[newObj.getName()] = Levels[line[2]]
        print("Object Added    : " + line[0] + " " + newObj.getName() + " " + str(
            objDict[newObj.getName()].name))  # this prints the contents of the obj dictionary

    # status
    elif line[0] == my_list[2]:
        # this takes in invalid ops like "status 10" I need to find a way to accept status commands that are ONLY status

        # print(line)
        print("+--------current state--------+")
        print("|-subject-|--level--|--value--|")
        for users in subList:
            print("|" + '{:^9}'.format(users.getName()) + "|" + '{:^9}'.format(
                subDict[users.getName()].name) + "| " + '{:^8}'.format(str(users.getVal())) + "|")
        print("|--object-|--level--|--value--|")
        for objects in objList:
            print("|" + '{:^9}'.format(objects.getName()) + "|" + '{:^9}'.format(
                objDict[objects.getName()].name) + "| " + '{:^8}'.format(str(objects.getVal())) + "|")
        print("+-----------------------------+")

    # write
    # write name object value
    elif line[0] == my_list[3]:
        tempUser = User(line[1])
        tempObj = Object(line[2])
        tempVal = int(line[3])

        # if the subject has a lower level than the object, we can write up.
        if subDict[tempUser.getName()].value <= objDict[tempObj.getName()].value:
            i = 0
            j = 0
            while objList[i].getName() != tempObj.getName():
                i += 1
            objList[i].setVal(tempVal)
            print("Access Granted  : " + tempUser.getName() + " writes value " + str(tempVal) + " to " + tempObj.getName())
            while subList[j].getName() != tempUser.getName():
                j += 1
            subList[j].setVal(tempVal)
        # no write down
        elif subDict[tempUser.getName()].value > objDict[tempObj.getName()].value:
            print("Access Denied  : " + tempUser.getName() + " writes value " + str(tempVal) + " to " + tempObj.getName())

        # print(subDict[tempUser], objDict[tempObj])

    # read
    elif line[0] == my_list[4]:
        tempUser = User(line[1])
        tempObj = Object(line[2])
        # when I call new objects,the temporary ones have the values set to 0. So I need to iterate through the object
        # list, where the names match, and assign that respective value

        if subDict[tempUser.getName()].value >= objDict[tempObj.getName()].value:
            i = 0
            j = 0
            while subList[i].getName() != tempUser.getName():
                i += 1

            while objList[j].getName() != tempObj.getName():
                j += 1
            # issue here, has the right object, incorrect value. but the write command sets the desired value in location
            subList[i].setVal(objList[j].getVal())

            print("Access Granted  : " + tempUser.getName() + " reads  " + tempObj.getName())

        elif subDict[tempUser.getName()].value < objDict[tempObj.getName()].value:
            print("Access Denied  : " + tempUser.getName() + " reads  " + tempObj.getName())

    else:
        print("Bad Instruction: " + line[0])
