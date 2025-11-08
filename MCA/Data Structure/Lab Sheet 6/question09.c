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
        printf("Memory allocation failed!\n");
        exit(1);
    }
}

bool isFull(Stack *s) {
    return s->top == s->size - 1;
}

bool isEmpty(Stack *s) {
    return s->top == -1;
}

void push(Stack *s, int data) {
    if (isFull(s)) {
        printf("Stack Overflow for data %d\n", data);
        return;
    }
    s->top++;
    s->arr[s->top] = data;
}

int pop(Stack *s) {
    if (isEmpty(s)) {
        printf("Stack Underflow\n");
        return -1; 
    }
    int data = s->arr[s->top];
    s->top--;
    return data;
}

void display(Stack *s, const char *name) {
    if (isEmpty(s)) {
        printf("\n%s Stack is empty\n", name);
    } else {
        printf("\n%s Stack (Top to Bottom):\n", name);
        for (int i = s->top; i >= 0; i--) {
            printf("%d\n", s->arr[i]);
        }
    }
}

int main() {
    int size = 10;
    Stack mainStack, oddStack, evenStack;
    
    initialize(&mainStack, size);
    initialize(&oddStack, size);
    initialize(&evenStack, size);

    printf("Pushing elements onto main stack: 1 to 10\n");
    for (int i = 1; i <= 10; i++) {
        push(&mainStack, i);
    }
    
    display(&mainStack, "Main");

    printf("\n...Sorting into Odd and Even Stacks...\n");
    while (!isEmpty(&mainStack)) {
        int data = pop(&mainStack);
        
        if (data % 2 == 0) {
            push(&evenStack, data);
        } else {
            push(&oddStack, data);
        }
    }

    display(&mainStack, "Main");
    display(&oddStack, "Odd");
    display(&evenStack, "Even");

    free(mainStack.arr);
    free(oddStack.arr);
    free(evenStack.arr);

    return 0;
}