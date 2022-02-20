def make_word_file():
    file = open("words_alpha.txt", "r")
    data = file.readlines()
    file.close()
    Vletters = []
    for i in range(len(data)):
        if (len(data[i]) > 5):
            Vletters.append(data[i])
    nfile = open("5+letter_words.txt", "w")
    nfile.writelines(Vletters)
    nfile.close()


def open_words():
    import json
    file = open("5+letter_words.txt", "r")
    data = file.read()
    file.close()
    v_letter_words = data.split('\n')
    words_json = json.dumps(v_letter_words)
    file = open("5+letter_words.json", "w")
    file.writelines(words_json)
    file.close()


open_words()
