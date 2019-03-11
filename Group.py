class Group:
    __groupCount = -1
    __groups = []

    @classmethod
    def groups(cls):
        return cls.__groups

    @classmethod
    def get(cls, guid):
        if guid in range(0, cls.__groupCount+1):
            return cls.__groups[guid]
        return None

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
            Group.__groups[self.id()] = self

    def remove_member(self, uuid):
        for person in self.__members:
            if person.uuid() == uuid:
                person.set_group(False)
                self.__members.remove(person)
                Group.__groups[self.id()] = self
            return True
        return False

    def id(self):
        return self.__id

    def members(self):
        return self.__members

    def validate(self):
        for person in self.members():
            person.validate(["firstName", "lastName", "ID"])
        member_count = len(self.__members)
        if member_count < 3:
            print("Group ", self.__id, " has less than 3 members")
        if member_count > 5:
            print("Group ", self.__id, " has more than 5 members")
