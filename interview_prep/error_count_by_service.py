def error_count_by_service(logs):
    result = {}

    for log in logs:
        timestamp, service, level = log.split()
        # print(parts)
        if level == "ERROR":
            result[service] = result.get(service, 0) + 1

    return result

logs = [
    "2026-02-08 api INFO",
    "2026-02-08 api ERROR",
    "2026-02-08 web INFO",
    "2026-02-08 api ERROR",
    "2026-02-08 db ERROR",
    "2026-02-08 web INFO"
]

print(error_count_by_service(logs))