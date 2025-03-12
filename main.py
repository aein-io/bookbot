import sys
from stats import get_word_count, get_char_count, sort_chars


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_count = get_char_count(book_text)
    sorted_char_count = sort_chars(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyszing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_char_count:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
