# tower of hanoi showing moves

def move(f,t):
    print(f"Move disc from {f} to {t}!")

def hanoi(n,f,h,t):
    if(n == 0):
        pass
    else:
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)

#driver from here
discs  = int(input("No. of discs"))
p1 = input("Name of pillar 1 ")
p2 = input("Name of pillar 2 ")
p3 = input("Name of pillar 3 ")

hanoi(discs,p1,p2,p3)
