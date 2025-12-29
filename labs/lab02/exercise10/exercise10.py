
def calculate_base_usage(distance):
    usage = distance / 10
    return usage * 1.5

def apply_mode_bonus(usage, is_sport_mode):
    if is_sport_mode:
        return usage * 1.5  
    
    else : 
        return usage 

def has_enough_battery(distance, current_battery, is_sport_mode):
    round_trip_distance = distance * 2

    base_usage = calculate_base_usage(round_trip_distance)
    total_usage = apply_mode_bonus(base_usage, is_sport_mode)

    return current_battery >= total_usage