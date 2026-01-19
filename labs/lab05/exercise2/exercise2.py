
def find_largest_drop(readings):
    droplet = []
    for i in range (len(readings)-1) : 
        a = readings[i]
        b = readings[i+1]
        if readings[i] > readings[i+1]:
            drop = readings[i] - readings[i+1] 
            droplet.append(drop)

    if len(droplet) == 0 : 
        return 0.0
    
    largest_drop = max(droplet) 
    return largest_drop
        

# Test
temps = (100.0, 50.0, 60.0, 70.0)
result = find_largest_drop(temps)
print(f"Largest Drop: {result}")  # Expected: 3.5
