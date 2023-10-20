with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
    letter_list = letter.read()
with open("./Input/Names/invited_names.txt", mode="r") as names:
    name_list = names.readlines()
for name in name_list:
    stripped_name = name.strip()
    replaced_text = letter_list.replace("[name]", f"{stripped_name}")
    final_text = replaced_text
    with open(f"./Output/ReadyToSend/{stripped_name}.txt", mode="w") as letter:
        letter.write(final_text)
