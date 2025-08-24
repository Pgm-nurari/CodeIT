#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};
struct Node *head = NULL;
struct Node *createNode(int data) {
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed.\n");
        exit(EXIT_FAILURE);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void insertNode() {
    int data;
    printf("Enter data to insert: ");
    scanf("%d", &data);
    struct Node *newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
        head->next = head;
    } else {
        struct Node *temp = head;
        while (temp->next != head) {
            temp = temp->next;
        }
        newNode->next = head;
        temp->next = newNode;
    }
    printf("Node with data %d inserted.\n", data);
}

void deleteNode() {
    if (head == NULL) {
        printf("List is empty. Nothing to delete.\n");
        return;
    }
    struct Node *temp = head;
    struct Node *prev = NULL;
    while (temp->next != head) {
        prev = temp;
        temp = temp->next;
    }
    if (temp == head && temp->next == head) {
        free(temp);
        printf("Node deleted. List is now empty.\n");
        head = NULL;
        return;
    }
    prev->next = head;
    if (temp == head) {
        head = head->next;
    }
    printf("Last node deleted.\n");
    free(temp);
}

void displayList() {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }
    struct Node *current = head;
    printf("Circular Linked List: ");
    do {
        printf("%d -> ", current->data);
        current = current->next;
    } while (current != head);

    printf("(head)\n");
}


int main() {
    int choice;
    do {
        printf("\nCircular Linked List Operations Menu:\n");
        printf("1. Insert Node\n");
        printf("2. Delete Node\n");
        printf("3. Display List\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                insertNode();
                break;
            case 2:
                deleteNode();
                break;
            case 3:
                displayList();
                break;
            case 4:
                printf("Exiting the program.\n");
                break;
            default:
                printf("Invalid choice. Please enter a valid option.\n");
        }
    } while (choice != 4);
    return 0;
}
