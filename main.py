def read_book(file_path):
    with open(file_path) as f:
        file_data = f.read()

    return file_data

def main():
    file_data = read_book("books/frankenstein.txt")

    words = file_data.split()
    word_count = len(words)

    print(word_count)

    return word_count

main()
