def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
        
    return file_contents

def get_num_of_words(book_str: str) -> int:
    number_of_words = book_str.split()
    return len(number_of_words)

def get_char_counts_dict(book_str):
    character_dict = dict()
    
    for char in book_str:
        char = char.lower()
        character_dict[char] = character_dict.get(char, 0) + 1
        
    return character_dict

def __sort_func(dict):
    return dict['num']

def get_sorted_dics(character_dict):
    dict_list = []
    
    for char in character_dict:
        if char.isalpha(): # we're not interested in non alpha characters
            dict_list.append({'char': char, 'num': character_dict[char]})
            
    dict_list.sort(reverse=True, key=__sort_func)
    return dict_list