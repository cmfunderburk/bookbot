from stats import get_num_words
from stats import get_num_chars
from stats import sort_num_chars
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    else:

        path = sys.argv[1]
        contents = get_book_text(path)
        num_words = get_num_words(contents)
        char_counts = get_num_chars(contents)
        sorted_chars = sort_num_chars(char_counts)


        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        for entry in sorted_chars:
            character = entry["char"]
            count = entry["num"]
            print(f"{character}: {count}")
            


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()

