'''def synchronize_databases(legacy_list, modern_set, blacklist):
    valid_legacy = set()
    for item in legacy_list:
        if item not in blacklist:
            valid_legacy.add(item)

    lost_set = valid_legacy - modern_set
    lost_id = list(lost_set)
    lost_idd = []

    for i in range (len(lost_id)): 
        new = lost_id[i][0]
        lost_idd.append(new)
    
    lost_set_id = set(lost_idd)
    ghost_set = modern_set - valid_legacy

    return (lost_set_id, ghost_set)

legacy = [(1, "a@b.com"), (2, "c@d.com")]
modern = {1, 3}
lost, ghost = synchronize_databases(legacy, modern, set())'''

def synchronize_databases(legacy_list, modern_set, blacklist):
    valid_legacy_ids = set()

    for item in legacy_list:
        id_num, email = item
        if email not in blacklist:
            valid_legacy_ids.add(id_num)

    lost_set = valid_legacy_ids - modern_set

    ghost_set = modern_set - valid_legacy_ids

    return (lost_set, ghost_set)
