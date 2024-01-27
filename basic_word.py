class BasicWord:
    def __init__(self, word, subwords=[]):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return (f"Исходное слово: {self.word}\n"
                f"Подслова: {", ".join(self.subwords)}")

    def check_answer(self, user_answer):
        if user_answer in self.subwords:
            return True
        return False

    def count_subwords(self):
        return int(len(self.subwords))
