#include<stdio.h>
#include<stdlib.h>

int n;

struct node {
    int data;
    struct node *nextptr;

}*head,*newNode,*temp,*end,*temp2;

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

void deletionBegin(){
    if (head==NULL){
        printf("No Liked List found, to delete from, create a new Linked List.");
    }
    else{
        temp = head->nextptr;
        free(head);
        head = temp;
    }
}

void deletionEnd(){
    if (head==NULL){
        printf("No Liked List found, to delete from, create a new Linked List.");
    }
    else if(head->nextptr==NULL){
        free(head);
    }
    else{
        temp = head;
        while (temp->nextptr!=NULL){
            if (((temp->nextptr)->nextptr)==NULL){
                end=(temp->nextptr)->nextptr;
                free(end);
                temp->nextptr = NULL;
            }
            else{
                temp=temp->nextptr;
            }
        }
    }
}

void deletionRandom(){
    if (head==NULL){
        printf("There is no linked list to delete from.");
    }
    else if (head->nextptr==NULL){
        head=NULL;
        free(head);
        printf("Final node also deleted.");
    }
    else{
        int pos;
        printf("Enter the position of the element: ");
        scanf("%d",&pos);
        if (pos==1){ deletionBegin();}
        else{
            temp=head;
            int count;
            for (count = 1;count<pos-1;count++){
                temp=temp->nextptr;
            }
            temp2=temp->nextptr;
            temp->nextptr=temp2->nextptr;
            temp=temp->nextptr;
            free(temp2);
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
        printf("1. Creation of Nodes\n2. Delete the First element\n");
        printf("3. Delete the Last element\n4. Delete element from random position.\n");
        printf("5. Display the List\n6. Exit");
        printf("\nEnter your choice: ");
        scanf("%d",&ch);

        switch(ch){
            case 1:
                creatingNodes();
                continue;
            case 5:
                display();
                continue;
            case 2:
                deletionBegin();
                continue;
            case 3:
                deletionEnd();
                continue;
            case 4:
                deletionRandom();
                continue;
            case 6:
                printf("Exiting...the Menu...!\n\n");
                exit(0);
                break;
            default:
                printf("Invalid Option");
        }
    }
    return 0;
}