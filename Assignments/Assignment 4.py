class Check:
    def __init__(self, MAX, TRUE, FALSE, ERROR, buffer, SP, A):
        self.MAX = MAX
        self.TRUE = TRUE
        self.FALSE = FALSE
        self.ERROR = ERROR
        self.buffer = buffer
        self.SP = SP
        self.A = A
    
    def IsEmpty(self):
        if(SP == 0):
            return TRUE

        else:
            return FALSE

    def IsFull(self):
        if(self.SP == (MAX - 1)):
            return TRUE

        else:
            return FALSE

    def push(self):
        full = Check(MAX, TRUE, FALSE, ERROR, buffer, SP, A)
        empty = Check(MAX, TRUE, FALSE, ERROR, buffer, SP, A)
        if(full.IsFull() == FALSE):
            if(empty.IsEmpty() == TRUE):
                A[SP] = input("Enter an element to be pushed:\n")

            else:
                for i in range(MAX):
                    if(i == None):
                        A.remove(None)
                        break

                self.SP += 1
                A[SP + 1] = input("Enter an element to be pushed:\n")

        else:
            return ERROR

    def pop(self):
        empty = Check(MAX, TRUE, FALSE, ERROR, buffer, SP, A)
        if(empty.IsEmpty() == FALSE):
            self.buffer = A[SP]
            try:
                A.remove(A[SP + 1])
                return buffer
            
            except:
                A.remove(A[SP])

        else:
            return ERROR

if __name__ == "__main__":
    #initialization for c
    MAX = 5
    TRUE = 1
    FALSE = 0
    ERROR = -1
    A = [None] * MAX
    SP = 0
    buffer = 0
    counter = MAX - 1

    SP = int(input("Enter how many elements are there:\n"))

    for i in range(SP):
        A[i] = input("Enter an element of the stack:\n")

    for i in range(MAX):
        if(A[counter] != None):
            SP = counter
            break

        counter -= 1

    push = Check(MAX, TRUE, FALSE, ERROR, buffer, SP, A)
    if(push.push() == -1):
        print("You cannot push more than MAX")

    else:
        empty = Check(MAX, TRUE, FALSE, ERROR, buffer, SP, A)
        if(empty.IsEmpty() == TRUE):
            print("{} has been pushed".format(A[SP]))
            print(A)

        else:
            print("{} has been pushed".format(A[SP + 1]))
            print(A)


    pop = Check(MAX, TRUE, FALSE, ERROR, buffer, SP, A)
    if(pop.pop() == -1):
        print("You cannot pop an empty stack")

    else:
        print("Top-most element has been popped from the stack")
        print(A)
