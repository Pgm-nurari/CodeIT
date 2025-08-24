#include<stdio.h>
#include<stdlib.h>

struct queueNode {
    int data;
    struct queueNode *nextptr;
}*front,*rear,*newNode,*temp;

void createQueue(){
    front = malloc(sizeof(struct queueNode));
    if (front!=NULL){
        printf("\nEnter the element: ");
        scanf("%d",&(front->data));
        front->nextptr = NULL;
        rear = front;
    }
}

void enqueue(){
    if (front == NULL){
        createQueue();
    }
    else{
        newNode=malloc(sizeof(struct queueNode));
        if (newNode!=NULL){
            printf("\nEnter the element: ");
            scanf("%d",&(newNode->data));
            rear->nextptr = newNode;
            newNode->nextptr=NULL;
            rear = newNode;            
        }
    }
}

void dequeue(){
    if (front==NULL){
        printf("Queue Underflow");
    }
    else if (front==rear){
        temp=front;
        printf("%d ",temp->data);
        front = rear = NULL;
        free(temp);
    }
    else{
        temp=front;
        printf("%d ",temp->data);
        front = temp->nextptr;
        free(temp);
    }
}

void display(){
    if (front!=NULL){
        temp = front;
        while(temp!=NULL){
            printf("%d ",temp->data);
            temp=temp->nextptr;
        }
    }
    else{
        printf("\nQueue not found.");
    }
}

int main(){
    front = rear = NULL;
    int x=0;
    while (x==0){
        printf("\n\n..................\n       MENU\n..................");
        printf("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit\nEnter your choice: ");
        int ch;
        scanf("%d",&ch);
        switch(ch){
            case 1:
                enqueue();
                break;
            case 2:
                dequeue();
                break;
            case 3:
                display();
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