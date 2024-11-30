#include <stdio.h> 
void main()
{
int i=1, j=2;
i=i%2, j=j%2;
if(i==0)
{
printf("%d",j);
}
else
{
printf("%d",i);
}
}
