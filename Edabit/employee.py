from typing import Union


class Employee:

    def __init__(self, name: str, **kwargs: Union[str, int, list]):

        self.__dict__.update(kwargs)

        for k, v in self.__dict__.items():
            self.__setattr__(k, v)


        name = name.strip()
        try:
            self.name = name.split()[0]
            self.lastname = name.split()[1]
        except IndexError:
            raise IndexError('Invalid name argument.')



emp = Employee('John Doe', race='white', dog='g-shep')

print(emp.race)
print(emp.dog)

