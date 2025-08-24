#include<stdio.h>
#include<stdlib.h>

struct node {
    struct node *preptr;
    int data;
    struct node *nextptr;
    

}*head,*newNode,*temp,*end;

void creatingNodes(){
    int n;
    printf("\nEnter the number of nodes");
    scanf("%d",&n);
    head=malloc(sizeof(struct node));
    if (head!=NULL && n>0){
        head->preptr=NULL;
        printf("Enter the data for first node: ");
        scanf("%d",&(head->data));
        head->nextptr = NULL;
        temp = head;
        if (n>1){
            for (int i=1;i<n-1;i++){
                newNode = malloc(sizeof(struct node));
                if (newNode!=NULL){
                    newNode->preptr=temp;
                    printf("Enter the data for the node: ");
                    scanf("%d",&(newNode->data));
                    newNode->nextptr = NULL;
                    temp->nextptr = newNode;
                    temp = newNode;
                }
            }
            end=malloc(sizeof(struct node));
            end->preptr=temp;
            temp->nextptr = end;
            printf("Enter the data for the last node: ");
            scanf("%d",&(end->data));
            end->nextptr=NULL;
            temp=end;
        }
    }
    else{
        printf("Could not create the linked list.");
    }
}

void displayForward(){
    printf("Printing data from forward: \n");
    if (head!=NULL){
        temp=head;
        do{
            printf("%d -> ",temp->data);
            temp=temp->nextptr;
        }while(temp!=NULL);
    }
    else{
        printf("Create a Linked List before printing.");
    }
}

void displayBackward(){
    printf("Printing data from backward: \n");
    if (end!=NULL){
        temp=end;
        do{
            printf("%d -> ",temp->data);
            temp=temp->preptr;
        }while(temp!=NULL);
    }
    else{
        printf("Create a Linked List before printing.");
    }
}

void insertBegin(){
    if (head!=NULL){
        temp=head;
        newNode = malloc(sizeof(struct node));
        newNode->preptr = NULL;
        temp->preptr = newNode;
        newNode->nextptr = temp;
        printf("Enter data for the new node: ");
        scanf("%d",&(newNode->data));
        head = newNode;
    }
}

void insertEnd(){
    if (head!=NULL){
        temp=head;
        while(temp->nextptr!=NULL){
            temp=temp->nextptr;
        }
        end=malloc(sizeof(struct node));
        temp->nextptr = end;
        end->preptr=temp;
        end->nextptr = NULL;
        printf("Enter the data for the last Node: ");
        scanf("%d",&(end->data));
        temp=end;
    }
}

void deleteBegin(){
    if (head==NULL){
        printf("Create a Linked List to delete from.");
    }
    else{
        temp=head->nextptr;
        temp->preptr = NULL;
        free(head);
        head = temp;
    }
}

void deleteEnd(){
    if (head==NULL){
        printf("Create a Linked List to delete from.");
    }
    else if(head->nextptr==NULL){
        head=NULL;
        free(head);
        printf("All the elements in the Linked List are deleted");
    }
    else{
        temp=head;
        while(temp!=NULL){
            if((temp->nextptr)->nextptr==NULL){
                end = (temp->nextptr)->nextptr;
                free(end);
                temp->nextptr = NULL;
                break;
            }
            else{
                temp = temp->nextptr;
            }
        }
    }
}

int main(){
    
    int ch=1;
    while (ch>0){
        printf("\n\n");
        printf("*------------------------------------*\n");
        printf("            MENU CHOICE               \n");
        printf("*------------------------------------*\n");
        printf("1. Creation of Nodes\n2. Inserting node at the Beginning\n");
        printf("3. Inserting at the End\n4. Delete from begin\n5. Delete from the end");
        printf("\n6. Display forward\n7. Display Backward");
        printf("\n0. Exit\nEnter your choice: ");
        scanf("%d",&ch);

        switch(ch){
            case 1 :
                creatingNodes();
                break;
            case 2:
                insertBegin();
                break;
            case 3:
                insertEnd();
                break;
            case 4:
                deleteBegin();
                break;
            case 5:
                deleteEnd();
                break;
            case 6:
                displayForward();
                break;
            case 7:
                displayBackward();
                break;
            case 0:
                printf("Exiting... the Menu...!");
                break;
            default:
                printf("Invalid Option");
                continue;
        }
    }
    return 0;
}