class BasicWord():
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return "Класс для базовых слов, из которых пользователь будет находить новые"

    def check_word(self, word):
        if word in self.subwords:
            return True
        else:
            return False

    def subwords_Count(self):
        return len(self.subwords)


class Player():
    def __init__(self, username, used_words):
        self.username = username
        self.used_words = used_words

    def __repr__(self):
        return "Класс игрока для хранения данных о его действиях в игре"

    def get_used_words(self):
        return len(self.used_words)

    def check_word(self, word):
        if word in self.used_words:
            return True
        else:
            return False

    def add_word(self, words):
        if not Player.check_word(self, words):
            print("верно")
            self.used_words.append(words)
        else:
            print("уже использовано")
