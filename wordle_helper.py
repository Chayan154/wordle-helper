
# creating functions
from re import I


def open_words():
    file = open("5_letter_words.txt", "r")
    data = file.read()
    file.close()
    v_letter_words = data.split('\n')
    return v_letter_words


def includes(a, *b):
    for i in b:
        if i not in a:
            return False
    else:
        return True


def excludes(a, *b):
    for i in b:
        if i in a:
            return False
    else:
        return True


def matched_words1(a, *l):
    words = []
    for i in a:
        if includes(i, *l):
            words.append(i)
        else:
            pass
    return words


def matched_words2(a, *l):
    words = []
    for i in a:
        if excludes(i, *l):
            words.append(i)
        else:
            pass
    return words


def letter_data(b):
    e_letters = []
    i_letters = []
    g_letters = []
    for i in range(len(b)):
        if(b[i] == '0'):
            e_letters.append(b[i-1])
        elif(b[i] == '1' or b[i] == '2'):
            i_letters.append(b[i-1])
        if(b[i] == '2'):
            g_letters.append(b[i-1])
            g_letters.append(int(((i-1)/2)))

    return e_letters, i_letters, g_letters


def isMatched(a, b):
    for j in range(int(len(b)/2)):
        if a[b[2*j+1]] != b[2*j]:
            return False
    else:
        return True


def wordle_helper():
    word_data = open_words()
    final_words = word_data
    print("hi, this is wordle helper")
    print("--------------------------------")
    print("""
    0 = black letters;
    1 = yellow letters;
    2 = green letters
    write the word with its corresponding numbers beside it
    An input example - 'a0d1i0e2u0'
    """)
    while len(final_words) != 1:
        print('\n')
        word = input("Submit your inputs: ")
        a, b, c = letter_data(word)
        m_words1 = matched_words1(final_words, *b)
        m_words2 = matched_words2(m_words1, *a)
        final_words = [w for w in m_words2 if isMatched(w, c)]
        print(final_words)

    else:
        print(f"Todays Word is -> {final_words[0]}")


# Calling main function
# wordle_helper()

wordle_helper()
