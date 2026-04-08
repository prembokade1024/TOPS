# 3. Write a Python program to count the occurrences of each word in a given sentence.
def count_word_frequencies(sentence):
    words = sentence.lower().split()
    
    word_counts = {}
    
    for word in words:
        clean_word = word.strip(".,!?;:")
        
        if clean_word:
            word_counts[clean_word] = word_counts.get(clean_word, 0) + 1
            
    return word_counts

sentence = input("Enter a sentence : ")
frequencies = count_word_frequencies(sentence)

print("Word Frequencies:")
for word, count in frequencies.items():
    print(f"'{word}': {count}")