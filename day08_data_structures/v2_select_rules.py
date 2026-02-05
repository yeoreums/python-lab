sizes = {
    "S":[(160, 180), (85, 95), (70, 80)],
    "M":[(170, 190), (90, 100), (75, 85)]
    }
measurements = [175, 92, 78]

result = "OK"

for i, (low, high) in zip(measurements, sizes["S"]):
    if i < low:
        result = "Down"
        break
    elif i > high:
        result = "Up"
        break

print(result)