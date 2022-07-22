#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define MAX 3
#define TRUE 1
#define FALSE 0
#define QUEUEEMPTY 0
#define ERROR -1

//functional specifications
int enque(int);
int deque(void);
int IsQueueFull(void);
int IsQueueEmpty(void);

//Static Variables
static int Queue[MAX], QP = QUEUEEMPTY;

int main()
{
    int time = 0, largest = 0;

    while (IsQueueFull()==FALSE){
       printf("QP =  %d, ",QP);
       enque(rand()%100); 
    }

    printf("\n");

    while (IsQueueEmpty()==FALSE) {
        time = deque();
//Fill the logic to calculate the largest service time
    }
    
    printf("Largest service time = %d\n",largest);    

    return 0;
}

int enque(int a)
{
    if(IsQueueFull()==FALSE){
        printf("Service Time = %d\n",a);
        a = rand()
// Fill enque logic here to add service time to queue

        return(0);
    } else
        return(ERROR);
}

int IsQueueFull(void)
{
    if(QP==MAX){
        return(TRUE);   
    } 
    else {
        return(FALSE);
    }
}

int deque(void)
{
    int i,counter;
    
    i=0; counter = 0;
 
    if(IsQueueEmpty()==FALSE){
 //Fill the logic for removing the first element

    }
    else {
        return(ERROR);
    }
        
    for(counter=0;counter < QP; counter++){
 //Fill the logic to move all entries one place to front

    }
        
    QP = QP -1;
    return(i);
}

int IsQueueEmpty(void)
{
    if(QP==QUEUEEMPTY){
        return(TRUE);  
    } 
    else {
        return(FALSE);
    }
}
