#include<stdio.h>

void traverse(int arr[], int size){
    printf("\nDisplaying the array: ");
    for(int i=0;i<size;i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void traverseCharArray(char arr[], int size){
    printf("\nDisplaying the array: ");
    for(int i=0;i<size;i++){
        printf("%c ", arr[i]);
    }
    printf("\n");
}

int insertValue(int arr[], int size, int limit, int value, int position){
    int index = position-1;
    if (limit<size-1){
        if (index<0 || index>size){
            printf("\nPosition entered is out of range.");
            return -1;
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
            return -1;
        }
    }
    else{
        printf("\nLimit of the array exceeded. Array not empty.");
    }
}

int deleteValue(int arr[], int size, int limit, int position){
    int index = position-1;
    if (index<0 || index>size){
        printf("\nPosition entered is out of range.");
        return -1;
    }
    else if(index>limit){
        printf("\nArray empty at given position... Enter value!");
    }
    else if(index<=limit){
        int delValue = arr[index];
        for (int i=index; i<limit;i++){
            arr[i]=arr[i+1];
        }
        arr[limit]=0;
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

void displayAtEven(int arr[], int limit){
    printf("\nDisplaying the array: ");
    for(int i=1;i<=limit;i+=2){
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void displayAllOddNumbers(int arr[], int limit){
    printf("\nDisplaying all odd numbers: ");
    for(int i=0;i<=limit;i++){
        if (arr[i]%2!=0)
            printf("%d ",arr[i]);
    }
    printf("\n");
}

void displayAlternates(int arr[], int limit){
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

char updateCharArrayValue(char arr[], int size, int limit, int position, char value) {
    int index = position - 1; 
    if (index < 0 || index >= size) {
        printf("\nPosition entered is out of range.");
        return '\0'; // null char to indicate error
    }
    char previousValue = arr[index];
    arr[index] = value;
    if (index > limit) {
        printf("\nNote: You updated a position beyond current limit.");
    }
    return previousValue;
}

void displayCharAtMid(char arr[], int limit){
    if (limit%2!=0){
        printf("%c %c", arr[(limit/2)], arr[(limit/2)+1]);
    }
    else{
        printf("%c",arr[(limit/2)]);
    }
}

int main(){
    char charArray[10] = {'a','b','c','d','e',' ',' ',' ',' ',' '};

    traverseCharArray(charArray,10);

    updateCharArrayValue(charArray,10,4,3,'z');

    traverseCharArray(charArray,10);

    displayCharAtMid(charArray,3);
    return -1;
}