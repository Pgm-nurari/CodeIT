#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

Node *front = NULL;
Node *rear = NULL;

bool isEmpty() {
    return front == NULL;
}

void enqueue() {
    int data;
    printf("Enter data to enqueue: ");
    scanf("%d", &data);

    Node *newNode = (Node *)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("\nHeap Overflow! Cannot create node.\n");
        return;
    }
    newNode->data = data;
    newNode->next = NULL;

    if (isEmpty()) {
        front = newNode;
        rear = newNode;
    } else {
        rear->next = newNode;
        rear = newNode;
    }
    printf("%d enqueued to queue\n", data);
}


int dequeue() {
    Node *temp = front;
    int data = temp->data;

    if (front == rear) {
        front = NULL;
        rear = NULL;
    } else {
        front = front->next;
    }
    free(temp);
    return data;
}


void display() {
    if (isEmpty()) {
        printf("\nQueue is empty.\n");
        return;
    }
    Node *temp = front;
    printf("\nQueue (Front to Rear):\n");
    printf("FRONT -> ");
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("REAR\n");
}

int main() {
    int choice, dequeued_val;

    while (1) {
        printf("\n--- Integer Linear Queue Menu (Linked List) ---\n");
        printf("1. Enqueue (Add)\n");
        printf("2. Dequeue (Remove)\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("-------------------------------------------------\n");
        printf("Enter your choice: ");

        if (scanf("%d", &choice) != 1) {
            while (getchar() != '\n');
            printf("Invalid input. Please enter a number.\n");
            continue;
        }

        switch (choice) {
            case 1:
                enqueue();
                break;
            case 2:
                if (isEmpty()) {
                    printf("\nQueue Underflow! Cannot dequeue.\n");
                } else {
                    dequeued_val = dequeue();
                    printf("\nDequeued element: %d\n", dequeued_val);
                }
                break;
            case 3:
                display();
                break;
            case 4:
                printf("Exiting program. Freeing queue...\n");
                while (!isEmpty()) {
                    dequeue();
                }
                exit(0);
            default:
                printf("Invalid choice. Please enter 1-4.\n");
        }
    }
    return 0;
}