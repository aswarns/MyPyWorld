with open('example.txt', 'r') as file:
    content = file.read()

file_content = content.split(". ")
#print(file_content)
file_output = []

for word in file_content:
    word = word.capitalize()
    file_output.append(word)

#print(file_output)
file_output = ". ".join(file_output)
#print(file_output)

with open('new_example.txt', 'w') as file:
    file.write(file_output)
