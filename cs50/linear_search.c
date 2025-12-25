#include <stdio.h>



int main(void)
{
    bool is_found = false;
    int target = 7;
    int numbers[] = {1, 2, 3, 4, 5};
    int length = sizeof(numbers) / sizeof(numbers[0]);

    for (int i=0; i < length; i++) {
        if (numbers[i] == target) {
            is_found = true;
            break;
        }
    }
    if (is_found) {
        printf("Target found.\n");
    } 
    else {
        printf("Target not found.\n");
    }

}
