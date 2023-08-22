from morse_code_alphabet import morse_code_alphabet
from morse_code_tree import MorseCodeTree


class MorseCode:
    def __init__(self):
        self.morse_code_alphabet = morse_code_alphabet
        self.morse_code_tree = MorseCodeTree()

    def to_morse_code(self, text: str):
        self._validate_text(text)
        upper_case_text = text.upper()
        return self._convert_to_code(upper_case_text)

    def to_text(self, morse_code: str):
        return self.morse_code_tree.convert_to_text(morse_code)


    @staticmethod
    def _validate_text(text):
        if type(text) != str:
            raise TypeError(f'Type: {type(text)} is invalid. Can only convert string.')
        if not text:
            raise ValueError("Empty string error. Can't convert empty string.")

    def _convert_to_code(self, text: str):
        code = ''
        for i, letter in enumerate(text):
            code += self._letter_to_code(letter)
            code += self._add_separator(i, text)
        return code

    def _letter_to_code(self, letter):
        self._validate_letter(letter)
        return self.morse_code_alphabet.get(letter)

    def _validate_letter(self, letter):
        if letter not in self.morse_code_alphabet.keys():
            raise ValueError(f"Unknown character. {letter} is not in the morse code alphabet.")

    def _add_separator(self, index, text):
        if self._is_last(index, text):
            return ''
        return ' '

    @staticmethod
    def _is_last(index, text):
        if index < len(text)-1:
            return False
        return True
