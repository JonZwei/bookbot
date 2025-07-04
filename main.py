from stats import get_num_words, letter_count, dict_sort
import sys

def get_book_text():
	with open(sys.argv[1]) as f:
		file_contents = f.read()
		return file_contents

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	num_words = get_num_words(get_book_text())
	letter_list = letter_count(get_book_text())
	letters_sorted = dict_sort(letter_list)
	print('============ BOOKBOT ==========')
	print(f'Analyzing book found at {sys.argv[1]}...')
	print('----------- Word Count ----------')
	print(f"Found {num_words} total words")
	print('--------- Character Count -------')
	for dic in letter_list:
		letter = dic["name"]
		numb = dic["num"]
		print(f'{letter}: {numb}')
	



main()
