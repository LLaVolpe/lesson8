class Player:
    def __init__(self, name, used_words=[]):
        self.name = name
        self.used_words = used_words  # отгаданные слова

    def __repr__(self):
        print(f'Имя пользователя:{self.name}\n'
              f'Использованные слова: {self.used_words}')

    def get_words(self):
        return len(self.used_words)

    def add_word(self, user_answer):
        self.used_words.append(user_answer)

    def check_word(self, user_answer):
        if user_answer in self.used_words:
            return True
        return False
