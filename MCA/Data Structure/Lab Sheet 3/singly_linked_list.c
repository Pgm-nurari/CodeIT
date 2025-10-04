#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* head = NULL;

Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void createList(int n) {
    if (n <= 0) {
        printf("Invalid size\n");
        return;
    }
    int val;
    Node* temp;
    for (int i = 0; i < n; i++) {
        printf("Enter value for node %d: ", i + 1);
        scanf("%d", &val);
        Node* newNode = createNode(val);
        if (head == NULL) {
            head = newNode;
            temp = head;
        } else {
            temp->next = newNode;
            temp = newNode;
        }
    }
}

void displayList() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    Node* temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

void searchValue(int key) {
    Node* temp = head;
    int pos = 1;
    while (temp != NULL) {
        if (temp->data == key) {
            printf("Value %d found at position %d\n", key, pos);
            return;
        }
        temp = temp->next;
        pos++;
    }
    printf("Value %d not found\n", key);
}

int countNodes() {
    int count = 0;
    Node* temp = head;
    while (temp != NULL) {
        count++;
        temp = temp->next;
    }
    return count;
}

void displayAlternate() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    Node* temp = head;
    int flag = 1;
    while (temp != NULL) {
        if (flag)
            printf("%d ", temp->data);
        flag = !flag;
        temp = temp->next;
    }
    printf("\n");
}

void displayEvenPositioned() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    Node* temp = head;
    int pos = 1;
    while (temp != NULL) {
        if (pos % 2 == 0)
            printf("%d ", temp->data);
        temp = temp->next;
        pos++;
    }
    printf("\n");
}

void findMiddle() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    int total = countNodes();
    int mid1 = total / 2;
    int mid2 = (total % 2 == 0) ? mid1 + 1 : mid1 + 1;

    Node* temp = head;
    int pos = 1;
    while (temp != NULL) {
        if (total % 2 == 0 && (pos == mid1 || pos == mid2)) {
            printf("Middle Node %d: %d\n", (pos == mid1) ? 1 : 2, temp->data);
        } else if (total % 2 != 0 && pos == mid2) {
            printf("Middle Node: %d\n", temp->data);
        }
        temp = temp->next;
        pos++;
    }
}

void insertFirst(int data) {
    Node* newNode = createNode(data);
    newNode->next = head;
    head = newNode;
}

void insertLast(int data) {
    Node* newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
        return;
    }
    Node* temp = head;
    while (temp->next != NULL)
        temp = temp->next;
    temp->next = newNode;
}

void insertAfter(int key, int data) {
    Node* temp = head;
    while (temp != NULL && temp->data != key)
        temp = temp->next;
    if (temp == NULL) {
        printf("Node %d not found\n", key);
        return;
    }
    Node* newNode = createNode(data);
    newNode->next = temp->next;
    temp->next = newNode;
}

void insertBefore(int key, int data) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    if (head->data == key) {
        insertFirst(data);
        return;
    }
    Node* prev = NULL;
    Node* temp = head;
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }
    if (temp == NULL) {
        printf("Node %d not found\n", key);
        return;
    }
    Node* newNode = createNode(data);
    prev->next = newNode;
    newNode->next = temp;
}

void insertBetween(int key1, int key2, int data) {
    Node* temp = head;
    while (temp != NULL && temp->next != NULL) {
        if (temp->data == key1 && temp->next->data == key2) {
            Node* newNode = createNode(data);
            newNode->next = temp->next;
            temp->next = newNode;
            return;
        }
        temp = temp->next;
    }
    printf("Nodes %d and %d not found adjacent\n", key1, key2);
}

void insertAtPosition(int pos, int data) {
    if (pos <= 0) {
        printf("Invalid position\n");
        return;
    }
    if (pos == 1) {
        insertFirst(data);
        return;
    }
    Node* temp = head;
    for (int i = 1; i < pos - 1 && temp != NULL; i++)
        temp = temp->next;
    if (temp == NULL) {
        printf("Position out of range\n");
        return;
    }
    Node* newNode = createNode(data);
    newNode->next = temp->next;
    temp->next = newNode;
}

void deleteFirst() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    Node* temp = head;
    head = head->next;
    free(temp);
}

void deleteLast() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    if (head->next == NULL) {
        free(head);
        head = NULL;
        return;
    }
    Node* temp = head;
    while (temp->next->next != NULL)
        temp = temp->next;
    free(temp->next);
    temp->next = NULL;
}

void deleteAfter(int key) {
    Node* temp = head;
    while (temp != NULL && temp->data != key)
        temp = temp->next;
    if (temp == NULL || temp->next == NULL) {
        printf("No node exists after %d\n", key);
        return;
    }
    Node* del = temp->next;
    temp->next = del->next;
    free(del);
}

void deleteBefore(int key) {
    if (head == NULL || head->next == NULL) {
        printf("Not enough nodes\n");
        return;
    }
    if (head->next->data == key) {
        deleteFirst();
        return;
    }
    Node* prev = NULL;
    Node* temp = head;
    while (temp->next != NULL && temp->next->data != key) {
        prev = temp;
        temp = temp->next;
    }
    if (temp->next == NULL) {
        printf("Node %d not found\n", key);
        return;
    }
    prev->next = temp->next;
    free(temp);
}

void deleteBetween(int key1, int key2) {
    Node* temp = head;
    while (temp != NULL && temp->next != NULL && temp->next->next != NULL) {
        if (temp->data == key1 && temp->next->next->data == key2) {
            Node* del = temp->next;
            temp->next = del->next;
            free(del);
            return;
        }
        temp = temp->next;
    }
    printf("No node found between %d and %d\n", key1, key2);
}

void deleteAtPosition(int pos) {
    if (pos <= 0 || head == NULL) {
        printf("Invalid position\n");
        return;
    }
    if (pos == 1) {
        deleteFirst();
        return;
    }
    Node* temp = head;
    for (int i = 1; i < pos - 1 && temp != NULL; i++)
        temp = temp->next;
    if (temp == NULL || temp->next == NULL) {
        printf("Position out of range\n");
        return;
    }
    Node* del = temp->next;
    temp->next = del->next;
    free(del);
}

void reverseList() {
    Node* prev = NULL;
    Node* curr = head;
    Node* next = NULL;
    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    head = prev;
}

int main() {
    int choice, n, val, key, key1, key2, pos;
    printf("Enter number of nodes to create: ");
    scanf("%d", &n);
    createList(n);

    while (1) {
        printf("\nMenu:\n");
        printf("1. Display list\n");
        printf("2. Search value\n");
        printf("3. Count nodes\n");
        printf("4. Display alternate nodes\n");
        printf("5. Display even positioned nodes\n");
        printf("6. Find middle node(s)\n");
        printf("7. Insert first\n");
        printf("8. Insert last\n");
        printf("9. Insert after\n");
        printf("10. Insert before\n");
        printf("11. Insert between 2 nodes\n");
        printf("12. Insert at a position\n");
        printf("13. Delete first\n");
        printf("14. Delete last\n");
        printf("15. Delete after\n");
        printf("16. Delete before\n");
        printf("17. Delete between 2 nodes\n");
        printf("18. Delete at a position\n");
        printf("19. Reverse the list\n");
        printf("20. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: displayList(); break;
            case 2: printf("Enter value: "); scanf("%d", &val); searchValue(val); break;
            case 3: printf("Total nodes: %d\n", countNodes()); break;
            case 4: displayAlternate(); break;
            case 5: displayEvenPositioned(); break;
            case 6: findMiddle(); break;
            case 7: printf("Enter value: "); scanf("%d", &val); insertFirst(val); break;
            case 8: printf("Enter value: "); scanf("%d", &val); insertLast(val); break;
            case 9: printf("Enter key and value: "); scanf("%d %d", &key, &val); insertAfter(key, val); break;
            case 10: printf("Enter key and value: "); scanf("%d %d", &key, &val); insertBefore(key, val); break;
            case 11: printf("Enter 2 keys and value: "); scanf("%d %d %d", &key1, &key2, &val); insertBetween(key1, key2, val); break;
            case 12: printf("Enter position and value: "); scanf("%d %d", &pos, &val); insertAtPosition(pos, val); break;
            case 13: deleteFirst(); break;
            case 14: deleteLast(); break;
            case 15: printf("Enter key: "); scanf("%d", &key); deleteAfter(key); break;
            case 16: printf("Enter key: "); scanf("%d", &key); deleteBefore(key); break;
            case 17: printf("Enter 2 keys: "); scanf("%d %d", &key1, &key2); deleteBetween(key1, key2); break;
            case 18: printf("Enter position: "); scanf("%d", &pos); deleteAtPosition(pos); break;
            case 19: reverseList(); break;
            case 20: exit(0);
            default: printf("Invalid choice\n");
        }
    }
    return 0;
}
