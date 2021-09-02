def minimize_waiting_time():
    service_times = input("Enter query servicing time (type:arr): ").split()
    service_times = [int(i) for i in service_times]
    service_times.sort()
    minimum_waiting_time = 0
    N = len(service_times)
    for index in range(1, N):
        minimum_waiting_time += service_times[index-1]*(N-index)
    print(minimum_waiting_time)


minimize_waiting_time()
