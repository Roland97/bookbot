def get_num_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def character_count(book_text):
    lowered_text = book_text.lower()
    sum_character = {}
    for character in lowered_text:
        if character in sum_character:
            sum_character[character] += 1
        else:
            sum_character[character] = 1
    return sum_character

def sort_on(d):
    return d["num"]

def dict_to_list(num_chars_dict):
    sorted_list = []
    for ch, count in num_chars_dict.items():
        sorted_list.append({"char": ch, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list