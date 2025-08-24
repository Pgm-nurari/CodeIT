#include<stdio.h>
#include<stdlib.h>
#define size 5

void push(int arr[],int *top){
    if (*top>=size-1){
        printf("Stack Overflow.");
    }
    else{
        printf("Enter the item: ");
        *top = *top+1;
        scanf("%d",&arr[*top]);
        printf("\nItem Inserted");
    }
}

void pop(int arr[],int *top){
    if (*top==-1){
        printf("Stack underflow");
    }
    else{
        int item = arr[*top];
        *top = *top-1;
        printf("\n%d was popped out.",item);
    }
}

void display(int arr[], int *top){
    if (*top==-1){
        printf("Nothing to print here, Enter something into the Stack!\n");
        push(arr,top);
    }
    else{
        printf("\nStack Elements: ");
        for (int i=0;i<=*top;i++){
            printf("%d ",arr[i]);
        }
        printf("\n");
    }
        
}

void menu(int arr[],int *top){
    int ch=0;
    printf("\n1. To push an element\n2. To Pop an element\n3. To display the element\n4.To exit");
    printf("\nEnter your decision: ");
    scanf("%d",&ch);
    switch(ch){
        case 1:
            push(arr,top);menu(arr,top);
        case 2:
            pop(arr,top);menu(arr,top);
        case 3:
            display(arr,top);menu(arr,top);
        case 4:
            exit(0);
        case 5:
            printf("Invalid choice!...");
            menu(arr,top);
    }
}

int main(){
    int arr[size];
    int top=-1;

    menu(arr,&top);

}