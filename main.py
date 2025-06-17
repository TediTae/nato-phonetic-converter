import pandas

nato_phonetic_df = pandas.read_csv("nato_phonetic_alphabet.csv")

np_dict = {row.letter: row.code for (index, row) in nato_phonetic_df.iterrows()}
# print(np_dict)

entered_word = input("enter a word: ").upper()
output_list = [np_dict[letter] for letter in entered_word]
print(output_list)
