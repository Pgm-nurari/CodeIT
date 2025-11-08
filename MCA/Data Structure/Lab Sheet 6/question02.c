#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
    char data;
    struct Node *next;
} Node;

Node *top = NULL;

bool isEmpty() {
    return top == NULL;
}

void push() {
    char data;
    printf("Enter character to push: ");
    scanf(" %c", &data);
    
    Node *newNode = (Node *)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("\nHeap Overflow! Cannot create node.\n");
        return;
    }
    newNode->data = data;
    newNode->next = top;
    top = newNode;
    printf("Pushed: %c\n", data);
}

char pop() {
    Node *temp = top;
    char popData = temp->data;
    top = top->next;
    free(temp);
    return popData;
}

void display() {
    if (isEmpty()) {
        printf("\nStack is empty.\n");
        return;
    }
    Node *temp = top;
    printf("\nStack (Top to Bottom):\n");
    printf("TOP -> ");
    while (temp != NULL) {
        printf("%c -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

int main() {
    int choice;
    char popped_val;

    while (1) {
        printf("\n--- Character Stack Menu (Linked List) ---\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("--------------------------------------------\n");
        printf("Enter your choice: ");

        if (scanf("%d", &choice) != 1) {
            while (getchar() != '\n');
            printf("Invalid input. Please enter a number.\n");
            continue;
        }
        while (getchar() != '\n');

        switch (choice) {
            case 1:
                push();
                break;
            case 2:
                if (isEmpty()) {
                    printf("\nStack Underflow! Cannot pop.\n");
                } else {
                    popped_val = pop();
                    printf("Popped: %c\n", popped_val);
                }
                break;
            case 3:
                display();
                break;
            case 4:
                printf("Exiting program. Freeing stack...\n");
                while (!isEmpty()) {
                    pop();
                }
                exit(0);
            default:
                printf("Invalid choice. Please enter 1-4.\n");
        }
    }
    return 0;
}