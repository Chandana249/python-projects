def is_palindrome(text):
    # Convert to lowercase and remove spaces
    text = text.lower().replace(" ", "")

    # Check if the string is equal to its reverse
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"

# User input
word = input("Enter a word or phrase: ")
print(is_palindrome(word))