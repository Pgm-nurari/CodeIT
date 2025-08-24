#include<stdio.h>

void createArray(int *arrPtr, int *p){
    for (int i=0; i<*p; i++){
        printf("Enter a element: ");
        scanf("%d",( arrPtr + i ));
    }
}

void printArrayRange(int *arrPtr,int *start,int *p){
    for (int i=*start; i<*p; i++){
        printf("%d ",*( arrPtr + i ));
    }
}

void printArray(int *arrPtr,int *p){
    for (int i=0; i<*p; i++){
        printf("%d ",*( arrPtr + i ));
    }
}

void dupArray(int *arr, int *len, int *new_arr){
    for (int i=0;i<*len;i++){
        *(new_arr + i) = *(arr + i);
    }
}

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}