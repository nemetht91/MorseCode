from morse_code import MorseCode

converter = MorseCode()
keep_going = True

print('Welcome to Morse Code converter!')
while keep_going:
    command = input('Do you want to code, decode, stop?\n').lower()
    if command == 'code':
        text = input('Type a text and I will convert it to morse code: \n')
        try:
            code = converter.to_morse_code(text)
            print(f'Morse code: {code}')
        except (TypeError, ValueError) as e:
            print("The following error occurred: ")
            print(e)
    elif command == 'decode':
        code = input('Type a morse code and I will decode it. Valid characters: .-/ \n')
        try:
            converted_text = converter.to_text(code)
            print(f'Decoded text: {converted_text}')
        except (TypeError, ValueError) as e:
            print("The following error occurred: ")
            print(e)
    elif command == 'stop':
        keep_going = False
        print('See you later!')
    else:
        print(f'Invalid choose: {command}. Please try again')



