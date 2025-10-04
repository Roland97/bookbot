from stats import get_num_words
from stats import character_count
from stats import dict_to_list

def get_book_text(books):
    with open(books) as f:
        text = f.read()
        return text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    full_count = character_count(book_text)
    sorted_chars = dict_to_list(full_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("------------ Word Count ------------")
    print(f"Found {num_words} total words")
    print("------------ Character Count ------------")
    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()