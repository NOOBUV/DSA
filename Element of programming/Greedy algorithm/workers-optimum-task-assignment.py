def optimum_task_assignment():
    """
    Given a workload and a list of task weights, return a list of
    task assignments that optimizes the workload.
    """
    taskdurations = input("Enter task durations (type:array): ").split()
    taskdurations = [int(x) for x in taskdurations]
    taskdurations.sort()
    paired_tasks = []
    start, end = 0, len(taskdurations)-1
    while start < end:
        paired_tasks.append((taskdurations[start], taskdurations[end]))
        start += 1
        end -= 1
    print(paired_tasks)


optimum_task_assignment()
