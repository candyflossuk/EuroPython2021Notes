"""
Notes from the Introduction to Property-Based Testing session
by Zac Hatfield Dodds (HypoFuzz) from EuroPython 2021
"""

# Nested context managers over multiple lines are shown
with open('file.txt') as fobj_in, \
        open('out.txt', 'w') as fobj_out:
    fobj_out.write(fobj_in.read())

