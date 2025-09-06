#include<stdio.h>

void initializeArray(int arr[], int size){
    for (int i=0; i<size; i++){
        arr[i] = 0;
    }
}

void displayArray(int arr[], int limit){
    printf("Displaying the array: ");
    for (int i=0; i<=limit; i++){
        printf("%d ", arr[i]);
    }
}

int deleteValue(int arr[], int size, int limit, int pos){
    if (pos>=1 && pos<=size){
        if (pos-1<=limit){
            for (int i=pos-1; i<limit; i++){
                arr[i] = arr[i+1];
            }
            arr[limit] = 0;
            limit--;
        }
    }
    return limit;
}

int main(){

    int limit=7; //takes values from 0
    int arr[10] = {10,20,30,40,50,60,70,80,0,0};    

    displayArray(arr,limit);

    int pos, val;
    printf("\nEnter a position to delete from: ");
    scanf("%d", &pos);

    limit = deleteValue(arr, 10, limit, pos);
    displayArray(arr,limit);
    printf("\nlimit %d",limit);

    return 0;
}