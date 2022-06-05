#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXWIDTH 81
#define MAXLINES 100

int main()
{
    char *lines[MAXLINES];
    char line[MAXWIDTH];
    int i, n;

    // store in a ragged array
    for (n = 0; n < MAXLINES && fgets(line, MAXWIDTH, stdin) != NULL; ++n)
    {
        if ((lines[n] = malloc(strlen(line) + 1)) == NULL)
            exit(1);
        strcpy(lines[n], line);
    }

    // print in reverse order
    for (i = 0; i < n; ++i)
    {
        puts(lines[n - i - 1]);
        free(lines[n - i - 1]);
    }

    return 0;
}