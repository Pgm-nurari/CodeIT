#include<stdio.h>
#define len 5

int main(){
    printf("\nEnter 5 elements: \n");
    int arr[len];
    for (int i=0;i<len;i++){
        printf("Enter an integer: ");
        scanf("%d",&arr[i]);
    }
    
    int res = 0;
    for (int i=0; i<len; i++){
        res = res + arr[i];
    }
    printf("\nSum of elements in the array is: %d",res);
    return 0;
}