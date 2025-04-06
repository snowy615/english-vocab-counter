import csv
from collections import defaultdict
#test
def clean_word(word):
    """Remove invisible characters and normalize word"""
    return word.strip().replace('\ufeff', '').lower()

# Step 1: Load existing vocab
vocab = defaultdict(int)
with open('vocab.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip header
    for row in reader:
        if row and len(row) >= 2:  # Check if row has at least word and frequency
            word = clean_word(row[0])
            try:
                vocab[word] = int(row[1])
            except ValueError:
                vocab[word] = 0  # Default to 0 if frequency is invalid

# Step 2: Process input words
new_words_added = 0
with open('input.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:  # Skip empty lines
            word = clean_word(row[0])
            if word not in vocab:
                new_words_added += 1
            vocab[word] += 1  # Adds new words with freq=1, increments existing

# Step 3: Save updated vocab
with open('vocab.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['word', 'frequency'])
    for word, freq in sorted(vocab.items()):
        writer.writerow([word, freq])

print(f"Success! Updated {len(vocab)} words. New words added: {new_words_added}")