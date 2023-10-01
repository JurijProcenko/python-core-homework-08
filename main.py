"""This script manage phonebook
-----------------------------
you can use command below:
add <name> <phone number>    - add new record to the phonebook
change <name> <phone number> - change record into phonebook
phone <name>                 - show phone number for name
show all                     - show all records from phonebook
hello                        - it is just hello :)
exit | close | good bye      - finish the program
help                         - this information
"""

from pathlib import Path


def input_error(func):
    def inner(*args, **kwargs):
        try:
            retcode = func(*args, **kwargs)
        except KeyError:
            retcode = (kwargs, "Unkwown person, try again")
        except ValueError:
            retcode = (kwargs, "The phone number must consist of numbers ONLY!")

        return retcode

    return inner


def normalize(number: str) -> str:
    for i in "+-()":
        number = number.replace(i, "")
    if not number.isdigit():
        raise ValueError
    return number


@input_error
def add_number(person: str, number: str, phone_book: dict) -> tuple:
    phone_book[person] = normalize(number)
    return phone_book, "Abonent added succefully!"


@input_error
def change_number(person: str, number: str, phone_book: dict) -> tuple:
    if person not in phone_book:
        raise KeyError
    phone_book[person] = normalize(number)
    return phone_book, f"Phone number <{person}> changed succefully!"


@input_error
def phone(person: str, **phone_book: dict) -> str:
    return phone_book[person]


# @input_error
# def delete(person: str, **phone_book: dict) -> tuple:
#     del phone_book[person]
#     return phone_book, f"Abonent <{person}> was succefully deleted!"


def show_all(phone_book: dict) -> str:
    return_string = ""
    for key, values in phone_book.items():
        return_string += f"{key}    {values}\n"
    return return_string


def parser(command: str, phone_book: dict, data_pb: Path) -> str:
    if command.startswith("help"):
        return __doc__

    if command.startswith("show all"):
        return show_all(phone_book)

    if command.startswith(("good bye", "close", "exit")):
        with open(data_pb, "w") as pb:
            for k, v in phone_book.items():
                pb.write(f"{k} {v}\n")
        return "Good bye!"

    command = command.lower().split()
    match command[0]:
        case "hello":
            return "How can I help you?"
        case "phone":
            return phone(" ".join(command[1:]), **phone_book)
        case "add":
            retcode = add_number(" ".join(command[1:-1]), command[-1], phone_book)
            phone_book, return_str = retcode
            return return_str
        case "change":
            retcode = change_number(" ".join(command[1:-1]), command[-1], phone_book)
            phone_book, return_str = retcode
            return return_str
        # case "delete":
        #     retcode = delete(" ".join(command[1:]), **phone_book)
        #     phone_book, return_str = retcode
        #     print(phone_book)
        #     return return_str

    return "Command not recognized, try again"


def main():
    data_pb = Path("phonebook.txt")
    phone_book = {}
    if data_pb.exists():
        with open(data_pb, "r") as pb:
            records = pb.readlines()
            for record in records:
                record = record.replace("\n", "").lower().split()
                phone_book[" ".join(record[:-1])] = record[-1]

    while True:
        command = input("Enter your command>> ")
        ret_code = parser(command, phone_book, data_pb)
        if ret_code == "Good bye!":
            print("Good bye!")
            break
        else:
            print(ret_code)


if __name__ == "__main__":
    main()
