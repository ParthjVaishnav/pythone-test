# Input
nouns = ["car", "plane"]

# ------------------------------
# Step 1: Add correct article (A/An)
# ------------------------------
articles = []
for word in nouns:
    if word[0].lower() in "aeiou":   # starts with vowel
        articles.append("An " + word)
    else:
        articles.append("A " + word)

# ------------------------------
# Step 2: Join words properly
# ------------------------------
if len(articles) == 2:
    sentence = articles[0] + " and " + articles[1]
else:
    sentence = ", ".join(articles[:-1]) + " and " + articles[-1]

# ------------------------------
# Step 3: Capitalize first letter + add period
# ------------------------------
sentence = sentence[0].upper() + sentence[1:] + "."

# ------------------------------
# Final Output
# ------------------------------
print(sentence)

