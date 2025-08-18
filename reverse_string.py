s = "a,b$c"

# Step 1: collect alphabets
alphabets = []
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)

# Step 2: reverse in place
alphabets.reverse()

# Step 3: rebuild string
result = []
idx = 0
for ch in s:
    if ch.isalpha():
        result.append(alphabets[idx])
        idx += 1
    else:
        result.append(ch)

# Step 4: join list into string
output = "".join(result)

print("Input :", s)
print("Output:", output)
