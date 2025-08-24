#include<stdio.h>

void traverseCharArray(char arr[], int size){
    printf("\nDisplaying the array: ");
    for(int i=0;i<size;i++){
        printf("%c ", arr[i]);
    }
    printf("\n");
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