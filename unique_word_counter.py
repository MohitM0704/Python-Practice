text = input("Enter a sentence: ")
words = text.split()
print(f"Total words in sentence: {len(words)}")

unique_words = set()
repeated_words = set()
for word in words:
    if word in unique_words:
        repeated_words.add(word)
    else:
        unique_words.add(word)

print(f"Unique words: {unique_words}")
print(f"Repeated words: {repeated_words}") 