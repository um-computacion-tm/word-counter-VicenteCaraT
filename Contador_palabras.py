
def count_words(phrase):
    words = {}
    word_list = phrase.lower().split()

    for index in word_list:
        if index in words:
            words[index] += 1
        else:
            words[index] = 1
    result = words
    return result


if __name__ == '__main__':
    pass