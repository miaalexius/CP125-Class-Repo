def calculate_xp_required(current_level):
    return current_level * 100 


def can_level_up(current_xp, required_xp):
    return current_xp >= required_xp


def calculate_final_level(total_xp):
    level = 1
    remaining_xp = total_xp

    while can_level_up(remaining_xp, calculate_xp_required(level)):
        remaining_xp -= calculate_xp_required(level)
        level += 1

    return level


def calculate_remaining_xp(total_xp):
    level = 1
    remaining_xp = total_xp

    while remaining_xp >= calculate_xp_required(level):
        remaining_xp -= calculate_xp_required(level)
        level += 1

    return remaining_xp
