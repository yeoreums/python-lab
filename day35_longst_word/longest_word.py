def find_longest_word(text):
    words = text.split()

    longest_word = None
    max_length = 0
    
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    
    return longest_word
    
    # Pythonic version
    # words = text.split()
    # return max(words, key=len)


def main():
    text = "apple banana strawberry kiwi"
    longest_word = find_longest_word(text)

    print(longest_word)


if __name__ == "__main__":
    main()
