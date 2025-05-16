import sys
from stats import *


def print_character_count(list_of_dicts):
    print("--------- Character Count -------")
    
    for char_dict in list_of_dicts:
        print(f"{char_dict['char']}: {char_dict['num']}")
 
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_name = sys.argv[1]
    
    # remove any spaces, just in case
    book_name = book_name.strip()
    
    book_str = get_book_text(book_name)
    total_words = get_num_of_words(book_str)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_name}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")

    characters_count_dict = get_char_counts_dict(book_str)
    
    dict_list = get_sorted_dics(characters_count_dict)
    
    print_character_count(dict_list)

main()

