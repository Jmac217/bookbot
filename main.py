import sys
from stats import get_num_words
from stats import get_letter_frequency
from stats import sort_letter_frequency

def print_usage():
    print("Usage: python3 main.py <path_to_book>")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if (len(sys.argv) > 1):
        book = sys.argv[1]
    else:
        print_usage()
        sys.exit(1)
    book_text = get_book_text(book)
    num_words = get_num_words(book_text)
    letter_frequency = get_letter_frequency(book_text)
    isSorted = True
    sorted_letter_frequency = sort_letter_frequency(letter_frequency, isSorted)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entries in sorted_letter_frequency:
        char = entries["char"]
        num = entries["num"]
        print(f"{char}: {num}")
    print("============= END ===============")
main()