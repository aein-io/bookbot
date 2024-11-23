def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_count = get_char_count(book_text)
    sorted_char_count = sort_chars(char_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for item in sorted_char_count:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


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


def sort_key(dict):
    return dict["num"]


def sort_chars(char_dict):
    sorted = []

    for char in char_dict:
        sorted.append({"char": char, "num": char_dict[char]})

    sorted.sort(reverse=True, key=sort_key)
    return sorted


main()
