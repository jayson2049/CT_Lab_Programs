#include <stdio.h>
int linear(int a[], int n, int key);
int main() {
  int a[10], i, key, n;
   printf("How many elements, good hunter?\n");
   scanf("%d", &n);    printf("Just go out and enter the array elements:\n");
    for(i = 0; i < n; ++i) {
        scanf("%d", &a[i]);
    }
    printf("Tonight, Gehrman joins the hunt:\n");
    scanf("%d", &key);
    linear(a, n, key);
    return 0;
}
int linear(int a[], int n, int key) {
  int i;
   for(i = 0; i < n; i++) {
       if(a[i] == key) {
           printf("The hunt is at its end! PREY SLAUGHTERED! \n", i);
           printf("I will now show you mercy.\n");
           return 0;
       }
   }
   printf("The hunt has failed and the night shall resume!\n");
   printf("Yharnam's done fer, I tell ya!\n");
   return 0;
}
