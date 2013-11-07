#!/usr/bin/env python
from constraint import *
import itertools as it


def gen_disjunct_intervals(ints):
    p = Problem()
    size = len(ints)
    sizeL = range(size)
    for intnum, key in enumerate(ints):
        values = [[]]
        for i in sizeL:
            values += [item for item in it.combinations(ints, i+1) if key in item]
        p.addVariable(intnum, values)

    for i in sizeL:
        p.addConstraint(check_continuity, (i,))
    for i1, i2 in it.product(sizeL, sizeL):
        if i1 < i2:
            p.addConstraint(check_all, (i1, i2))
    p.addConstraint(all_interval, sizeL)

    return p.getSolution()


def all_interval(*args):
    ''' The number of intervalls is not changed after grouping them.
    '''
    return sum(len(i) for i in args) == len(args)


def check_continuity(v):
    size = len(v)
    if (size < 2):
        result = True
    else:
        sumr = sum([intersec(v[x],v[y]) for x in range(size) for y in range(size) if x < y])
        result = sumr >= (size - 1)
    return result


def check_all(v1, v2):
    return all([not intersec(x,y) for x in v1 for y in v2])


def intersec(*args):
    x, y = args
    if (x == y):
        result = True
    elif (not x or not y):
        result = False
    else:
        result = any(args[k%2][0] <= args[(k+1)%2][i] <= args[k%2][1] for i in range(2) for k in range(2))
    return result
