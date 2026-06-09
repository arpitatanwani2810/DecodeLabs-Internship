import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

items = [
    {
        "title": "Machine Learning Fundamentals",
        "tags": ["ai", "python", "machine learning", "data"]
    },
    {
        "title": "Web Development Bootcamp",
        "tags": ["html", "css", "javascript", "web"]
    },
    {
        "title": "Data Science with Python",
        "tags": ["python", "data", "analytics", "ai"]
    },
    {
        "title": "UI UX Design Masterclass",
        "tags": ["figma", "design", "creativity", "ux"]
    },
    {
        "title": "Deep Learning Essentials",
        "tags": ["ai", "neural networks", "python"]
    },
    {
        "title": "Leadership and Team Building",
        "tags": ["leadership", "management", "communication"]
    },
    {
        "title": "Digital Art Studio",
        "tags": ["art", "creativity", "drawing"]
    },
    {
        "title": "Competitive Programming",
        "tags": ["c++", "algorithms", "problem solving"]
    }
]

print("\nAI RECOMMENDATION SYSTEM")
print("-" * 50)

user_input = input(
    "\nEnter your interests separated by commas:\n"
).lower()

user_preferences = {
    interest.strip()
    for interest in user_input.split(",")
}

recommendations = []

for item in items:
    item_tags = set(item["tags"])

    similarity = len(
        user_preferences.intersection(item_tags)
    ) / len(
        user_preferences.union(item_tags)
    )

    recommendations.append(
        {
            "Title": item["title"],
            "Similarity Score": round(similarity, 3)
        }
    )

df = pd.DataFrame(recommendations)

df = df.sort_values(
    by="Similarity Score",
    ascending=False
)

top_results = df.head(5)

print("\nTOP RECOMMENDATIONS")
print("-" * 50)
print(top_results)

plt.figure(figsize=(10, 5))

plt.bar(
    top_results["Title"],
    top_results["Similarity Score"]
)

plt.xticks(rotation=20)
plt.ylabel("Similarity Score")
plt.title("Top Recommended Items")
plt.tight_layout()

plt.savefig("recommendation_results.png")

print("\nGraph saved as recommendation_results.png")
