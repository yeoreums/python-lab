def most_error_service(logs):
    result = {}

    for log in logs:
        timestamp, service, level = log.split()
        if level == "ERROR":
            result[service] = result.get(service, 0) + 1

    # Preventing error if there's no "ERROR"
    if not result:
        return None

    return max(result, key=result.get)


logs = [
    "2026-02-08 api ERROR",
    "2026-02-08 api ERROR",
    "2026-02-08 web ERROR",
    "2026-02-08 db INFO"
]


print(most_error_service(logs))