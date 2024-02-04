def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except Exception:
        return "Invalid input. Expected: add [username] [phone]"

def change_contact(args, contacts):
    try:
        name, phone = args
        try:
            contacts.pop(name)
            contacts[name] = phone
            return "Contact updated."
        except KeyError:
            return f"Contact '{name}' does not exist in contact list."
    except Exception:
        return "Invalid input. Expected: change [username] [phone]"
    
def show_phone(args, contacts):
    try:
        name = args[0]
        try:
            return f"{name}: {contacts[name]}"
        except KeyError:
            return f"Contact '{name}' does not exist in contact list."
    except Exception:
        return "Invalid input. Expected: phone [username]"
    
def show_all(contacts):
    contatct_list = [f"{key}: {contacts.get(key)}" for key in contacts.keys()] if len(contacts.keys()) > 0 else ["contact list is empty"]
    return contatct_list


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            for el in show_all(contacts):
                print(el, end="\n")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

