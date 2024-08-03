def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lower_text = convert_to_lower(text)
    dict_counted_characters = count_characters(lower_text)
    print(dict_counted_characters)

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


main()
