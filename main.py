import re
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command format"

    return wrapper


class ContactAssistant:
    def __init__(self):
        self.contacts = {}

    @input_error
    def add_contact(self, input_str):
        _, name, phone = input_str.split()
        self.contacts[name] = phone
        return f"Contact {name} added with phone {phone}"

    @input_error
    def change_contact(self, input_str):
        _, name, phone = input_str.split()
        if name in self.contacts:
            self.contacts[name] = phone
            return f"Phone number for {name} changed to {phone}"
        else:
            raise KeyError

    @input_error
    def phone_lookup(self, input_str):
        _, name = input_str.split()
        if name in self.contacts:
            return f"The phone number for {name} is {self.contacts[name]}"
        else:
            raise KeyError

    def show_all_contacts(self):
        if not self.contacts:
            return "No contacts available."
        result = "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])
        return result

    def process_command(self, command):
        command = command.lower()
        if command == "hello":
            return "How can I help you?"
        elif command.startswith("add"):
            return self.add_contact(command)
        elif command.startswith("change"):
            return self.change_contact(command)
        elif command.startswith("phone"):
            return self.phone_lookup(command)
        elif command == "show all":
            return self.show_all_contacts()
        elif command in ["good bye", "close", "exit"]:
            return "Good bye!"
        else:
            return "Invalid command. Please try again."

    def main(self):
        print("Welcome to the Contact Assistant CLI!")
        print("Enter commands or type 'good bye' to exit.")

        while True:
            user_input = input("Enter your command: ")
            result = self.process_command(user_input)

            if result == "Good bye!":
                print(result)
                break
            else:
                print(result)


if __name__ == "__main__":
    assistant = ContactAssistant()
    assistant.main()
