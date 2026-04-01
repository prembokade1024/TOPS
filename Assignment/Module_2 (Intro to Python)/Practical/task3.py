# 3. Write a Python program to count the occurrences of each word in a given sentence.
def count_word_frequencies(sentence):
    # 1. Standardize: Convert to lowercase to ensure "Word" and "word" are counted together
    # 2. Split: Default split() handles multiple spaces and newline characters
    words = sentence.lower().split()
    
    word_counts = {}
    
    for word in words:
        # Remove common punctuation attached to words (optional but recommended)
        clean_word = word.strip(".,!?;:")
        
        if clean_word:
            # Update the count in the dictionary
            word_counts[clean_word] = word_counts.get(clean_word, 0) + 1
            
    return word_counts

sentence = input("Enter a sentence : ")
frequencies = count_word_frequencies(sentence)

print("Word Frequencies:")
for word, count in frequencies.items():
    print(f"'{word}': {count}")