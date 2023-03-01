file = open("file.txt", "r")
string = file.read()
words = string.split()
count = 0
repeatedWords = {}
while len(words) > count: 
    #read by character
    char = words[count]
    if not char: #if char is false finish the while | Si no es un char termina el ciclo
        break
    if char.isalpha():
        char = char.lower()
        if char in repeatedWords:
            repeatedWords[char] += 1
        else:
            repeatedWords[char] = 1
        print(char, end=", ")
        count += 1
    else: count += 1
for word, repeat in repeatedWords.items():
    if repeat > 1:
        print(word+':', repeat)
file.close()
