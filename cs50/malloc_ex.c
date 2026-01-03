#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

char *str_copy(char *s) {
    char *t = malloc(strlen(s) + 1);

    for (int i = 0, n = strlen(s); i <= n; i++) {
        t[i] = s[i];
    }

    return t;
}

int main(void)
{
    char *s = "something";
    char *t = str_copy(s);
    if (t == NULL) return 1;
    //
    // // copy content of s to t.
    // for (int i = 0, n = strlen(s); i <= n; i++) {
    //     t[i] = s[i];
    // }

    if (strlen(t) > 0) {
        t[0] = toupper(s[0]);
    }

    printf("%s\n", s);
    printf("%s\n", t);
}
