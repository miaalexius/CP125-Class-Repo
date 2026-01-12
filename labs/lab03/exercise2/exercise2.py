def find_station(stations, name):
    for i in range (len(stations)): 
        if name == stations[i]:
            return i 
    return -1 

def count_stops(stations, start, stop):
    start_index = find_station(stations, start)
    stop_index = find_station (stations, stop)

    if start_index == -1 or stop_index == -1: 
        return -1
        
    if start_index == stop_index : 
        return 0 
    
    else: 
        count = stop_index - start_index
        return abs(count)  
    
