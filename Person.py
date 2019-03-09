class Person:
    __totalPopulation = 0
    __people = []
    __default_attr = {'uuid': None, 'firstName': None, "lastName": None}

    @classmethod
    def people(cls):
        return cls.__people

    def __init__(self):
        Person.__totalPopulation += 1
        self.__attributes = {**Person.__default_attr, "uuid": Person.__totalPopulation}
        Person.__people.append(self)

    def __init__(self, attr):
        Person.__totalPopulation += 1
        self.__attributes = {**Person.__default_attr, **attr}
        Person.__people.append(self)

    def change_attribute(self, attr_name, attr):
        self.__attributes = {**self.__attributes, attr_name: attr}

    def name(self):
        return self.__attributes["firstName"] + " " + self.__attributes["lastName"]

    def uuid(self):
        return self.__attributes["uuid"]
