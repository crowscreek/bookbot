
from stats import count_words
from stats import count_characters
from stats import sorted_list
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)    
    char_counts = count_characters(book_text)
    dict_list = sorted_list(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    for char_dict in dict_list:
        char = char_dict["char"]
        count = char_dict["num"]

        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")
main()
