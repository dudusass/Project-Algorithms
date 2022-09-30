def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for i in range(0, len(permanence_period)):
            if permanence_period[i][0] <= target_time <= permanence_period[i][1]:
                counter += 1
        return counter
    except TypeError:
        return None



