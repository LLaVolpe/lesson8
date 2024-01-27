import random
class Question:

    def __init__(self, q, d, a, points=0, is_answered=False, user_answer=None):
        self.q = q
        self.d = int(d)
        self.a = a
        self.points = points
        self.is_answered = is_answered
        self.user_answer = user_answer

    def __repr__(self):
        return (f'Задан ли вопрос: {self.is_answered}\n'
                f'Ответ пользователя: {self.user_answer}\n'
                f'Баллы за вопрос: {self.points}\n')

    def get_points(self):
        self.points = int(self.d * 10)
        return self.points

    def is_correct(self):
        if self.user_answer == self.a:
            self.is_answered = True
        else:
            self.is_answered = False
        return self.is_answered

    def build_question(self):
        print(f"Вопрос: {self.q}\n"
              f"Сложность: {self.d}/5")

    def build_positive_feedback(self):
        print(f"Ответ верный, получено {self.points} баллов")

    def build_negative_feedback(self):
        print(f"Ответ неверный, верный ответ -  {self.a}")


def get_questions():
    import json
    questions = []
    with open("questions.txt", "r") as f:
        content = json.loads(f.read())

    for que in content:
        question = Question(que["q"], que["d"], que["a"])
        questions.append(question)
    return questions

def get_statistics(questions):
    correct_questions = 0
    points = 0
    for q in questions:
        points += q.points
        if q.is_answered is True:
            correct_questions += 1
    print(f"Вот и всё!\n"
          f"Отвечено {correct_questions} вопроса из {len(questions)}\n"
          f"Набрано баллов: {points}")


questions = get_questions()
random.shuffle(questions)

for question in questions:
    question.build_question()
    question.user_answer = input("Введите ответ:")

    if question.is_correct() is True:
        question.get_points()
        question.build_positive_feedback()
    else:
        question.build_negative_feedback()

results = get_statistics(questions)

