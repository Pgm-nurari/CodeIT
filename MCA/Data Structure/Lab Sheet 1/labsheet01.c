#include<stdio.h>

void traverse(int arr[], int size){
    printf("\nDisplaying the array: ");
    for(int i=0;i<size;i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int insertValue(int arr[], int size, int limit, int value, int position){
    int index = position-1;
    if (limit<size-1){
        if (index<0 || index>size){
            printf("\nPosition entered is out of range.");
            return limit;
        }
        else if(limit<size-1){
            for (int i=limit;i>index-1;i--){
                arr[i+1]=arr[i];
            }
            arr[index]=value;
            limit++;
            return limit;
        }
        else if (position==size){
            arr[index]=value;
            limit++;
            return limit;
        }
        else{
            printf("\nEnter the insertion between the limits");
            return limit;
        }
    }
    else{
        printf("\nLimit of the array exceeded. Array not empty.");
        return size;
    }
}

int deleteValue(int arr[], int size, int* limit, int position){
    int index = position-1;
    if (index<0 || index>size){
        printf("\nPosition entered is out of range.");
        return -1;
    }
    else if(index>*limit){
        printf("\nArray empty at given position... Enter value!");
        return -1;
    }
    else if(index<=*limit){
        int delValue = arr[index];
        for (int i=index; i<*limit;i++){
            arr[i]=arr[i+1];
        }
        arr[*limit]=0;
        (*limit)--;
        return delValue;
    }
    else{
        printf("\nEnter the insertion between the limits");
        return -1;
    }
}

int searchInArray(int arr[], int limit, int key){
    for (int i=0; i<=limit; i++){
        if(arr[i]==key){
            printf("\n%d found at position %d", key, i+1);
            return i;
        }
    }
    printf("\n%d not found.", key);
    return 0;
}

void displayAllOddNumbers(int arr[], int limit){
    printf("\nDisplaying all odd numbers: ");
    for(int i=0;i<=limit;i++){
        if (arr[i]%2!=0)
            printf("%d ",arr[i]);
    }
    printf("\n");
}

void displayAtEven(int arr[], int limit){
    printf("\nDisplaying the values in the even position in the array: ");
    for(int i=1;i<=limit;i+=2){
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void displayAlternates(int arr[], int limit){
    printf("\nDisplaying elements at alternate positions: ");
    printf("\nDisplaying the array at even positions: ");
    for(int i=1;i<=limit;i+=2){
        printf("%d ", arr[i]);
    }
    printf("\n");
    printf("\nDisplaying the array at odd positions: ");
    for(int i=0;i<=limit;i+=2){
        printf("%d ", arr[i]);
    }
}

void reverseArray(int arr[], int limit){
    int mid = (limit/2);
    for (int i=0;i<=mid;i++){
        int temp = arr[i];
        arr[i] = arr[limit-i];
        arr[limit-i] = temp;
    }
}

int main(){
    int arr[10] = {0,0,0,0,0,0,0,0,0,0};
    int size = sizeof(arr)/sizeof(int);

    int limit, insertionPosition, insertionValue, deletePosition, keyValue;

    printf("\nEnter the limit (less than 10): ");
    scanf("%d", &limit);

    printf("Enter %d integers: ", limit);
    for (int i = 0; i < limit; i++){
        scanf("%d", &arr[i]);
    }

    traverse(arr, size);

    printf("\nEnter the value and position to be inserted: ");
    scanf("%d %d", &insertionPosition, &insertionValue);

    limit = insertValue(arr,10,limit-1,insertionValue, insertionPosition);
    traverse(arr, size);

    printf("\nEnter the position to delete from: ");
    scanf("%d", &deletePosition);

    printf("\nDeleted Value is: %d", deleteValue(arr,10,&limit,deletePosition));
    traverse(arr,size);

    int arr2[10] = {1,4,2,6,4,7,3,8,3,9};
    traverse(arr2,10);

    printf("\nEnter the value to search: ");
    scanf("%d", &keyValue);
    searchInArray(arr2, 10, keyValue);

    displayAllOddNumbers(arr2, 10);

    displayAtEven(arr2, 10);

    displayAlternates(arr2, 10);

    printf("\nReversing the array: ");
    reverseArray(arr2, 10);
    traverse(arr2,10);

    return 0;
}