class Person:
    __totalPopulation = -1
    __people = []
    __default_attr = {'ID': None, 'firstName': None, "lastName": None, "hasGroup": False}

    @classmethod
    def people(cls):
        return cls.__people

    @classmethod
    def get(cls, uuid):
        if uuid not in range(0, cls.__totalPopulation+1):
            return None
        return cls.__people[uuid]

    def __init__(self, attr):
        Person.__totalPopulation += 1
        self.__attributes = {**Person.__default_attr, **attr, 'ID': Person.__totalPopulation}
        Person.__people.append(self)

    def change_attribute(self, attr_name, attr):
        self.__attributes = {**self.__attributes, attr_name: attr}
        Person.__people[self.uuid()] = self

    def name(self):
        return self.__attributes["firstName"] + " " + self.__attributes["lastName"]

    def uuid(self):
        return self.__attributes["ID"]

    def set_group(self, entry):
        self.__attributes["hasGroup"] = entry
        Person.__people[self.uuid()] = self

    def has_group(self):
        return self.__attributes["hasGroup"]

    def validate(self, attrs):
        if len(attrs) == 0:
            attrs = ["ID", "firstName", "lastName"]
        for attr in attrs:
            if attr not in self.__attributes or self.__attributes[attr] is None:
                print(self.name(), " is missing the attribute: ", attr)
        if not self.__attributes["hasGroup"]:
            print(self.name(), " does not have an assigned group")
