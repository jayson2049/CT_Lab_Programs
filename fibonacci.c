#include<stdio.h>
#include<math.h>
int main()
{
int a=0,b=1,n,x;
printf("Enter n");
scanf("%d",&n);
int count=1;
while(count<=n)
{
if(count==1)
printf("%d",a);
else if(count==2)
printf("%d",b);
else
{
x=a+b;
printf("%d",x);
a=b;
b=x;
}
count++;
}
}
