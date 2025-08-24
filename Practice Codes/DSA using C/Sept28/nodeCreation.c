/*
So this is a program to create the linked list but, it has 'n' no. of 
nodes to store the data, and also has extra two nodes, that represent
the Head and End of the Linked List.
*/

#include<stdio.h>
#include<stdlib.h>

struct node {
    int data;
    struct node *nextptr; // The pointer is of struct datatype, since it points to a container that is a structure.
}*head,*temp,*newNode,*end;

int main(){
    int n;
    printf("Enter the number of nodes to be created: ");
    scanf("%d",&n);
    head = malloc(sizeof(struct node));
    if (head==NULL){
        printf("Head of the node could not be created.");
        exit(0);
    }
    else{
        temp = malloc(sizeof(struct node));
        if (temp!=NULL){
            printf("Enter the data for node-1: ");
            scanf("%d",&(temp->data));
            head->nextptr = temp;
            temp->nextptr = NULL;

            for (int i=1;i<n;i++){
                newNode = malloc(sizeof(struct node));
                if (newNode!=NULL) {
                    printf("Enter the data for node-%d: ",i+1);
                    scanf("%d",&(newNode->data));
                    temp->nextptr = newNode;
                    newNode->nextptr = NULL;
                    temp = newNode;
                }
            }
        } 
        end = malloc(sizeof(struct node));
        temp->nextptr = end;
        end->nextptr = NULL;
    }
    

    printf("Printing the nodes data: \n");
    temp = (head->nextptr);
    while (temp->nextptr!=NULL){
        printf(" %d", temp->data);
        temp = temp->nextptr;
    }

    return 0;
}