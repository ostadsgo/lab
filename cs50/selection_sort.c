#include <stdio.h>


/* Find the smallest number in the list and swap it with 
 * current number.
**/

int main(void)
{
    int nums[] = { 7, 2, 5, 4, 1, 6, 0, 3 };
    int smallest_value = nums[0];
    int smallest_index = 0;

    // find smallest
    for (int i = 0; i < 8; i++) {
        smallest_value = nums[i];
        smallest_index = i;

        // Update smallest value and index if found.
        for (int j = i; j < 8; j++) {
            if (nums[j] < smallest_value)
                smallest_value = nums[j];
                smallest_index = j;
        }
        // swap the current element with smallest 
        nums[smallest_index] = nums[i];
        nums[i] = smallest_value;
    }

    for (int i = 0; i < 8; i++) {
        printf("%d ", nums[i]);
    }
    printf("\n");

}
