#ifndef EMPLOYEE_H
#define EMPLOYEE_H

struct Employee
{
    char last[16];
    char first[11];
    int salary;
};

struct Employee *
createEmployee(char *, char *, int);
char *getLast(struct Employee *);
char *getFirst(struct Employee *);
int getSalary(struct Employee *);
void setLast(struct Employee *, char *);
void setFirst(struct Employee *, char *);
void setSalary(struct Employee *, int);
void printEmployee(struct Employee *);

#endif