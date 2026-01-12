
def was_backward_detected(waypoints):
    for i in range(len(waypoints) - 1):
        if (waypoints[i][0] > waypoints[i + 1][0] or
            waypoints[i][1] > waypoints[i + 1][1]):
            return True
    return False

