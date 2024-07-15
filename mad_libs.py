with open("text.txt", "r") as f:
    text = f.read()

words = set()
start_position = 0

start_symbol = "<"
end_symbol  = ">"

for i, char in enumerate(text):
    if char == start_symbol:
        start_position = i

    if char == end_symbol and start_position != -1:
        word = text[start_position: i + 1]
        words.add(word)
        start_position = -1


user_answers = {}


for word in words:
    answer = input("Type a word for " + word + ": ")
    user_answers[word] = answer

for word in words:
    text = text.replace(word, user_answers[word])

print(text)