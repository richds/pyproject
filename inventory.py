
print("Welcome to TrackYourStuff")

maxLocs=2
containers = []

print("You don't currently have any stuff tracked")
i=0
while i < maxLocs:
    print("Please enter your container or location name")
    newItem=input()
    containers.append([newItem])
    i+=1


print("You now have these locations for stuff: ")

for x in range(0,maxLocs):
    if containers[x]:
        print(str(x+1) + ". " + str(containers[x]))
    else:
        break
print("Type exit to leave program")
while 1:
    print("Please enter the number for a location to add items to: ")
    locInput=input()
    if locInput == "exit":
        break
    locIndex=int(locInput) -1
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
