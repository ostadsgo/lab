#include <stdio.h>
#include <string.h>



typedef struct {
    char *name;
    char *phone;
} Person;


int main(void)
{
    char target_name[100];

    Person contacts[3];
    // names
    contacts[0].name = "John";
    contacts[1].name = "Bob";
    contacts[2].name = "James";
    // phones
    contacts[0].phone = "123";
    contacts[1].phone = "321";
    contacts[2].phone = "456";

    printf("Enter contact name: ");
    scanf("%99s", target_name);

    for (int i = 0; i < 3; i++) {
        if (strcmp(target_name, contacts[i].name) == 0) {
            printf("Phone number is %s\n", contacts[i].phone);
            return 0;
        }
    }
    printf("Not found.\n");
}
