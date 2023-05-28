def min_arrows_rotation(_string):
    counts = {'^': 0, 'v': 0, '<': 0, '>': 0}

    for arrow in _string:
        counts[arrow] += 1

    max_count = max(counts.values())
    total_arrows = len(_string)
    rotations = total_arrows - max_count

    return rotations


print(min_arrows_rotation("^vv<v^^v>>^<<<"))
print(min_arrows_rotation("v>^v>^v^v<>>^v"))
print(min_arrows_rotation("^<v<v<^"))
