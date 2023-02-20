from classes import *
from utils import load_word


def main():
    stopwords = ["stop", 'стоп']
    player = Player(input("Ввведите имя игрока: "), used_words=[])

    print(f"Привет, {player.username}")

    MyWord = load_word()
    print(f"Составьте {MyWord.subwords_Count()} слов из слова {MyWord.word}")
    print("Слова должны быть не короче 3 букв")
    print("Чтобы закончить игру, угадайте все слова или напишите 'stop'")
    print("Поехали, ваше первое слово?")

    while player.get_used_words() < MyWord.subwords_Count():
        answer = input()
        if len(answer) < 3:
            print("слишком короткое слово")
        elif answer in stopwords:
            break
        elif answer not in MyWord.subwords:
            print("неверно")
        else:
            player.add_word(answer)



    print(f"Игра завершена, вы угадали {len(player.used_words)} слов!")

main()