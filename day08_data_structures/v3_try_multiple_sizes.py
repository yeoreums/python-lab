sizes = {
    "S": [(160, 180), (85, 95), (70, 80)],
    "M": [(170, 190), (90, 100), (75, 85)],
    "L": [(180, 200), (95, 105), (85, 95)],
}

measurements = [175, 92, 78]

found_size = None

for size_name in sizes:
    ranges = sizes[size_name]

    fits = True  # assume this size fits

    for value, (low, high) in zip(measurements, ranges):
        if value < low or value > high:
            fits = False
            break  # this size fails, stop checking it

    if fits:
        found_size = size_name
        break  # stop after first fitting size

if found_size:
    print(f"Customer fits size {found_size}")
else:
    print("No size fits")
