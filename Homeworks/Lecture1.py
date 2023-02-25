file = open("file.txt", "r")
string = file.read()
words = string.split()
count = 0

while len(words) > count: 
    #read by character
    char = words[count]
    if not char: #if char is false finish the while | Si no es un char termina el ciclo
        break
    if char.isalpha():
        print(char, end=", ")
        count = count + 1
    else: count = count + 1
file.close()
