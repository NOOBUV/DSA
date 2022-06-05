#include "employ2.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Employee *
createEmployee(char *last, char *first, int salary)
{
    struct Employee *p = malloc(sizeof(struct Employee));
    if (p != NULL)
    {
        strcpy(p->last, last);
        strcpy(p->first, first);
        p->salary = salary;
    }
    return p;
}

char *getLast(struct Employee *p)
{
    return p ? p->last : "";
}

char *getFirst(struct Employee *p)
{
    return p ? p->first : "";
}

int getSalary(struct Employee *p)
{
    return p ? p->salary : 0;
}

void setLast(struct Employee *p, char *last)
{
    if (p != NULL)
        strcpy(p->last, last);
}
void setFirst(struct Employee *p, char *first)
{
    if (p != NULL)
        strcpy(p->first, first);
}
void setSalary(struct Employee *p, int salary)
{
    if (p != NULL)
        p->salary, salary;
}
void printEmployee(struct Employee *p)
{
    putchar('{');
    if (p != NULL)
    {
        printf("%s %s %d", p->last, p->first, p->salary);
    }
    putchar('}');
}