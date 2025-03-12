def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    char_list = {}
    lowered_text = text.lower()

    for char in lowered_text:
        if char.isalpha():
            if char in char_list:
                char_list[char] += 1
            else:
                char_list[char] = 1

    return char_list


def sort_chars(char_dict):
    sorted = []

    for char in char_dict:
        sorted.append({"char": char, "num": char_dict[char]})

    sorted.sort(reverse=True, key=sort_key)
    return sorted


def sort_key(dict):
    return dict["num"]
