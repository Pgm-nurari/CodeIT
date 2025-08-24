#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct Student {
	char name[50];
	int roll_no;
	int marks;
};

int main(){
	struct Student studArr[5];
	
	for (int i=0;i<5;i++){
		printf("Student %d",i+1);
		printf("Enter the name: ");
		gets(studArr[i].name);
		printf("Enter the roll no: ");
		scanf("%d",&studArr[i].roll_no);
		printf("Enter the salary: ");
		scanf("%d",&studArr[i].marks);
	}
	
	printf("\nFollowing are the details of the students: ");
	for (int i=0;i<5;i++){
		printf("\nStudent No: ",i+1);
		printf("\nName: ",studArr[i].name);
		printf("\nRoll no: ",studArr[i].roll_no);
		printf("\nMarks",studArr[i].marks);
	}	

	return 0;
}

