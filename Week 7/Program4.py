def frequency_analysis(message):
    letter_counts = {}
    for char in message.lower():
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts[:6]


result = frequency_analysis("Hello, this is a sample message.")
print(result)
