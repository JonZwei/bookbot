def get_num_words(file):
	count_file = file.split()
	return len(count_file)

def letter_count(book):
    book = book.lower()
    letters = list(book)
    letter_dict = {}
    for let in letters:
        if let not in letter_dict and let.isalpha():
            letter_dict[let] = 1
        elif let in letter_dict:
            letter_dict[let] +=1
    new_list = []
    for key in letter_dict:
        new_list.append({"name": key, "num": letter_dict[key]})
    return new_list

def dict_sort(dict):
    def sort_on(items):
        return items["num"]

    dict.sort(reverse=True, key=sort_on)
    return dict


