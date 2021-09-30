with open("Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_content = letter_file.read()

with open("Input/Names/invited_names.txt", mode="r") as names_file:
    invited_names = names_file.readlines()

#for each name in invited_names.txt
for name in invited_names:
    # Replace the [name] placeholder with the actual name.
    personal_letter = letter_content.replace("[name]", f"{name.strip()}")
    # Save the letters in the folder "ReadyToSend".
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(personal_letter)
