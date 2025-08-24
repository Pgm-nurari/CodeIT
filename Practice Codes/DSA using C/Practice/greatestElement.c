#include<stdio.h>
#define size 5
int main(){
    int arr[size];
    printf("\nEnter 5 elements: \n");
    for (int i=0;i<size;i++){
        printf("Enter an integer: ");
        scanf("%d",&arr[i]);
    }
    int flag = arr[0];
    for (int i=1;i<size;i++){ 
        if (arr[i]>=flag){
            flag = arr[i];
        }
    }
    printf("\nGreatest element is: %d",flag);
    return 0;
}