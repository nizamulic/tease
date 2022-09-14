from mailtm import Email

def listener(message):
    print("\nSubject: " + message['subject'])
    with open('readme.txt', 'w', encoding="utf-8") as f:
        f.write(message['text'] if message['text'] else message['html'])
    # extract a specific line from message
    with open('readme.txt', 'r', encoding="utf-8") as f:
        for line in f:
            if line.startswith('https://teaserfast.ru/registration/?verification='):
                print(line)
    print("Content: " + message['text'] if message['text'] else message['html'])

# Get Domains
test = Email()
print("\nDomain: " + test.domain)

# Make new email address
test.register()
print("\nEmail Adress: " + str(test.address))

# Start listening
test.start(listener)
print("\nWaiting for new emails...")