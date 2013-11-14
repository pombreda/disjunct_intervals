disjunct_intervals
==================

Find disjunct intervals sets in an interval list, using CSP (constraint solver problem) or ITER (basic -recursive- iteration).
disjunct_intervals is a module implementing support for handling the problem of find disjunct intervals of list of intervals.
Basically this can return the list of list of intervals from a list of intervals where all the elements are disjunct from the others.

For example:
------------

Intervals of the natural numbers.
Input: [[2, 3], [6, 8], [3, 5]]
Output would be: [[], [[6, 8]], [[2, 3], [3, 5]]]
As you can see this will return the same numbere of set as the input was.

WARNING
-------

This is not fully tested so there could be errors.
In case of the resolver cannot find a solution the result would be None.

This solution using CSPs (Constraint Solving Problems) over finite domains as default.
This means that for high number of intervals this could be very slow, please consider the value domain before use this.

```python
import minints

minints.gen_disjunct_intervals(dates_input) # or minints.gen_disjunct_intervals(dates_input, 'CSP')
```

You can use ITER (basic -recursive- iteration) as well if you define in function call.
This algorithm is better if the intervals' number higher than 10.

```python
import minints

minints.gen_disjunct_intervals(dates_input, 'ITER')
```

HOW TO
------

run tests:
	python -m nose [-v]

install:
	python setup.py install

uninstall:
	pip uninstall dijunct_ints

recommendations:
	- use pip
	- use virtualenv
	- use virtualenvwrapper
	- use nose
	- use stuptools
