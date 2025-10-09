#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* head = NULL;

Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void createList(int n) {
    if (n <= 0) {
        printf("Invalid number of nodes\n");
        return;
    }
    Node *newNode, *temp;
    for (int i = 0; i < n; i++) {
        int data;
        printf("Enter data for node %d: ", i + 1);
        scanf("%d", &data);
        newNode = createNode(data);
        if (head == NULL) {
            head = newNode;
            head->next = head;
        } else {
            temp = head;
            while (temp->next != head)
                temp = temp->next;
            temp->next = newNode;
            newNode->next = head;
        }
    }
}

void displayList() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    Node* temp = head;
    printf("\nCircular Singly Linked List Visualization:\n");
    printf("HEAD -> ");
    do {
        printf("[%d] -> ", temp->data);
        temp = temp->next;
    } while (temp != head);
    printf("HEAD\n");
}

void insertFirst(int data) {
    Node* newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
        head->next = head;
        return;
    }
    Node* temp = head;
    while (temp->next != head)
        temp = temp->next;
    newNode->next = head;
    temp->next = newNode;
    head = newNode;
}

void insertLast(int data) {
    Node* newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
        head->next = head;
        return;
    }
    Node* temp = head;
    while (temp->next != head)
        temp = temp->next;
    temp->next = newNode;
    newNode->next = head;
}

void deleteFirst() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    if (head->next == head) {
        free(head);
        head = NULL;
        return;
    }
    Node* temp = head;
    while (temp->next != head)
        temp = temp->next;
    Node* del = head;
    head = head->next;
    temp->next = head;
    free(del);
}

void deleteLast() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    if (head->next == head) {
        free(head);
        head = NULL;
        return;
    }
    Node *temp = head, *prev = NULL;
    while (temp->next != head) {
        prev = temp;
        temp = temp->next;
    }
    prev->next = head;
    free(temp);
}

int main() {
    int choice, data, n;
    while (1) {
        printf("\n--- Circular Singly Linked List Menu ---\n");
        printf("1. Create List\n2. Display List\n3. Insert at First\n4. Insert at Last\n5. Delete First\n6. Delete Last\n7. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter number of nodes: ");
                scanf("%d", &n);
                createList(n);
                break;
            case 2:
                displayList();
                break;
            case 3:
                printf("Enter data: ");
                scanf("%d", &data);
                insertFirst(data);
                displayList();
                break;
            case 4:
                printf("Enter data: ");
                scanf("%d", &data);
                insertLast(data);
                displayList();
                break;
            case 5:
                deleteFirst();
                displayList();
                break;
            case 6:
                deleteLast();
                displayList();
                break;
            case 7:
                exit(0);
            default:
                printf("Invalid choice\n");
        }
    }
    return 0;
}
