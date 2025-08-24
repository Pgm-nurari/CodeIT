#include<stdio.h>
#include<stdlib.h>

int n;

struct node {
    int data;
    struct node *nextptr;

}*head,*newNode,*temp,*end;

void creatingNodes(){
    printf("\nEnter the number of nodes");
    scanf("%d",&n);
    head=malloc(sizeof(struct node));
    if (head!=NULL && n>0){
        printf("Enter the data for Node - 1: ");
        scanf("%d",&(head->data));
        head->nextptr = NULL;
        temp = head;
        if (n>1){
            for (int i=1;i<n-1;i++){
                newNode = malloc(sizeof(struct node));
                if (newNode!=NULL){
                    printf("Enter the data for Node - %d: ",i+1);
                    scanf("%d",&(newNode->data));
                    newNode->nextptr = NULL;
                    temp->nextptr = newNode;
                    temp = newNode;
                }
            }
            end = malloc(sizeof(struct node));
            temp->nextptr = end;
            printf("Enter the final node data: ");
            scanf("%d",&(end->data));
            end->nextptr = NULL;
            temp = end;
        }
    }
    else{
        printf("Could not create the linked list.");
        free(head);
    }
}

void display(){
    temp = head;
    int count = 0;
    printf("Displaying the elements in the Linked List: \n");
    while(temp!=NULL){
        printf(" %d",temp->data);
        temp = temp->nextptr;
        count++;
    }
    if (count == 0){ printf("\nNo Linked List exists, or it might be empty.\nEither create a new Linked List or try Entering data into it.");}
}

void insertBegin(){
    if (head!=NULL){
        newNode = malloc(sizeof(struct node));
        if (newNode!=NULL){
            printf("Enter the data for the new Node: ");
            scanf("%d",&(newNode->data));
            newNode->nextptr = head;
            head = newNode;
        }
        else{
            printf("Could not create a Node...");
        }
    }
    else{
        printf("Create a Linked List first, by selecting option 1 in the menu.");
    }    
}

void insertEnd(){
    temp = head;
    if (temp == NULL){
        printf("No Linked List exists, pls create a new Linked List by selecting option 1 in the main menu.");
    }
    else{
        newNode = malloc(sizeof(struct node));
        if (newNode!=NULL){
            while (temp->nextptr!=NULL){ temp=temp->nextptr;}
            printf("Enter the data for the new Node: ");
            scanf("%d",&(newNode->data));
            temp->nextptr = newNode;
            newNode->nextptr = NULL;
            temp = newNode;
        }
        else{
            printf("Node could not be created");
        }
    }
}

void insertRandom(){
    int pos;
    printf("Enter the position of the node to be replaced: ");
    scanf("%d",&pos);
    temp = head;
    if (pos==1 || temp==NULL){
        printf("No Linked List exists, pls create a new Linked List by selecting option 1 in the main menu.");
    }
    else{
        newNode = malloc(sizeof(struct node));
        if (newNode!=NULL){
            printf("Enter the data for the new Node: ");
            scanf("%d",&(newNode->data));
            for (int i=1; i<=pos-2;i++){
                temp = temp->nextptr;
            }
            newNode->nextptr = temp->nextptr;
            temp->nextptr = newNode;
        }
        else{
            printf("Could not create a Node...");
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
        printf("3. Inserting at the End\n4. Inserting at a Random Position\n");
        printf("5. Display the List\n6. Exit\n");
        printf("\nEnter your choice: ");
        scanf("%d",&ch);

        switch(ch){
            case 1 :
                creatingNodes();
                continue;
            case 2:
                insertBegin();
                continue;
            case 3:
                insertEnd();
                continue;
            case 4:
                insertRandom();
                continue;
            case 5:
                display(&n);
                continue;
            case 6:
                printf("Exiting... the Menu...!\n\n");
                exit(0);
                break;
            default:
                printf("Invalid Option");
        }
    }
    return 0;
}