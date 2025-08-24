#include<stdio.h>
#include<stdlib.h>
#define size 3

void enqueue(int arr[],int *front, int *rear){
    if (*rear!=size-1){
        *rear=*rear+1;
        if (*front==-1){ *front=*front+1; }
        printf("\nEnter the element: ");
        scanf("%d",&arr[*rear]);
        printf("\nElement added.");
    }
    else{
        printf("Queue Overflow.");
    }
}

void dequeue(int arr[],int *front, int *rear){
    if (*front == -1){
        printf("\nQueue Underflow.");
    }
    else{
        int item = arr[*front];
        printf("\nThe deleted element from the queue is: %d",item);
        if (*front==*rear){ *rear = -1; *front = -1;}
        else{ *front=*front+1; }
    }
}

void display(int arr[],int *front,int *rear){
    printf("\n");
    for (int i=*front;i<=*rear;i++){
        printf("%d ",arr[i]);
    }
}

int main(){
    int queue[size];
    int front = -1;
    int rear = -1;
    int x=0;
    while (x==0){
        printf("\n\n..................\n       MENU\n..................");
        printf("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit\nEnter your choice: ");
        int ch;
        scanf("%d",&ch);
        switch(ch){
            case 1:
                enqueue(queue,&front,&rear);
                break;
            case 2:
                dequeue(queue,&front,&rear);
                break;
            case 3:
                display(queue,&front,&rear);
                break;
            case 4:
                exit(0);
                x=1;
                break;
            default:
                printf("Invalid Option! Please Re-select!");
                break;
        }
    }
    return 0;
}