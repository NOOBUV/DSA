#include "employee.c"
#include <stdio.h>

int main()
{
    int i;
    // Fill employee array
    while (addEmployee() != -1)
        ;
    // print each employee
    for (i = 0; i < numEmployees(); ++i)
    {
        printEmployee(i);
        putchar('\n');
    }
    return 0;
}