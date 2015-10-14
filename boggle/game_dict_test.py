# Tests
from game_dict import *

"""SETUP 0"""
file = ['hi']
read(file, 3)

"""TEST 0"""
assert words == []
print("Passed test 0! words =", words)

"""TEARDOWN 0"""
del words
from game_dict import *

"""SETUP 1"""
file = ['hello']
read(file, 3)

"""TEST 1"""
assert words == ['hello']
print("Passed test 1! words =", words)

"""TEARDOWN 1"""
del words
from game_dict import *

"""SETUP 2"""
file = ['in-line']
read(file, 3)

"""TEST 2"""
assert words == ['hello']
print("Passed test 2! words =", words)

"""TEARDOWN 2"""
del words 
from game_dict import *

"""SETUP 3"""
file = ['final']
read(file, 3)

"""TEST 3"""
assert words == ['hello', 'final']
print("Passed test 2! words =", words)

"""TEARDOWN 3"""
del words 