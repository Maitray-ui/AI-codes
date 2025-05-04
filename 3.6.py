jobs = [(100, 2), (19, 1), (27, 2), (25, 1), (15, 3)]  # (profit, deadline)
jobs.sort(reverse=True)

slots = [False] * len(jobs)
profit = 0

for p, d in jobs:
    for j in range(min(d, len(jobs))-1, -1, -1):
        if not slots[j]:
            slots[j] = True
            profit += p
            break

print("Max Profit:", profit)
