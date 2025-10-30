#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

typedef struct stack{
    int top;
    int size;
    int *arr;
}Stack;

void initialize(Stack *s, int size){
    s->size = size;                                 //(*s).size = size;
    s->top = -1;                                    // (*s).top = -1;
    s->arr = (int *)malloc(size * sizeof(int));     // (*s).arr = (int *)malloc(size * sizeof(int)); 

    if (s->arr==NULL){
        printf("\nMemory allocation failed!");
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

int getTop(Stack *s){
    return s->top;
}

int pop(Stack *s){
    if (isEmpty(s)){
        printf("\nUnderflow!!");
    }
    else{
        int del = s->arr[s->top];
        s->top--;
        return del;
    }
}

void push(Stack *s){
    if (isFull(s)){
        printf("\nOverflow!!");
    }
    else{
        int data;
        printf("\nEnter the data: ");
        scanf("%d", &data);
        s->top++;
        s->arr[s->top] = data;
    }
}

void peek(Stack *s){
    if (isEmpty(s)){
        printf("\nThe Stack is Empty\n");
    }
    else{
        printf("\nTop element is: %d\n", s->arr[s->top]);
    }
}

void display(Stack *s){
    if (isEmpty(s)){
        printf("\nThe Stack is Empty");
    }
    else{
        printf("\n");
        for(int i = s->top; i >= 0; i--){
            printf("%d ", s->arr[i]);
        }
    }
}

int main(){
    int n, choice, popped_val;
    Stack s;
    printf("\nEnter the size of the stack: ");
    scanf("%d",&n);

    initialize(&s, n);

    while(1){
        printf("\n--- Stack Menu (Array) ---\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Display\n");
        printf("4. Peek (Show Top)\n");
        printf("5. Exit\n");
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
                    printf("\nPopped element: %d\n", popped_val);
                }
                break;

            case 3:
                display(&s);
                break;
            
            case 4:
                peek(&s);
                break;

            case 5:
                printf("\nExiting program. Freeing memory...\n");
                free(s.arr);
                exit(0);

            default:
                printf("\nInvalid choice. Please enter a number between 1 and 5.\n");
        }
    }

    return 0;
}