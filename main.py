def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lower_text = convert_to_lower(text)
    dict_counted_characters = count_characters(lower_text)
    chars_sorted_list = sort_on(dict_counted_characters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['value']} times")

    print(f"--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def convert_to_lower(text):
    lowered_text = text.lower()
    return lowered_text

def count_characters(lower_text):
    char_dict = {}
    for char in lower_text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] +=1
    return char_dict

def get_value(item):
    return item['value']

def sort_on(dict):
    list_of_dicts = []
    for char in dict:
        list_of_dicts.append({"char": char, "value": dict[char]})
    list_of_dicts.sort(key=get_value, reverse=True)
    return list_of_dicts


main()
