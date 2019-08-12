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


importDatabase()
arrayLength=len(containers)
printLocations()

print("Please enter your container or location names ")
print("Type" + BOLD+" done "+END+" when you have added all locations.")
i=0
while 1:
    newItem=input()
    if str(newItem) == 'done':
        break
    if len(newItem) < 2:
        print("Please enter a valid location.")
        continue
    containers.append([newItem])
    arrayLength+=1

print("You now have these locations for stuff: ")


print("Type " + BOLD+"x"+END+" to leave program")
while 1:
    printLocations()
    print("Please enter the number for a location to add items to: ")
    locInput=input()
    if locInput == "x":
        break
    try:
        locIndex=int(locInput) -1
    except ValueError:
        print("Sorry, that's not a valid option. Enter a number.\n")
        continue
    if 1 <= int(locInput) <= arrayLength :
        print("You're adding to " + str(containers[locIndex]) + ".")
        while 1:
            print("Please enter the item you want to add. Hit x to go back")
            itemInput=input()
            if itemInput == "x":
                break
            if len(itemInput) < 2:
                print("Please enter an item name")
                continue
            if len(containers[locIndex]) > 1:
                containers[locIndex][1].append(itemInput)
            else:
                containers[locIndex].append([itemInput])


print("Here is your inventory: ")   
print(containers)     

printContents(containers)

with open('data.txt', 'w') as outfile:
    json.dump(containers, outfile)


