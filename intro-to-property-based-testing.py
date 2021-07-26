"""
Notes from the Introduction to Property-Based Testing session
by Zac Hatfield Dodds (HypoFuzz) from EuroPython 2021
"""

# Nested context managers over multiple lines are shown
with open('file.txt') as fobj_in, \
        open('out.txt', 'w') as fobj_out:
    fobj_out.write(fobj_in.read())


class C:
    # Example of decorator using static method
    @staticmethod
    def func(self):
        return 42

    # equivalent to the below - where the staticmethod annotation is not used.
    # func = staticmethod(func)


def hello(func):
    # Create a wrapper that prints 'Wrapped' before executing the function
    def wrapper(*args, **kwargs):
        print('Wrapped')
        return func(*args, **kwargs)
    return wrapper


# Parametrized decorator
def say(text):
    def _say(func):
        def __say(*args, **kwargs):
            print(text)
            return func(*args, **kwargs)
        return __say
    return _say


@say('Hello')
@say('Good Morning')
def add(a, b):
    return a + b
