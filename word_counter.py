def count_words(text):
    words = text.lower().split()

    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result


text = input("Mətn daxil edin: ")

words = count_words(text)

print(words)

most_common = max(words, key=words.get)

print("Ən çox təkrarlanan söz:", most_common)