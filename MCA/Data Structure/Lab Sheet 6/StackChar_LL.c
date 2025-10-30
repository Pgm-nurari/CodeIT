#include <stdio.h>
#include <stdlib.h>

typedef struct Stack {
    char data;
    struct Stack *next;
} Stack;

Stack *top = NULL;

Stack *createNode(char data) {
    Stack *newNode = (Stack *)malloc(sizeof(Stack));
    if (newNode == NULL) {
        printf("\nHeap Overflow! Cannot create node.\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

int isEmpty() {
    return top == NULL;
}

void push(char data) {
    Stack *newNode = createNode(data);
    newNode->next = top;
    top = newNode;
    printf("Pushed: %c\n", data);
}

char pop() {
    if (isEmpty()) {
        printf("\nStack Underflow\n");
        return '\0';
    }
    
    Stack *temp = top;
    char popData = temp->data;
    top = top->next;
    free(temp);
    return popData;
}

void peek() {
    if (isEmpty()) {
        printf("Stack is empty.\n");
    } else {
        printf("Top element is: %c\n", top->data);
    }
}

void display() {
    if (isEmpty()) {
        printf("Stack is empty.\n");
        return;
    }
    
    Stack *temp = top;
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
    char data;
    char popped_val;

    while (1) {
        printf("\n--- Stack Menu (Linked List) ---\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Display\n");
        printf("4. Peek (Show Top)\n");
        printf("5. Exit\n");
        printf("-----------------------------------\n");
        printf("Enter your choice: ");

        if (scanf("%d", &choice) != 1) {
            while (getchar() != '\n');
            printf("Invalid input. Please enter a number.\n");
            continue;
        }

        while (getchar() != '\n');

        switch (choice) {
            case 1:
                printf("Enter character to push: ");
                scanf("%c", &data);
                push(data);
                break;
                
            case 2:
                popped_val = pop();
                if (popped_val != '\0') {
                    printf("Popped: %c\n", popped_val);
                }
                break;
                
            case 3:
                display();
                break;
                
            case 4:
                peek();
                break;
                
            case 5:
                printf("Exiting program. Freeing stack...\n");
                while (!isEmpty()) {
                    pop();
                }
                exit(0);
                
            default:
                printf("Invalid choice. Please enter a number between 1 and 5.\n");
        }
    }

    return 0;
}