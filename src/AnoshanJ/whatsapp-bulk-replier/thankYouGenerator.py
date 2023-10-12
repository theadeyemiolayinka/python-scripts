import re
# import pyautogui
import time

def generate_thank_you_message(messages, your_name):
    tagged_users = []
    
    # Extract birthday wishes and tagged users from the messages
    for message in messages:
        match = re.search(r"\[(.*?)\].*?:(.*?) @Me", message)
        if match:
            user = message.split(":")[1].split("] ")[1]
            tagged_users.append(user)

    # Generate the thank you message
    thank_you_message = "Thank you guys😁🙌\n"
    for user in tagged_users:
        thank_you_message += f"@{user}\n"    
    
    return thank_you_message

mode = input("Enter mode (1 for file, 2 for terminal): ")

if mode == "1":
    file_name = input("Enter file name: ")
    with open(file_name, "r", encoding="utf-8") as f:
        whatsapp_messages = f.read().splitlines()
elif mode == "2":
    print("Enter the messages below. Press enter on an empty line to finish.")
    whatsapp_messages = []
    while True:
        message = input()
        if not message:
            break
        whatsapp_messages.append(message)
else:
    print("Invalid mode selected.")
    exit()

# your_name = input("Enter your name: ")
your_name = "Me"

thank_you_msg = generate_thank_you_message(whatsapp_messages, your_name)

print(thank_you_msg)

# save it to file
with open("thank_you_message.txt", "w", encoding="utf-8") as f:
    f.write(thank_you_msg)