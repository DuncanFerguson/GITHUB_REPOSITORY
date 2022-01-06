class TotemPole:

    num_instances = 0

    def __init__(self, animals):
        self.tower = animals
        self.__class__.num_instances += 1

    def __add__(self, other):
        return TotemPole(self.tower + other.tower)

    def __lt__(self, other):
        return len(self.tower) < len(other.tower)

    def __str__(self):
        return "\n".join(self.tower)

    @classmethod
    def get_num_instances(cls):
        return cls.num_instances

first = TotemPole(['bear', 'eagle', 'hummingbird'])
# print(first)

orca = TotemPole(['orca'])
print(first + orca)