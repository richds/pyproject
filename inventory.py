import json
print("Welcome to TrackYourStuff")

BOLD = '\033[1m'
END = '\033[0m'

arrayLength=0
containers = []

def printContents(myStuff):
    for i in range(len(myStuff)): 
        if len(myStuff[i]) < 2:
            items = "Nothing"
        else:
            items=str(myStuff[i][1])
        print(BOLD + myStuff[i][0] +END +" has " + items)

def importDatabase():
    global containers
    with open("data.txt") as file:
        data = json.load(file)
    if data == None:
        print("You don't currently have any stuff tracked")
    else:
        printContents(data)

    print("Type 'new' for a new database, otherwise hit enter to continue with current.")
    if input() != 'new':
        containers = data


def printLocations():
    for x in range(0,len(containers)):
        if containers[x]:
            print(str(x+1) + ". " + str(containers[x]))
        else:
            break

def addLocation():
    while 1:
        global arrayLength
        global containers
        print("Please enter your container or location names ")
        print("Type" + BOLD+" done "+END+" when you have added all locations.")
        newItem=input()
        if str(newItem) == 'done':
            break
        if len(newItem) < 2:
            print("Please enter a valid location name.")
            continue
        containers.append([newItem])
        arrayLength+=1

def deleteLocation():
    while 1:
        global arrayLength
        global containers
        printLocations()
        print("Which number do you want to delete?")
        try:
            delInput=int(input())
            if (0 < delInput < arrayLength):
                del(containers[delInput -1])
                print("Deleted location "+ str(delInput))
                break
        except ValueError:
            print("Please enter a valid location number.")
            continue


def addItems(locIndex):
    print("You're adding to " + str(containers[locIndex]) + ".")
    print("Please enter the items you want to add. Enter x to go back")
    while 1:    
        itemInput=input()
        if itemInput == "x":
            break
        elif len(itemInput) < 2:
            print("Please enter an item name")
            continue
        elif len(containers[locIndex]) > 1:
            containers[locIndex][1].append(itemInput)
        else:
            containers[locIndex].append([itemInput])

importDatabase()
arrayLength=len(containers)

print("Please enter your container or location names ")
print("Type" + BOLD+" done "+END+" when you have added all locations.")
print("Type " + BOLD+"x"+END+" to leave program")
print("Type 'add' to add a location, or 'del' to delete a location, or the number to edit a location.")
while 1:
    printLocations()
    changeLocations=input()
    if changeLocations == "x":
        break
    elif changeLocations == 'add':
        addLocation()
    elif changeLocations == 'del':
        deleteLocation()
    elif 0 < int(changeLocations) < arrayLength:
        addItems(int(changeLocations) -1)

    else:
        print("Sorry, that's not a valid option. \n")
        continue





print("Here is your inventory: ")   
print(containers)     

printContents(containers)

with open('data.txt', 'w') as outfile:
    json.dump(containers, outfile)


