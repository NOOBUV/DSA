def interval_covering():
    """ scheduling minimum visit times such that every visit covers maximum no of work done
         in a particular interval given in intervals array."""
    # intervals = input("Enter intervals (type:[[a,b],[c,d]]")
    intervals = [[1, 2], [2, 3], [3, 4], [2, 3], [3, 4], [4, 5]]
    intervals.sort(key=lambda x: x[1])
    minimum_visit_times, visit_at = [], intervals[0][1]
    for index in range(1, len(intervals)):
        if visit_at < intervals[index][0]:
            minimum_visit_times.append(visit_at)
            visit_at = intervals[index][1]
    minimum_visit_times.append(visit_at)
    print(minimum_visit_times)


interval_covering()
