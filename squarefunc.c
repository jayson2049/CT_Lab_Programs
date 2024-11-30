#include<stdio.h>
int square(int);
int main()
{
  int num, res;
  printf("Enter the number, good hunter\n");
  scanf("%d",&num);
  res=square(num);
  printf("The square is %d = %d, good hunter\n", num, res);
}
int square(int x)
{
  return (x*x);
}
