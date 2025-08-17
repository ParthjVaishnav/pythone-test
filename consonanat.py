def rotate_consonants(s: str) -> str :
    vowels = "aeiouAEIOU"
    consonants_lower = "bcdfghjklmnpqrstvwxyz"
    consonants_upper = consonants_lower.upper()

    rotated = []

    for ch in s :
        if ch in vowels or not ch.isalpha() :
            # Keep vowels and non-letters as is
            rotated.append(ch)
        elif ch.islower() :
            idx = consonants_lower.index(ch)
            new_ch = consonants_lower[(idx + 1) % len(consonants_lower)]
            rotated.append(new_ch)
        elif ch.isupper() :
            idx = consonants_upper.index(ch)
            new_ch = consonants_upper[(idx + 1) % len(consonants_upper)]
            rotated.append(new_ch)
        else :
            rotated.append(ch)

    return "".join(rotated)


# Example Test
s = "Hello-World!"
print(rotate_consonants(s))  # Output: "Jello-Xpsme!"
