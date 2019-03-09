import Person


class Group:
    __groupCount = 0
    __groups = []

    @classmethod
    def groups(cls):
        return cls.__groups

    def __init__(self):
        self.__set_new_id()
        self.__memberIds = []
        Group.__groups.append(self)

    def __init__(self, members):
        self.__set_new_id()
        self.__memberIds = members
        Group.__groups.append(self)

    def __set_new_id(self):
        Group.__groupCount += 1
        self.__id = Group.__groupCount

    def add_members(self, uuid):
        if uuid not in self.__memberIds:
            self.__memberIds.append(uuid)

    def remove_member(self, uuid):
        if uuid in self.__memberIds:
            self.__memberIds.remove(uuid)

    def members(self):
        return self.__memberIds
