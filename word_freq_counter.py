def word_frequency(text):
    words = text.split()   # split text into words
    freq = {}              # dictionary to store frequency

    # count word frequency
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    # find most frequent word
    most_frequent = None
    max_count = 0
    for word in freq:
        if freq[word] > max_count:
            max_count = freq[word]
            most_frequent = word

    # final result dictionary
    result = {
        "Word Frequencies": freq,
        "Most Frequent Word": most_frequent
    }
    return result
# Example input
text = "apple banana apple orange banana apple banana banana"
output = word_frequency(text)
print(output)
