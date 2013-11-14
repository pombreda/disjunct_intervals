#!/usr/bin/env python
from constraint import Problem
import itertools as it

__solvers__ = [
    'CSP',
    'ITER',
]

'''
ints -> intervalls
an interval looks like [x, y] where x is the begining of the interval and y is
the end of the interval
'''


def gen_disjunct_intervals(ints, solver='CSP'):
    result = None
    if not solver in __solvers__:
        raise ValueError(
            'not good solver parameter, you should choice from {!s}'
            .format(__solvers__)
        )
    if solver == 'CSP':
        result = gen_disjunct_intervals_CSP(ints)
    elif solver == 'ITER':
        result = gen_disjunct_intervals_ITER(ints)
    return result


def recurzive_check_of_intersec(solution, from_idx=0):
    unmerged = False
    need_to_recheck = False
    itermap = range(from_idx, len(solution))
    for k in itermap:
        for ko in itermap:
            if k < ko:
                if any(
                    intersec(vi, voi)
                    for vi in solution[k]
                    for voi in solution[ko]
                ):
                    solution[k] += solution[ko]
                    solution[ko] = []
                    need_to_recheck = unmerged
                else:
                    unmerged = True
        if need_to_recheck:
            recurzive_check_of_intersec(solution, k)


def gen_disjunct_intervals_ITER(ints):
    solution = dict(enumerate(([x] for x in ints)))
    recurzive_check_of_intersec(solution)
    return solution


def gen_disjunct_intervals_CSP(ints):
    p = Problem()
    size = len(ints)
    sizeL = range(size)
    for intnum, key in enumerate(ints):
        values = [[]]
        for i in sizeL:
            values += [
                item
                for item in it.combinations(ints, i + 1) if key in item
            ]
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
        sumr = sum(
            [intersec(v[x], v[y])
                for x in range(size)
                for y in range(size)
                if x < y]
        )
        result = sumr >= (size - 1)
    return result


def check_all(v1, v2):
    return all([not intersec(x, y) for x in v1 for y in v2])


def intersec(*args):
    x, y = args
    if (x == y):
        result = True
    elif (not x or not y):
        result = False
    else:
        result = any(
            args[k % 2][0] <= args[(k + 1) % 2][i] <= args[k % 2][1]
            for i in range(2)
            for k in range(2)
        )
    return result
