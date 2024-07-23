# Open the text file "text.txt" in read mode and read its contents
# The text file was previously made specifically for the mad libs game
with open("text.txt", "r") as f:
    text = f.read()

# Initialize an empty set to store words
words = set()
# Initialize the starting position for word extraction
start_position = 0

# Define the symbols that indicate the start and end of a word
start_symbol = "<"
end_symbol  = ">"

# Iterate over each character in the text along with its index
for i, char in enumerate(text):
    # Check if the character is the start symbol
    if char == start_symbol:
        start_position = i

    # Check if the character is the end symbol and a start position has been set
    if char == end_symbol and start_position != -1:
        # Extract the word from start to end symbol and add it to the set
        word = text[start_position: i + 1]
        words.add(word)
        # Reset the start position
        start_position = -1

# Initialize an empty dictionary to store user answers
user_answers = {}

# Prompt the user to provide a replacement for each word
for word in words:
    answer = input("Type a word for " + word + ": ")
    user_answers[word] = answer

# Replace each word in the text with the user's input
for word in words:
    text = text.replace(word, user_answers[word])

# Print the modified text
print(text)
