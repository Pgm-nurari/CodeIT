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

int insertValue(int arr[], int size, int limit, int pos, int val){
    if (pos<=size){
        if (limit<size-1){
            for (int i = limit; i>=pos-1; i--){
                arr[i+1] = arr[i];
            }
            arr[pos-1] = val;
            limit++;
            printf("\nValue inserted in the array.");
        }
        else{
            printf("\nArray is full..!");
        }
    }
    else{
        printf("\nPosition entered is invald..! Greater than size.");
    }
    return limit;
}

int main(){

    int limit=6; //takes values from 0
    int arr[10] = {10,20,30,40,50,70,80,0,0,0};    

    displayArray(arr,limit);

    int pos, val;
    printf("\nEnter a position and a value: ");
    scanf("%d %d", &pos, &val);

    limit = insertValue(arr, 10, limit, pos, val);
    displayArray(arr,limit);
    printf("\nlimit %d",limit);

    return 0;
}