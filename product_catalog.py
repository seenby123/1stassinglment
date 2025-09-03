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



"""
Design Memo
-----------

For this assignment, I built a small recommendation program that matches what a customer likes
with a list of products. Each product has tags like "eco-friendly" or "durable" that describe it.
The customer inputs what they like, and the program scans for products that share the same tags.

I found sets to actually be very convenient here because they make it easy to know if two sets contain common items. For each product,
I also put the tags into a set. I then used the intersection operation (&) to know how
many tags the product and the customer had in common. That gave me a number of matches.

The program loops through each product and counts the number of matches.
Then I ordered the results so that products with the most matches are listed first.
This makes reading the output easier and more helpful to the customer.

If there were over 1,000 products, the program would continue to work. It would possibly take a
bit longer to run, but Python set operations and loops can handle that quantity. For really large
catalogs, like millions of products, I would probably need to use a database or other faster
searching methods, but for this project the direct approach is good enough.
"""


