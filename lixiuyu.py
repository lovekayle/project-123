# person.py
class Person:
    """ Class to represent a person
    """
    def __init__(self,name):
        self._name = name
        self._age = 0
    def reset_age(self):
        self._age = 0
    def incr_age(self):
        self._age = self._age + 1
    def get_name(self):
        return self._name
    def __str__(self):
        return "name = '%s', age = %d" % (self._name, self._age)
    def __repr__(self):
        return 'Person(%s)' % str(self)

class Man(Person):
    """ Class to represent a man
    """
    def __init__(self,name):
        self._name = name
        self._age = 20
    def reset_age(self):
        self._age = 20
    def incr_age(self):
        self._age = self._age + 10
    def get_name(self):
        return self._name 
    def __str__(self):
        return "name = '%s', age = %d" % (self._name, self._age)
    def __repr__(self):
        return 'Person(%s)' % str(self)

print('name = %s'% __name__)
if __name__ == '__main__':
    print('This is a main program')
