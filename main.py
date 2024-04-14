def read_book(file_path):
    with open(file_path) as f:
        file_data = f.read()

    print(file_data)

    return 0

def main():
    read_book("books/frankenstein.txt")

    return 0

main()