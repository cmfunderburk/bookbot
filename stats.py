def get_num_words(bookstring):
    book_words = bookstring.split()
    num_words = 0
    for word in book_words:
        num_words += 1
    return num_words

def get_num_chars(bookstring):
    book_words = bookstring.split()
    char_counts_dict = {}
    for word in book_words:
        for char in word:
            if char.lower() in char_counts_dict:
                char_counts_dict[f"{char.lower()}"] += 1
            else:
                char_counts_dict[f"{char.lower()}"] = 1
    return char_counts_dict

def sort_on(count_dict):
    return count_dict["num"]

def sort_num_chars(count_dict):
    dict_list = []
    for count in count_dict:
        current_dict = {}
        current_char = count
        current_count = count_dict[count]
        current_dict = {
            "char": current_char,
            "num": current_count
        }
        dict_list.append(current_dict)
    sorted = dict_list.sort(reverse=True, key=sort_on)
    return dict_list