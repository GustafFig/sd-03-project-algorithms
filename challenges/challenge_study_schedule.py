def study_schedule(start_time, end_time, target_time):
    if len(end_time) == 0 or len(start_time) == 0:
        return 0

    count = 0
    for i in range(len(start_time)):
        if start_time[i] <= target_time <= end_time[i]:
            count += 1

    return count
