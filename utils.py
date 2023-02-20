import requests
import random
from classes import BasicWord

def load_word():
    data = requests.get("https://api.npoint.io/44c4b1c1f51afc96928a").json()
    word = random.choice(data)
    My_Word = BasicWord(word["word"], word["subwords"])
    return My_Word




