# extract a specific line from message
with open('readme.txt', 'r', encoding="utf-8") as f:
    for line in f:
        if line.startswith('https://teaserfast.ru/registration/?verification='):
            print(line)

# extract a string before a character
s1 = "sbjdb@gmail.com"
s2 = s1.split('@')[0]
print(s2)