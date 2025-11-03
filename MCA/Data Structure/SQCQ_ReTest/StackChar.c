/*
    Character Stack Opertaions using Array
*/

#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

typedef struct Stack{
    int top;
    int size;
    char *arr;
}Stack;

void initialize(Stack *s, int size){
    s -> size = size;
    s -> top = -1;
    s -> arr = (char *)malloc(size * sizeof(char));

    if (s->arr==NULL){
        printf("\nMemory Allocation Failed");
    }
}

bool isFull(Stack *s){
    if (s->top == s->size -1){
        return true;
    }
    else{
        return false;
    }
}

bool isEmpty(Stack *s){
    if (s->top == -1){
        return true;
    }
    else{
        return false;
    }
}

char pop(Stack *s){
    if (isEmpty(s)){
        printf("\nUnderflow!!");
        return '\0';
    }
    else{
        char del = s->arr[s->top];
        s->top--;
        return del;
    }
}

void push(Stack *s){
    if (isFull(s)){
        printf("\nOverflow!!");
    }
    else{
        char data;
        // Clear the input buffer before reading character
        while (getchar() != '\n');
        printf("\nEnter the data: ");
        scanf("%c", &data);
        s->top++;
        s->arr[s->top] = data;
    }
}

void display(Stack *s){
    if (isEmpty(s)){
        printf("\nThe Stack is Empty");
    }
    else{
        printf("\n");
        for(int i = s->top; i >= 0; i--){
            printf("%c ", s->arr[i]);
        }
    }
}

int main(){
    int n, choice;
    char popped_val;
    Stack s;
    printf("\nEnter the size of the stack: ");
    scanf("%d",&n);

    initialize(&s, n);

    while(1){
        printf("\n--- Character Stack Menu (Array) ---\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("----------------------------\n");
        printf("Enter your choice: ");

        if (scanf("%d", &choice) != 1) {
            while (getchar() != '\n');
            printf("\nInvalid input. Please enter a number.\n");
            continue;
        }

        switch (choice){
            case 1:
                push(&s);
                break;

            case 2:
                if (isEmpty(&s)){
                    printf("\nUnderflow!! Cannot pop.\n");
                }
                else{
                    popped_val = pop(&s);
                    printf("\nPopped element: %c\n", popped_val);
                }
                break;

            case 3:
                display(&s);
                break;

            case 4:
                printf("\nExiting program. Freeing memory...\n");
                free(s.arr);
                exit(0);

            default:
                printf("\nInvalid choice. Please enter a number between 1 and 5.\n");
        }
    }

    return 0;
}