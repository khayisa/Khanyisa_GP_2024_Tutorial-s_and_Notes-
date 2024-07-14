class Person:
    species = "Homo sapiens"

    @classmethod
    def get_species(cls):
        return cls.species

print(Person.get_species())
