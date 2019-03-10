from Person import Person
from Group import Group

options = list(["-1, end process."])
options.append("0, Output what each number does.")
options.append("1, Create a new Person.")
options.append("2, Create a new group.")
options.append("3, Modify an existing group.")
options.append("4, Validate all existing groups.")
options.append("5, Output each group’s number and members.")


def print_options():
    print("Options:")
    for option in options:
        print("\n\t", option)


def print_groups():
    groups = Group.groups()
    for group in groups:
        print("Group ID: ", group.__id)
        print("\n\t".join([person.name() for person in Person.people() if person.uuid in group.members()]))


def create_person():
    p_attr = {"firstName": input("Enter Person's first name: "), "lastName": input("Enter Person's last name: ")}
    Person(p_attr)


def print_group_people_with_no_group():
    groups = Group.groups()
    for group in groups:
        print("Group ID: ", group.__id)
        print("\n\t".join([person.name() for person in Person.people() if person.uuid in group.members()]))


def create_group():
    uuids = []
    while True:
        uuid = int(input("Which person would you like to add to the new group?(-1 to finish adding people): "))
        if uuid not in [person.uuid() for person in Person.people()]:
            print("There is no user with that id")


def modify_group():
    Group.print_groups()


def validate_group():
    pass


services = {
    0: print_options,
    1: create_person,
    2: create_group,
    3: modify_group,
    4: validate_group,
    5: print_groups
}


def main_loop():
    while True:
        usr_option = int(input("Choose an option: "))
        if usr_option < -1 or usr_option > 6:
            print("Error: invalid input")
        else:
            if usr_option == -1:
                return
            services[usr_option]()


if __name__ == '__main__':
    main_loop()
