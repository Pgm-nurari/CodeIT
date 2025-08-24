#include<stdio.h>
#include<stdlib.h>

struct node {
    struct node *leftptr;
    int data;
    struct node *rightptr;
};

struct node *createNode(int value){
    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    if (newNode!=NULL){
        newNode->data=value;
        newNode->leftptr=NULL;
        newNode->rightptr=NULL;
    }
}

void insertNode(struct node *temp,int value){
    if (value<temp->data){
        if (temp->leftptr == NULL) {temp->leftptr = createNode(value);}
        else{ insertNode(temp->leftptr,value);}
    }
    else if(value>temp->data){ 
        if (temp->rightptr == NULL) { temp->rightptr = createNode(value);}
        else { insertNode(temp->rightptr,value);}
    }
    else{
        return;
    }
}

void inorder(struct node *temp){
    if (temp!=NULL){
        inorder(temp->leftptr);
        printf("%d ",temp->data);
        inorder(temp->rightptr);
    }else{
        return ;
    }
}

void postorder(struct node *temp){
    if (temp!=NULL){
        postorder(temp->leftptr);
        postorder(temp->rightptr);
        printf("%d ", temp->data);
    }
    else{
        return;
    }
}

void preorder(struct node *temp){
    if (temp!=NULL){
        printf("%d ", temp->data);
        postorder(temp->leftptr);
        postorder(temp->rightptr);
    }
    else{
        return;
    }
}


int main() {
    int num,choice;
    do {
        printf("\n1. Create Node\n2. Insert Node\n3. Inorder Display\n4. Postorder Display\n5. Preorder Display\n0. Exit...\nEnter your choice: ");
        scanf("%d",&choice);
        switch (choice) {
            case 1:
            printf("Enter the number to be created as a node:");
            scanf("%d", &num);
            struct node *root = createNode(num);
            break;
            case 2:
            printf("Enter the number to be inserted into tree:");
            scanf("%d", &num);
            insertNode(root, num);
            break;
            case 3:
            printf("Inorder display of binary search tree is:\n");
            inorder(root);
            break;
            case 4:
            printf("Postorder display of binary search tree is:\n");
            postorder(root);
            break;
            case 5:
            printf("Preorder display of binary search tree is:\n");
            preorder(root);
            break;
            case 0:
            exit(0);
            default :
            printf("Invalid Choice!");
        }
    }while (choice!=0);
    return 0;
}