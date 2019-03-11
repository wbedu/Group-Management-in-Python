class Group:
    __groupCount = 0
    __groups = []

    @classmethod
    def groups(cls):
        return cls.__groups

    def __init__(self):
        self.__set_new_id()
        self.__members = list()
        Group.__groups.append(self)

    def __set_new_id(self):
        Group.__groupCount += 1
        self.__id = Group.__groupCount

    def add_members(self, person):
        if person.uuid() not in [p.uuid() for p in self.__members]:
            person.set_group(True)
            self.__members.append(person)

    def remove_member(self, uuid):
        for person in self.__members:
            if person.uuid() == uuid:
                person.set_group(False)
                self.__members.remove(person)

    def id(self):
        return self.__id

    def members(self):
        return self.__members
