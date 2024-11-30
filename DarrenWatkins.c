#include <stdio.h>
int main()
{
int s,d,t;
printf("Enter distance travelled in km:");
scanf("%d", &d);
printf("Enter time period in hours:");
scanf("%d", &t);
s = d/t;
printf("The speed of the vehicle is %d km/h \n", s);
}
