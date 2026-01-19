
def find_bottleneck_index(traceroute):
    largest_jump = 0
    bottleneck_index = 0

    for i in range(len(traceroute) - 1):
        hop1 = traceroute[i]
        hop2 = traceroute[i + 1]

        jump = abs(hop2[1] - hop1[1])

        if jump > largest_jump:
            largest_jump = jump
            bottleneck_index = i

    return bottleneck_index






# Test
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1
