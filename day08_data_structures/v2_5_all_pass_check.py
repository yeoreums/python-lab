ranges = [(160, 180), (85, 95), (70, 80)]
measurements = [175, 92, 78]

fits = True
result = "OK"

for i, (low, high) in zip(measurements, ranges):
    if i < low or i > high:
        result = "Not ok"
        fits = False
        break

print(result)        
