#include<stdio.h>
int main()
{
int n1,n2,n3;
printf("Enter the numbers:");
scanf("%d % d %d" &n1, &n2, &n3);
 if ((n1>n2) && (n2>n3));
    printf("%d is the greatest\n",n1)
 else
 if ((n2>n1) && (n2>n3));
    printf("%d is th greatest\n", n2)
 else
    printf("%d is the greatest\n",n3)
}
