#include <stdio.h>


/* Find the smallest number in the list and swap it with 
 * current number.
**/

int main(void)
{
    int nums[] = { 7, 2, 5, 4, 1, 6, 0, 3 };
    int min_index = 0;

    // find smallest
    for (int i = 0; i < 8; i++) {
        min_index = i;

        // Update smallest value and index if found.
        for (int j = i + 1; j < 8; j++) {
            if (nums[j] < nums[min_index]) {
                min_index = j;
            }
        }
        // swap the current element with smallest 
        int temp = nums[i];
        nums[i] = nums[min_index];
        nums[min_index] = temp;
    }

    for (int i = 0; i < 8; i++) {
        printf("%d ", nums[i]);
    }
    printf("\n");

}
