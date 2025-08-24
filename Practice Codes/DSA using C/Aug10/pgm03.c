//Swapping of 2 numbers
#include<stdio.h>
void main(){
	int a,b;
	scanf("%d%d",&a,&b);
	printf("Before swapping:\n a=%d b=%d\n",a,b);
	b=a+b;
	a=b-a;
	b=b-a;
	printf("After Swapping:\n a=%d b=%d\n",a,b);
}
