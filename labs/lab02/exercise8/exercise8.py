def calculate_bounce_height(current_height):
    return current_height * 0.8


def is_ball_stopped(height):
    return height < 1


def calculate_bounce_count(initial_height):
    bounce_count = 0
    height = initial_height

    while True:
        if is_ball_stopped(height):
            break

        height = calculate_bounce_height(height)
        bounce_count += 1
    
    return bounce_count


def calculate_total_distance(initial_height):
    total_distance = initial_height 
    height = initial_height

    while True:
        height = calculate_bounce_height(height)
        total_distance += height

        if is_ball_stopped(height):
            break

        total_distance += height

    return total_distance