# CodSoft Internship Project
# Simple Recommendation System (Movies, Books, Products)

items = {
    "3 Idiots": ["movie", "comedy", "friendship", "college"],
    "Dangal": ["movie", "sports", "drama"],
    "Kabir Singh": ["movie", "romance", "drama"],
    "Baahubali": ["movie", "action", "fantasy"],
    "PK": ["movie", "comedy", "sci-fi"],

    "The Alchemist": ["book", "fiction", "inspirational"],
    "Harry Potter": ["book", "fantasy", "magic"],
    "Atomic Habits": ["book", "self-help", "motivation"],
    "Wings of Fire": ["book", "biography", "inspirational"],

    "iPhone 14": ["product", "electronics", "smartphone"],
    "Samsung Galaxy": ["product", "electronics", "android"],
    "Nike Shoes": ["product", "fashion", "sports"],
    "Adidas Jacket": ["product", "fashion", "clothing"]
}

def recommend(item):
    item = item.lower()
    found = None
    for key in items:
        if key.lower() == item:
            found = key
            break
    if not found:
        return ["Sorry, item not in database"]

    base_tags = set(items[found])
    scores = {}
    for other, tags in items.items():
        if other != found:
            score = len(base_tags & set(tags))
            if score > 0:
                scores[other] = score

    sorted_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_items[:5]]


print("Welcome to Simple Recommendation System")
choice = input("Enter a movie, book or product you like: ")

results = recommend(choice)

print("\nRecommended for you:")
for i, r in enumerate(results, 1):
    print(f"{i}. {r}")
