text = input('Enter Text:')
character = input('Enter One character that want checked it:')
count = 0

if len(character) == 1:
    for i in text:
        if i == character:
            count = count + 1
    
print(count)