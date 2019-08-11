
print("Welcome to TrackYourStuff")

BOLD = '\033[1m'
END = '\033[0m'

maxLocs=0
containers = []

print("You don't currently have any stuff tracked")
print("Please enter your container or location names ")
print("Type done when you have added all locations.")
i=0
while 1:
    newItem=input()
    if str(newItem) == 'done':
        break
    containers.append([newItem])
    maxLocs+=1

print("You now have these locations for stuff: ")


print("Type exit to leave program")
while 1:
    for x in range(0,maxLocs):
        if containers[x]:
            print(str(x+1) + ". " + str(containers[x]))
        else:
            break
    print("Please enter the number for a location to add items to: ")
    locInput=input()
    if locInput == "exit":
        break
    try:
        locIndex=int(locInput) -1
    except ValueError:
        print("Sorry, that's not a valid option. Enter a number.\n")
        continue
    if 1 <= int(locInput) <= maxLocs :
        print("You're adding to " + str(containers[locIndex]) + ".")
        while 1:
            print("Please enter the item you want to add. Hit x to go back")
            itemInput=input()
            if itemInput == "x":
                break
            if len(containers[locIndex]) > 1:
                containers[locIndex][1].append(itemInput)
            else:
                containers[locIndex].append([itemInput])


print("Here is your inventory: ")   
print(containers)     

for i in range(len(containers)): 
    if len(containers[i]) < 2:
        items = "Nothing"
    else:
        items=str(containers[i][1])
    print(BOLD + containers[i][0] +END +" has " + items)
