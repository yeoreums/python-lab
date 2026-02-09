def error_count_by_user(logs):
    result = {}

    for log in logs:
        r = log.split(" ")
        # print(r)
        if r[1] == "error":
            result[r[0]] = result.get(r[0], 0) + 1
    return result

logs = [
    "10 success",
    "10 error",
    "11 success",
    "10 error",
    "12 success",
    "11 error"
]

print(error_count_by_user(logs))
