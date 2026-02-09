def top_users(events):
    totals = {}

    for user, value in events:
        totals[user] = totals.get(user, 0) + value
        
    return max(totals, key=totals.get)

events = [
("user1", 10),
("user2", 5),
("user1", 7),
("user3", 20)
]

print(top_users(events))