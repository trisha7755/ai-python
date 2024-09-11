# Python Program to Strike Out Predefined Words in Text
def strike_out_words(text, words_to_strike):
    # Function to add strikethrough effect to a word
    def add_strikethrough(word):
        # Combine each character with the strikethrough Unicode character '\u0336'
        return ''.join([char + '\u0336' for char in word])

    # Split the input text into words
    words = text.split()

    # Iterate over the words and replace with strikethrough if in words_to_strike list
    struck_text = ' '.join([add_strikethrough(word) if word.lower() in words_to_strike else word for word in words])

    return struck_text

# Predefined list of words to be struck out
words_to_strike = {"bad", "ugly", "strike", "remove"}

# Main function to get input from the user and strike out predefined words
def main():
    print("Enter your text below. This program will strike out some predefined words.")
    user_input = input("Your text: ")

    # Process the text to strike out specific words
    result = strike_out_words(user_input, words_to_strike)

    print("\nProcessed Text:")
    print(result)

# Run the main function
if __name__ == "__main__":
    main()
