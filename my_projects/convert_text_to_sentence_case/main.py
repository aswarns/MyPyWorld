with open("example.txt", 'r') as file:
    content = file.read()

content = content.split()

new_word  = []

for word in content:
    new_word.append(word[::-1])

reversed_text = " ".join(new_word)

with open('example.txt', 'w') as file:
    file.write(reversed_text)


