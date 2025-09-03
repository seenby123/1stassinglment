from product_data import products

print("Sample products:")
for product in products[:3]:
    print(product)

customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input().strip().lower()
    if preference:
        customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()

customer_preferences = set(customer_preferences)

converted_products = []
for product in products:
    converted_products.append({
        "name": product["name"],
        "tags": set(product["tags"])
    })

def count_matches(product_tags, customer_tags):
    return len(product_tags & customer_tags) 


def recommend_products(products, customer_tags):
    recommendations = []
    for product in products:
        matches = count_matches(product["tags"], customer_tags)
        if matches > 0:
            recommendations.append((product["name"], matches))
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations

recommendations = recommend_products(converted_products, customer_preferences)

print("\nRecommended Products:")
for name, match_count in recommendations:
    print(f"- {name} ({match_count} match(es))")

# 1. What core operations did you use (e.g., intersections, loops)? Why?
#    - I used set intersections to quickly compare tags because sets make membership checks efficient.
#    - I used loops to go through all products and count the number of matches.
#    - Sorting was used to rank products so the ones that match best appear first.
#
# 2. How might this code change if you had 1000+ products?
#    - The same logic works, but efficiency matters more at scale.
#    - Set operations remain fast (O(1) average per check).
#    - Sorting is O(n log n), which is still efficient for thousands of products.
#    - For very large catalogs (millions of products), a database or search index would be better.

