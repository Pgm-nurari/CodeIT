#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *nextptr;
};

struct node *head = NULL;

void creatingNodes() {
    int n, i;
    printf("\nEnter the number of nodes: ");
    scanf("%d", &n);

    if (n <= 0) { printf("Invalid number of nodes. Exiting..."); return; }

    struct node *temp = NULL, *newNode = NULL;

    for (i = 0; i < n; i++) {
        newNode = (struct node *)malloc(sizeof(struct node));
        if (newNode == NULL) { printf("Memory allocation failed. Exiting..."); return; }
        printf("Enter the data for Node - %d: ", i + 1);
        scanf("%d", &(newNode->data));
        newNode->nextptr = NULL;
        if (temp == NULL) { head = newNode; temp = head; }
        else { temp->nextptr = newNode; temp = newNode; }
    }
}

void display() {
    struct node *temp = head;
    printf("Displaying the elements in the Linked List: ");
    while (temp != NULL) { printf(" %d", temp->data); temp = temp->nextptr; }
    if (head == NULL) { printf("\nNo Linked List exists, or it might be empty. Either create a new Linked List or try Entering data into it."); }
}

void deleteNode(struct node **target) {
    if (*target != NULL) { struct node *temp = (*target)->nextptr; free(*target); *target = temp; }
    else { printf("No Linked List found. Create a new Linked List."); }
}

void deletionBegin() { deleteNode(&head); }

void deletionEnd() {
    struct node *temp = head;
    if (temp == NULL) { printf("No Linked List found. Create a new Linked List."); return; }
    if (temp->nextptr == NULL) { free(temp); head = NULL; }
    else {
        while (temp->nextptr != NULL) {
            if (temp->nextptr->nextptr == NULL) {
                free(temp->nextptr);
                temp->nextptr = NULL;
            } else { temp = temp->nextptr; }
        }
    }
}

void deletionRandom() {
    int pos;
    printf("Enter the position of the element: ");
    scanf("%d", &pos);
    if (pos == 1) { deletionBegin(); }
    else {
        struct node *temp = head;
        int count;
        for (count = 1; count < pos - 1; count++) {
            temp = temp->nextptr;
        }
        if (temp != NULL && temp->nextptr != NULL) {
            struct node *temp2 = temp->nextptr;
            temp->nextptr = temp2->nextptr;
            temp = temp->nextptr;
            free(temp2);
        }
    }
}

void insertNode(struct node **target, int position) {
    if (*target != NULL || position == 1) {
        struct node *newNode = (struct node *)malloc(sizeof(struct node));
        if (newNode == NULL) { printf("Memory allocation failed. Exiting..."); return; }
        printf("Enter the data for the new Node: ");
        scanf("%d", &(newNode->data));
        if (position == 1) { newNode->nextptr = *target; *target = newNode; }
        else {
            struct node *temp = *target;
            int i;
            for (i = 1; i < position - 1; i++) {
                if (temp == NULL) { printf("Invalid position. Exiting..."); free(newNode); return; }
                temp = temp->nextptr;
            }
            newNode->nextptr = temp->nextptr;
            temp->nextptr = newNode;
        }
    } else { printf("No Linked List found. Create a new Linked List."); }
}

void insertBegin() { insertNode(&head, 1); }

void insertEnd() {
    struct node *temp = head;
    if (temp == NULL) { printf("No Linked List exists. Create a new Linked List."); }
    else {
        while (temp->nextptr != NULL) { temp = temp->nextptr; }
        insertNode(&temp, 2);
    }
}

void insertRandom() {
    int pos;
    printf("Enter the position of the node to be replaced: ");
    scanf("%d", &pos);
    insertNode(&head, pos);
}

int main() {
    int choice;
    do {
        printf("\n1. Create Nodes\n2. Display\n3. Delete from Beginning\n4. Delete from End\n5. Delete at Position\n6. Insert at Beginning\n7. Insert at End\n8. Insert at Position\n0. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1: creatingNodes(); break;
            case 2: display(); break;
            case 3: deletionBegin(); break;
            case 4: deletionEnd(); break;
            case 5: deletionRandom(); break;
            case 6: insertBegin(); break;
            case 7: insertEnd(); break;
            case 8: insertRandom(); break;
            case 0: printf("Exiting..."); break;
            default: printf("Invalid choice. Please enter a valid option."); break;
        }
    } while (choice != 0);
    return 0;
}
