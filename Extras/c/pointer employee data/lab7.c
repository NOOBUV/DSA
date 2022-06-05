#include "employ2.c"
#include <stdio.h>
#include <stdlib.h>

#define MAXEMPS 5

int main()
{
    struct Employee *emps[MAXEMPS];
    struct Employee *p;
    int i, nemps = 0;

    emps[nemps++] = createEmployee("Mantle", "Mickey", 58);
    emps[nemps++] = createEmployee("Maris", "Roger", 60);
    if (emps[nemps - 1]->salary != 61)
        emps[nemps - 1]->salary = 61;
    p = createEmployee("", "", 0);
    setLast(p, "kaline");
    setFirst(p, "Al");
    setSalary(p, 52);
    emps[nemps++] = p;

    for (i = 0; i < nemps; ++i)
    {
        printEmployee(emps[i]);
        putchar('\n');
        free(emps[i]);
    }
    return 0;
}