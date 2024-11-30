#include <stdio.h>
int main()
{
int x,h,m,s;
printf("Input time in seconds [x] :");
scanf("%d", &x);
m = x/60;
h = m/60;
s = x%60;
printf("The given integer is %d hours, %d minutes and %d seconds \n", h,m,s);
}
