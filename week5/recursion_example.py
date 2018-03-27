"""
Step through this.

Try to inspect how the arguments to the sum function evolve
"""

def sum(list):
    if len(list) == 1:  # this is the base case
        # we know the answer, so no recursion required
        return list[0]
    else:
        # you can slice lists. They will be super useful for the major project
        return list[0] + sum(list[1:])  # the recursive step


print(sum([5,7,3,8,10]))