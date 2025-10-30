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
    int n;
    Stack s;
    printf("\nEnter the size of the stack: ");
    scanf("%d",&n);

    initialize(&s, n);

    printf("%d", s.size); // Size of the Stack!

}