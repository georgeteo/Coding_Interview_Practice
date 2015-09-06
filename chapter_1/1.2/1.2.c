/* CCC 1.2: Use C or C++ to make a funciton void reverse(char *s), which
reverses a string. */

#include <stdlib.h> 
#include <stdio.h>
#include <string.h> 

/* Version that mallocs new array, but does not work
since the memory address of the string s is passed on the stack
and so you cannot change it in the callee (main) by changing it locally 
Wrong version*/

void reverse_1(char * s) {
	printf("%d\n", strlen(s));
	char *new_s = malloc(strlen(s) + 1);
	printf("Here Okay\n");
	for (int n = strlen(s) - 1; n >= 0; n--){
		int m = strlen(s) - 1 - n;
		printf("%d, %d, %c \n", m, n, s[n]); 
		new_s[m] = s[n];
	}
	s = new_s;
	printf("%s\n", s);
}	

/* Version 2: changes the string at the memory address that is passed in
through the function call 
Correct/Working Version. 

Complexity: O(n)
*/
void reverse_2(char *s){
	int n = strlen(s);
	for (int i = 0; i < n/2; i++){
		int j = n - 1 - i;
		printf("%c, %c \n", s[i], s[j]);
		/* Use C char as bytes trick to do swap without using temp var
		Will only work for letters. */
		s[i] = s[i] + s[j];
		s[j] = s[i] - s[j];
		s[i] = s[i] - s[j];
	}
}	

int main(){
	char test_string[] = "apples";
	printf("Input String: %s\n", test_string);
	reverse_1(test_string);
	printf("Flipped String: %s\n", test_string);

	printf("Input String 2: %s\n", test_string);
	reverse_2(test_string);
	printf("Fipped String 2: %s\n", test_string);

	char test_string_2[] = "apple";
	printf("Input String 3: %s\n", test_string_2);
	reverse_2(test_string_2);
	printf("Fipped String 3: %s\n", test_string_2);
	
}
