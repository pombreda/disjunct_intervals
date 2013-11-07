#!/usr/bin/env python
import minints


def test_disjunct_intervals():
	ints = ([1,3], [5,6], [13,16])
	solution = minints.gen_disjunct_intervals(ints)
	for item in solution.values():
		assert len(item) == 1
		assert item[0] in ints


def test_touching_intervals():
	ints = ([2,6], [6,8], [11,14])
	solution = minints.gen_disjunct_intervals(ints)
	for item in solution.values():
		if len(item) > 1:
			assert [2,6] in item
			assert [6,8] in item
		elif len(item) == 1:
			assert [11,14] in item
		else:
			assert item == []


def test_overlapping_intervals():
	ints = ([2,6], [4,8], [11,14])
	solution = minints.gen_disjunct_intervals(ints)
	for item in solution.values():
		if len(item) > 1:
			assert [2,6] in item
			assert [4,8] in item
		elif len(item) == 1:
			assert [11,14] in item
		else:
			assert item == []


def test_mixed_intervals_1():
	ints = ([1,3], [5,9], [13,19], [14, 15], [17,18], [19, 19])
	solution = minints.gen_disjunct_intervals(ints)
	assert len(filter(lambda x: x != [], solution.values())) == 3
	for item in solution.values():
		if len(item) > 1:
			assert [13,19] in item
			assert [14,15] in item
			assert [17,18] in item
			assert [19,19] in item
		elif len(item) == 1:
			assert [1,3] in item or [5,9] in item
		else:
			assert item == []

def test_equal_intervals():
	ints = ([2,6], [2,6], [2,6])
	solution = minints.gen_disjunct_intervals(ints)
	for item in solution.values():
		if len(item) == 3:
			assert all([ i == [2,6] for i in item])
		else:
			assert item == []

def test_equal_intervals_with_dates():
    import datetime
    ints = [[datetime.date(2007, 5, 7), datetime.date(2013, 11, 5)], [datetime.date(2007, 5, 7), datetime.date(2013, 11, 5)]]
    solution = minints.gen_disjunct_intervals(ints)
    for item in solution.values():
        if len(item) == 2:
            assert all([ i == [datetime.date(2007, 5, 7), datetime.date(2013, 11, 5)] for i in item])
        else:   
            assert item == []

        