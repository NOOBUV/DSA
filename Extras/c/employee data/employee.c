#include "employee.h"
#include <stdio.h>
#include <string.h>

#define MaxEmp 10

struct emp
{
    char lastname[16];
    char firstname[11];
    int salary;
};

static struct emp Employee[MaxEmp];
static int numEmp = 0;
// addEmployee
int addEmployee()
{
    if (numEmp == MaxEmp)
    {
        return -1;
    }

    printf("Enter the lastname of Employee: ");
    fflush(stdout);
    fgets(Employee[numEmp].lastname, 16, stdin);
    printf("%d\n", strlen(Employee[numEmp].lastname));
    if (strlen(Employee[numEmp].lastname) == 1)
        return -1;
    printf("Enter the firstname of Employee: ");
    fflush(stdout);
    fgets(Employee[numEmp].firstname, 11, stdin);
    printf("Enter the salary of Employee: ");
    fflush(stdout);
    scanf("%d", &Employee[numEmp].salary);
    getchar();

    return numEmp++;
}

// printEmployee
int printEmployee(int i)
{
    if (i < 0 || i >= numEmp)
        return -1;
    printf("{%s, %s, %d}\n", Employee[i].lastname, Employee[i].firstname, Employee[i].salary);
    return i;
}

// numEmployees
int numEmployees()
{
    return numEmp;
}
