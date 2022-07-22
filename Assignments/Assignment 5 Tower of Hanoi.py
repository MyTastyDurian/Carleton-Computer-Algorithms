#task - create an iterative function that takes n as an int for the input and outputs a series of steps to move all n disks from peg 1 to 3
#a - source pole
#b - extra pole
#c - destination
def IsEmpty(a):
    if not a:
        return True
    
    return False

def IsLegal(a,b):
    if a > b:
        return True

    return False

def push(a,b):
    return b.append(a)

def pop(a,b):
    return b.remove(a)

def move(n):
    m = pow(2,n) - 1
    a = []
    b = []
    c = []
    for i in range(n,0,-1):
        a.append(i)
    
    if(n%2 == 0):
        for i in range(1,m+1):
            if(i%3 == 1):
                if(IsEmpty(a)):
                    print("Disk {} moved from B to A".format(b[-1]))
                    push(b[-1],a)
                    pop(b[-1],b)
                    

                else:
                    if not(IsEmpty(b)):
                        if(IsLegal(a[-1],b[-1])):
                            print("Disk {} moved from B to A".format(b[-1]))
                            push(b[-1],a)
                            pop(b[-1],b)
                        

                        else:
                            print("Disk {} moved from A to B".format(a[-1]))
                            push(a[-1],b)
                            pop(a[-1],a)
                            
                    else:
                        print("Disk {} moved from A to B".format(a[-1]))
                        push(a[-1],b)
                        pop(a[-1],a)
        

            elif(i%3 == 2):

                if(IsEmpty(a)):
                    print("Disk {} moved from C to A".format(c[-1]))
                    push(c[-1],a)
                    pop(c[-1],c)

                else:
                    if not(IsEmpty(c)):
                        if(IsLegal(a[-1],c[-1])):
                            print("Disk {} moved from C to A".format(c[-1]))
                            push(c[-1],a)
                            pop(c[-1],c)

                        else:
                            print("Disk {} moved from A to C".format(a[-1]))
                            push(a[-1],c)
                            pop(a[-1],a)
                            

                    else:
                        print("Disk {} moved from A to C".format(a[-1]))
                        push(a[-1],c)
                        pop(a[-1],a)

            elif(i%3 == 0):
                if(IsEmpty(c)):
                    print("Disk {} moved from B to C".format(b[-1]))
                    push(b[-1],c)
                    pop(b[-1],b)

                else:
                    if not(IsEmpty(b)):
                        if(IsLegal(c[-1],b[-1])):
                            print("Disk {} moved from B to C".format(b[-1]))
                            push(b[-1],c)
                            pop(b[-1],b)

                        else:
                            print("Disk {} moved from C to B".format(c[-1]))
                            push(c[-1],b)
                            pop(c[-1],c)
                            
                    else:
                        print("Disk {} moved from C to B".format(c[-1]))
                        push(c[-1],b)
                        pop(c[-1],c)

    else:
        for i in range(1,m+1):
            if(i%3 == 1):
                if(IsEmpty(a)):
                    print("Disk {} moved from C to A".format(c[-1]))
                    push(c[-1],a,c)
                    pop(c[-1],c)
                    
                else:
                    if not(IsEmpty(c)):
                        if(IsLegal(a[-1],c[-1])):
                            print("Disk {} moved from C to A".format(c[-1]))
                            push(c[-1],a)
                            pop(c[-1],c)
                        

                        else:
                            print("Disk {} moved from A to C".format(a[-1]))
                            push(a[-1],c)
                            pop(a[-1],a)
                            
                    else:
                        print("Disk {} moved from A to C".format(a[-1]))
                        push(a[-1],c)
                        pop(a[-1],a)
        

            elif(i%3 == 2):

                if(IsEmpty(a)):
                    print("Disk {} moved from B to A".format(b[-1]))
                    push(b[-1],a)
                    pop(b[-1],b)

                else:
                    if not(IsEmpty(b)):
                        if(IsLegal(a[-1],b[-1])):
                            print("Disk {} moved from B to A".format(b[-1]))
                            push(b[-1],a)
                            pop(b[-1],b)

                        else:
                            print("Disk {} moved from A to B".format(a[-1]))
                            push(a[-1],b)
                            pop(a[-1],a)
                            

                    else:
                        print("Disk {} moved from A to B".format(a[-1]))
                        push(a[-1],b)
                        pop(a[-1],a)

            elif(i%3 == 0):
                if(IsEmpty(b)):
                    print("Disk {} moved from C to B".format(c[-1]))
                    push(c[-1],b)
                    pop(c[-1],c)

                else:
                    if not(IsEmpty(c)):
                        if(IsLegal(b[-1],c[-1])):
                            print("Disk {} moved from C to B".format(c[-1]))
                            push(c[-1],b)
                            pop(c[-1],c)

                        else:
                            print("Disk {} moved from B to C".format(b[-1]))
                            push(b[-1],c)
                            pop(b[-1],b)
                            
                    else:
                        print("Disk {} moved from B to C".format(b[-1]))
                        push(b[-1],c)
                        pop(b[-1],b)

if __name__ == "__main__":
    n = int(input("Enter the number of disks:\n"))
    move(n)
