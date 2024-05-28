import pandas

words_dict = {}
user_list = []

file = pandas.read_csv("nato_phonetic_alphabet.csv")

for (index, row) in file.iterrows():
    words_dict[row.letter] = row.code

print(words_dict)

user_input = input("Enter a word: ").upper()

for letter in user_input:
    user_list.append(words_dict[letter])

print(user_list)
