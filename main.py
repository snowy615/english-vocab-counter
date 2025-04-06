import csv
import os

VOCAB_FILE = 'vocab.csv'
INPUT_FILE = 'input.csv'

def clean_word(word):
    return word.strip().lower()

def load_vocab(filename):
    vocab = {}
    if not os.path.exists(filename):
        return vocab

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            word = clean_word(row.get('word', ''))
            freq_raw = row.get('frequency', '0').strip()
            try:
                freq = int(freq_raw)
            except ValueError:
                freq = 0
            if word:
                vocab[word] = freq
    return vocab

def load_input_words(filename):
    words = []
    if not os.path.exists(filename):
        return words

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            word = clean_word(row.get('word', ''))
            if word:
                words.append(word)
    return words

def update_vocab(vocab, words):
    for word in words:
        vocab[word] = vocab.get(word, 0) + 1
    return vocab

def save_vocab(vocab, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['word', 'frequency'])
        writer.writeheader()
        for word in sorted(vocab.keys()):
            writer.writerow({'word': word, 'frequency': vocab[word]})

def main():
    vocab = load_vocab(VOCAB_FILE)
    new_words = load_input_words(INPUT_FILE)

    if not new_words:
        print("No input words found in input.csv.")
        return

    vocab = update_vocab(vocab, new_words)
    save_vocab(vocab, VOCAB_FILE)
    print(f"Updated {len(new_words)} words. Saved to '{VOCAB_FILE}'.")

if __name__ == '__main__':
    main()
