ranges = [(160, 180), (85, 95), (70, 80)]
measurements = [175, 92, 78]

result = "OK"

for i, (low, high) in zip(measurements, ranges):
    if i < low:
        result = "Down"
        break
    elif i > high:
        result = "Up"
        break

print(result)