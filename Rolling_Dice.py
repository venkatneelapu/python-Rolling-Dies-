import random
x = "Y"
z = int(input("input a number between 1-6: ")) 
while x == "y" or x=="Y":
    num = random.randint(1,6)
     
    if num == 1:
        print(" ----- " , "|     |" , "|  0  |" , "|     |" , " ----- " , sep="\n")
    if num == 2:
        print(" ----- " , "| 0   |" , "|     |" , "|   0 |" , " ----- " , sep="\n")
    if num == 3:
        print(" ----- " , "|     |" , "|0 0 0|" , "|     |" , " ----- " , sep="\n")
    if num == 4:
        print(" ----- " , "|0   0|" , "|     |" , "|0   0|" , " ----- " , sep="\n")
    if num == 5:
        print(" ----- " , "|0   0|" , "|  0  |" , "|0   0|" , " ----- " , sep="\n")
    if num == 6:
        print(" ----- " , "|0 0 0|" , "|     |" , "|0 0 0|" , " ----- " , sep="\n")
    if num==z:
        print("\n You won \n")
        break

    print("\n")     
    x=input("Roll again: Y/y    exit: N/n")
    print("\n")
