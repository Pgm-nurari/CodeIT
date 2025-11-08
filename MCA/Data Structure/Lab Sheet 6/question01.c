#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Stack {
    int top;
    int size;
    int *arr;
} Stack;

void initialize(Stack *s, int size) {
    s->size = size;
    s->top = -1;
    s->arr = (int *)malloc(size * sizeof(int));
    if (s->arr == NULL) {
        printf("\nMemory allocation failed!");
        exit(1);
    }
}

bool isFull(Stack *s) {
    return s->top == s->size - 1;
}

bool isEmpty(Stack *s) {
    return s->top == -1;
}

void push(Stack *s) {
    if (isFull(s)) {
        printf("\nStack Overflow\n");
    } else {
        int data;
        printf("Enter data to push: ");
        scanf("%d", &data);
        s->top++;
        s->arr[s->top] = data;
        printf("%d pushed to stack\n", data);
    }
}

int pop(Stack *s) {
    int data = s->arr[s->top];
    s->top--;
    return data;
}

void display(Stack *s) {
    if (isEmpty(s)) {
        printf("\nStack is empty\n");
    } else {
        printf("\nStack (Top to Bottom):\n");
        for (int i = s->top; i >= 0; i--) {
            printf("%d\n", s->arr[i]);
        }
    }
}

int main() {
    int n, choice, popped_val;
    Stack s;
    printf("\nEnter the size of the stack: ");
    scanf("%d", &n);
    initialize(&s, n);

    while (1) {
        printf("\n--- Integer Stack Menu (Array) ---\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("------------------------------------\n");
        printf("Enter your choice: ");

        if (scanf("%d", &choice) != 1) {
            while (getchar() != '\n');
            printf("\nInvalid input. Please enter a number.\n");
            continue;
        }

        switch (choice) {
            case 1:
                push(&s);
                break;
            case 2:
                if (isEmpty(&s)) {
                    printf("\nStack Underflow! Cannot pop.\n");
                } else {
                    popped_val = pop(&s);
                    printf("\nPopped element: %d\n", popped_val);
                }
                break;
            case 3:
                display(&s);
                break;
            case 4:
                printf("\nExiting. Freeing memory...\n");
                free(s.arr);
                exit(0);
            default:
                printf("\nInvalid choice. Please enter 1-4.\n");
        }
    }
    return 0;
}