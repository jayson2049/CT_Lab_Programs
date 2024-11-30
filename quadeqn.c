#include<stdio.h>
#include<math.h>
int main()
{
int a,b,c,s,x,y,X;
printf("Enter the required values:");
scanf("%d%d%d",&a, &b, &c); 
s=(b*b)-(4*a*c);
switch(s>0?1:(s==0?0:-1))
{
case 0:
x=-b/(2*a);
printf("The roots are equal and real= %d",x);
break;
case 1:
x=(-b+sqrt(s))/(2*a);
y=(-b-sqrt(s))/(2*a);
printf("The roots are not equal and real= %d %d",x,y);
break;
default:
printf("The roots are non-existent\n");
}
return 0;
}
