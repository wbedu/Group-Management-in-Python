from Person import Person
from Group import Group

options = list(["-1, end process."])
options.append("0, Output what each number does.")
options.append("1, Create a new Person.")
options.append("2, Create a new group.")
options.append("3, Modify an existing group.")
options.append("4, Validate all existing groups.")
options.append("5, Output each group’s number and members.")


def request_int(req):
    while True:
        try:
            res = int(input(req))
            return res
        except ValueError:
            print("Invalid Entry type")



def print_options():
    print("Options:")
    for option in options:
        print("\n\t", option)


def print_groups():
    for group in Group.groups():
        print("Group ", group.id())
        print("\n\t".join([person.name() for person in group.members()]))


def create_person():
    p_attr = {"firstName": input("Enter Person's first name: "), "lastName": input("Enter Person's last name: ")}
    Person(p_attr)


def print_group_people_with_no_group():
    people = [person for person in Person.people() if not person.has_group()]
    if len(people) == 0:
        print("All users have groups")
    for person in people:
        print(person.uuid(), " ", person.name())


def create_group():
    guid = Group().id()
    while True:
        print_group_people_with_no_group()
        uuid = request_int("Which person would you like to add to the new group?(-1 to finish adding people): ")
        if uuid == -1:
            return
        add_member(guid, uuid)


def add_member(guid, uuid):
    if uuid in [person.uuid() for person in Person.people() if person.has_group()]:
        print("This person already has a group")
        return
    group = Group.get(guid)
    member = Person.get(uuid)
    if group is None or member is None:
        print("Either the group does not exist or the user does not exist")
        return
    group.add_members(member)


def remove_member(guid, uuid):
    group = Group.get(guid)
    if group is None:
        print("The group does not exist")
        return
    if not group.remove_member(uuid):
        print("removing person", uuid, " from group ", guid, " failed")


def modify_group():
    guid = request_int("Which group would you like to modify?")
    group = Group.get(guid)
    if group is None:
        print("There is no group with that id")
        return
    action = input("Would you like to ADD or Remove members?").lower()
    if "add" in action:
        while True:
            print_group_people_with_no_group()
            uuid = request_int("Which person would you like to add? (-1 to finish add people):")
            if uuid is -1:
                return
            add_member(guid, uuid)
    if "remove" in action:
        while True:
            for person in group.members():
                print(person.uuid(), " ", person.name())
            uuid = request_int("Which person would you like to remove? (-1 to finish removing people):")
            if uuid is -1:
                return
            remove_member(guid, uuid)
    else:
        print("Invalid action")


def validate_group():
    for person in Person.people():
        person.validate([])
    for group in Group.groups():
        group.validate()


def main_loop():
    services = {
        0: print_options,
        1: create_person,
        2: create_group,
        3: modify_group,
        4: validate_group,
        5: print_groups
    }
    while True:
        usr_option = request_int("Choose an option: ")
        if usr_option not in range(-1, 6):
            print("Error: invalid input")
        else:
            if usr_option == -1:
                return
            services[usr_option]()


if __name__ == '__main__':
    main_loop()
