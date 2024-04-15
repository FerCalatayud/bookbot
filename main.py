def read_book(file_path):
    with open(file_path) as f:
        file_data = f.read()

    return file_data

def count_words(file_data):
    words = file_data.split()
    word_count = len(words)

    return word_count

def count_characters(file_data):

    char_count = {}

    file_data = file_data.lower()

    for char in file_data:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def sort_dict(dict_to_sort):
    
    as_list = []

    for key in dict_to_sort:
        if key.isalpha():
            as_list.append({"letter": key, "count": dict_to_sort[key]})

    as_list.sort(reverse=True, key=lambda x: x["count"])

    return as_list

def create_report(word_count, char_count):

    print("--- Begin report of books/frankenstein.txt ---\n")

    print(f"{word_count} words found in the document\n")

    ordered_dict_as_list = sort_dict(char_count)

    for item in ordered_dict_as_list:
        print(f"The '{item["letter"]}' character was found {item["count"]} times")

    return 0

def main():
    file_data = read_book("books/frankenstein.txt")

    word_count = count_words(file_data)
    char_count = count_characters(file_data)

    create_report(word_count, char_count)

    return 0

main()
