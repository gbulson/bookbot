def main():
    book_path = "books/frankenstein.txt"
    file_contents = return_text_from_file(book_path)
    word_count = get_word_count(file_contents)
    charachter_count = character_count(file_contents)
    char_count_dictionary = character_count(file_contents)
    char_report(char_count_dictionary)
    

    


def return_text_from_file(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def get_word_count(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return word_count 

def character_count(text):
    lowered_text = text.lower()
    chars = list(lowered_text)
    chars_set = set(chars)
    char_count_dictionary = {}
    for char in chars_set:
        char_count_dictionary[char] = 0
    for char in chars:
        if char in char_count_dictionary:
            char_count_dictionary[char] += 1

    return char_count_dictionary

def char_report(char_count_dictionary):
    for char in char_count_dictionary:
        char_count = char_count_dictionary[char]
        print(f"The '{char}' character was found {char_count} times")
    

main()