#include <stdio.h>
int main() {
int n = 292;
int m, o, p;

p = n % 10; 
n = n / 10; 
o = n % 10; 
m = n / 10; 
printf("The digits are: %d, %d, %d\n", m, o, p);
printf("The reversed order is: %d, %d, %d\n", p, o, m);
if	(292 == 292)
{
	printf("The givern number is a palindromic sequence\n");
}
else
{
	printf("The given number is NOT a palindromic sequence\n");
	}
}
