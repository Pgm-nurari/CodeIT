#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct Personal {
	char name[50];
	char date[50];
	int salary;
};

int main(){
	struct Personal p1;
	
	printf("Enter the name: ");
	gets(p1.name);
	printf("Enter the date of joining: ");
	gets(p1.date);
	printf("Enter the salary: ");
	scanf("%d",&p1.salary);
	
	printf("\nEntered details are: ");
	printf("\nName: %s\nDate of Join: %s\nSalary: %d\n",p1.name,p1.date,p1.salary);
	
	return 0;
}

