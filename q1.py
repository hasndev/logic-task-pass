text = input('Enter Text:')

character = input('Enter One character that want deleted it:')
if len(character) == 1:
    res_str = text.replace(character, '')

print("Text after removal '"+ character+ "' character : " + res_str)
