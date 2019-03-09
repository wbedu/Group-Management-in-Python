import Person.Person as Person
import Group.Group as Group

options = ["-1, end process."]
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
    p_attr = {"firstName": input("Enter Person's first name"), "lastName": input("Enter Person's last name")}
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


services = {
    0: exit,
    1: print_options,
    2: create_person,
    3: create_group,
    4: Group.modify_group
}


def main_loop():
    usr_option = int(input("Choose an option: "))
    if usr_option < -1 or usr_option > len(services): #todo set static service length
        print("Error: invalid input")
    else:
        services[usr_option+1]()


if __name__ == '__main__':
    main_loop()
