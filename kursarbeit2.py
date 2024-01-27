from functions import load_random_word
from players import Player

letters = 3
end_word = ["stop", "стоп"]

name = input("Введите имя игрока:\n")
user = Player(name)
print(f'Привет, {user.name}!\n')

w = load_random_word()
print(f"Составьте {w.count_subwords()} слов из слова {w.word}\n"
      f"Слова должны быть не короче {letters} букв\n"
      f"Чтобы закончить игру, угадайте все слова или напишите ""stop"" \n"
      f"Поехали, ваше первое слово?")

while user.get_words() != w.count_subwords():
    user_answer = input()
    if user_answer in end_word:
        break
        ()
    elif len(user_answer) != letters:
        print(f"Необходимо составить слово из {letters} букв")
    elif w.check_answer(user_answer) is False:
        print("Неверно")
    elif user.check_word(user_answer) is True:
        print("Уже использовано")
    else:
        user.add_word(user_answer)
        print("Верно")

print(f"Игра завершена, вы угадали {user.get_words()} слов!")
