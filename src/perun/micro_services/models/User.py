from perun.micro_services.models.ObjectWithId import ObjectWithId


class User(ObjectWithId):

    id = None
    name = None

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def __str__(self):
        return 'User[id: {}, name:{}]'.format(self.id, self.name)
