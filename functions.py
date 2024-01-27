def load_random_word():
    import requests, random
    from basic_word import BasicWord
    raw_list = requests.get("https://api.npoint.io/a737ef2296b86f8e6aa5")
    subwords = raw_list.json()

    chosen = random.choice(subwords)
    word = BasicWord(chosen["word"], chosen["subwords"])
    return word
