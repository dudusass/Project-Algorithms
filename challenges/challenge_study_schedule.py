def study_schedule(permanence, target_time):
    try:
        counter = 0
        for i in range(0, len(permanence)):
            if permanence[i][0] <= target_time <= permanence[i][1]:
                counter += 1
        return counter
    except TypeError:
        return None
