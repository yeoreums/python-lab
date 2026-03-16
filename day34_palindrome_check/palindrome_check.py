def is_palindrome(word):
    return word == word[::-1]

def main():
    word = "racecar,apple,level,python"
    word_list = word.split(",")
    
    for word in word_list:
        if is_palindrome(word):
            print(f"{word} is a palindrome.")
        else:
            print(f"{word} is not a palindrome.")


if __name__ == "__main__":
    main()
