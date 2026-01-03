#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>


int main(void)
{
    char *s = "hello";
    char *t = malloc(strlen(s));

    // copy content of s to t.
    for (int i = 0, n = strlen(s); i <= n; i++) {
        t[i] = s[i];
    }

    t[0] = toupper(s[0]);

    printf("%s\n", s);
    printf("%s\n", t);
}
