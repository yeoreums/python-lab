def count_words(text):
    counts = {}
    words = text.split()

    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
    return counts


def main():
    text = "apple banana apple orange banana apple"
    counts = count_words(text)

    for word, count in counts.items():
        print(word, count)


if __name__ == "__main__":
    main()