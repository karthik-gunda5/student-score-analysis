import matplotlib.pyplot as plt

# Mock data (used due to API unavailability)
students = [
    {"name": "Karthik", "score": 78},
    {"name": "Anjali", "score": 85},
    {"name": "Rahul", "score": 72},
    {"name": "Sneha", "score": 90},
    {"name": "Amit", "score": 80}
]

names = []
scores = []

for s in students:
    names.append(s["name"])
    scores.append(s["score"])

average = sum(scores) / len(scores)

print("Average Score:", average)

# Bar chart
plt.bar(names, scores)
plt.axhline(average)
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Test Scores")

plt.show()
