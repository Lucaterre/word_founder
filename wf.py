#!/usr/bin/env python 
#-*- coding: utf-8 -*-

"""Small tool to help find the start of the offset 
of a word and its length in a very long text quickly

# Author : Lucas Terriel <lucas.terriel@inria.fr>
"""

def get_offset_length_word():
	def rerun():
		answer = input('Do you want continue ? [O/n]\n\n')
		if answer.lower() == 'o':
			run = True
		else:
			run = False
		return run

	def separator():
		return print('-' * 20, '\n')

	print("""
		|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
		|***********************************************|
		|**************** WORD FOUNDER *****************|
		|***********************************************|
		|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

		HELP
		----

		Found the offset and the length of your your word
		in sentence

		\n""")
	run = True

	while run:
		try :
			sentence = input('1) Enter your complete sentence : \n\n')
			separator()
			word_to_find = input('2) Enter the word want to find in sentence : \n\n')
			separator()
			offset_start_sentence = int(input('3) Enter the offset start sentence : \n\n'))
			separator()
			if offset_start_sentence == None:
				offset_start_sentence = 0
			offset_start_word = offset_start_sentence + sentence.index(word_to_find)
			length = len(word_to_find)
			print(f'[RESULT :] offset start word : {offset_start_word} | length of your word : {length} \n') 
			run = rerun()

		except ValueError as E:
			print(f"Your word didn't match in sentence | {E} \n")
			print("Try again ! \n")

			run = rerun()


if __name__ == "__main__":
	get_offset_length_word()