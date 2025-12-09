scores = {"Alice": 85, "Bob": 90}
scores["Charlie"] = 78
scores["Bob"] = 95
print(scores.get("Dave"), scores.get("Bob"))
scores.pop("Alice")
print(scores, len(scores))
print(scores.keys(), scores.values())