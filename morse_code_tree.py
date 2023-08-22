from morse_code_alphabet import morse_code_alphabet


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class MorseCodeTree:
    def __init__(self) -> None:
        self.root = Node('')
        self.morse_code_alphabet = morse_code_alphabet
        self._build_tree()

    def _build_tree(self):
        for letter in self.morse_code_alphabet.keys():
            code = self.morse_code_alphabet.get(letter)
            if code != '/':
                self._add_letter(letter, code)

    def _add_letter(self, letter, code):
        temp = self.root
        for step in code:
            if step == '-':
                if temp.right is None:
                    temp.right = Node(step)
                temp = temp.right
            elif step == '.':
                if temp.left is None:
                    temp.left = Node(step)
                temp = temp.left
        temp.value = letter

    def convert_to_text(self, morse_code):
        temp = self.root
        text = ''
        for code_bit in morse_code:
            if code_bit == '.':
                temp = self._step_validation(temp.left, morse_code)
            elif code_bit == '-':
                temp = self._step_validation(temp.right, morse_code)
            elif code_bit == ' ':
                text += temp.value
                temp = self.root
            elif code_bit == '/':
                text += ' '
                temp = self.root
            else:
                raise ValueError(f'Morse code decoder error: '
                                 f'unable to decode {morse_code} due to invalid character: {code_bit} ')
        text += temp.value
        return text

    @staticmethod
    def _step_validation(next_node: Node, morse_code):
        if next_node:
            return next_node
        raise ValueError(f'Morse code decoder error: {morse_code} is an invalid morse code')