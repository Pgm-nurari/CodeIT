#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *preptr;
}*top,*newNode,*temp;

void createNode(){
    top = NULL;
    newNode = malloc(sizeof(struct node));
    if (newNode!=NULL){
        printf("Enter value: ");
        scanf("%d",&(newNode->data));
        newNode->preptr=NULL;
        top = newNode;
    }
}

void push(){
    if (top==NULL){
        createNode();
    }
    else{
        newNode=malloc(sizeof(struct node));
        if (newNode!=NULL){
            printf("Enter value: ");
            scanf("%d",&(newNode->data));
            newNode->preptr=top;
            top = newNode;
        }
    }
}

void display(){
    temp = top;
    if (temp==NULL){
        printf("\nStack is Empty!");
    }
    else{
        printf("\nPrinting the data: ");
        while (temp != NULL) {
            printf("%d ", temp->data);
            temp = temp->preptr;
            }
    }
}

void pop(){
    if (top==NULL){
        printf("\nStack Underflow\n");
    }
    else{
        if (top->preptr==NULL){
            printf("%d\n",top->data);
            free(top);
            top=NULL;
        }
        else{
            printf("%d\n",top->data);
            temp=top;
            top = top->preptr;
            free(temp);
        }
    }
}

int main(){
    int choice;
    while (1){
        printf("\n1.Push\n2.Pop\n3.Display\n4.Exit\n");
        printf("Enter your choice: ");
        scanf("%d",&choice);
        switch (choice){
            case 1:
                push();
                break;
            case 2:
                pop();
                break;
            case 3:
                display();
                break;
            case 4:
                exit(0);
            default:
                printf("\nWrong choice, try again.\n");
        }
    }
    return 0;    
}
