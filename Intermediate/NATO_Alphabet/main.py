import pandas

words_dict = {}
user_list = []

file = pandas.read_csv("nato_phonetic_alphabet.csv")

for (index, row) in file.iterrows():
    words_dict[row.letter] = row.code

print(words_dict)

get_user_input = True

while get_user_input:
    user_input = input("Enter a word: ").upper()
    for letter in user_input:
        try:
            user_list.append(words_dict[letter])
        except KeyError:
            print("Sorry, only letters are acceptable!")
            user_list = []
            break
    if len(user_list) == len(user_input):
        get_user_input = False

print(user_list)
