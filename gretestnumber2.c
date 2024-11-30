#include <stdio.h>

int main() {
    int n1, n2, n3;
    printf("Enter the numbers: ");
    scanf("%d %d %d", &n1, &n2, &n3);  // Fixed the syntax for scanf

    // Removed the semicolons after the if statements
    if ((n1 > n2) && (n1 > n3)) {
        printf("%d is the greatest\n", n1);
    } else if ((n2 > n1) && (n2 > n3)) {
        printf("%d is the greatest\n", n2);
    } else {
        printf("%d is the greatest\n", n3);
    }

    return 0;
}
