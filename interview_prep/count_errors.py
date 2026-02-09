def count_errors(logs):
    result = {}

    for line in logs:
        level = line.split(":")[0]
        result[level] = result.get(level, 0) + 1

    return result

logs = [
    "INFO:Start",
    "ERROR:Disk full",
    "WARNING:Low memory",
    "ERROR:Timeout",
    "INFO:End"
]

print(count_errors(logs))