import random,copy,time
world=[[random.randint(0,1) for _ in range(16)] for _ in range(16)]
tempworld=[]
print(3)

def showworld():
    print("\n\n\n\n\n")
    for i in range(16):
        for j in range(16):
            if world[i][j]==1:
                print("■",end=" ")
            else:
                #print("□",end=" ")
                print(" ",end=" ")
        print()

def surroundingscheck(y,x):
    counter=0
    for i in range(-1,2):
        for j in range(-1,2):
            if i!=0 and j!=0:
                try:
                    counter+=tempworld[y+i][x+j]
                except:
                    pass
    return counter

def refreshworld():
    global world,tempworld
    tempworld=copy.deepcopy(world)
    for y in range(16):
        for x in range(16):
            if 2<=surroundingscheck(y,x)<=3:
                world[y][x]=1
            else:
                world[y][x]=0

while True:
    showworld()
    refreshworld()
    time.sleep(0.5)