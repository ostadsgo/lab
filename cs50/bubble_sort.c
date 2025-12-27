#include <stdio.h>




int main(void) 
{
    int values[] = {7, 2, 5, 4, 1, 6, 0, 3};
    bool swapped = false;
    for (int i=0; i < 8; i++) {
        for (int j=0; j < 8 - i - 1; j++) {
            // swape
            if (values[j+1] < values[j]) {
                int temp = values[j];
                values[j] = values[j+1];
                values[j + 1] = temp;
            }
            swapped = true;
        }
        if (!swapped)
            break;
    }
    for (int i = 0; i < 8; i++) {
        printf("%d ", values[i]);
    }
    printf("\n");
}
