def count_words(book):
    words = book.split()
    return len(words)

def letter_count(book):
    book = book.lower()
    letters = list(book)
    letter_dict = {}
    for let in letters:
        if let not in letter_dict and let.isalpha():
            letter_dict[let] = 1
        elif let in letter_dict:
            letter_dict[let] += 1
   
    return letter_dict


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    print('--- Begin report of books/frankenstein.txt ---')
    print('%d words found in the document\n' %
          (count_words(file_contents)))
    letter_dict = letter_count(file_contents)
    for key in letter_dict:
        print("The '%s' charactor was found %d times" %
              (key, letter_dict[key]))
    
    




main()
