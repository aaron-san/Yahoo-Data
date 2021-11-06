
# Python practice



# import keyword
# keyword.kwlist



import pandas as pd


df = pd.read_csv('combined_stat.csv')

for col in df.columns:
    print(col)
    
# update column names
# combined_sheets.columns = ["Ticker", "Breakdown", "Recent"]


# combined_sheets[combined_sheets.Breakdown == "totalAssets"]
    
# Remove a column 
# del combined_stats["level_1"]
 
# update column names
# combined_stats.columns = ["ticker", "field", "value"]

# Update value
# combined_stats['date'] = today

# type(combined_stats)
# combined_stats.to_csv("combined_stat " + today + ".csv")


# combined_stats.to_feather("sp500_combined_stats " + today + ".ftr")
# sp500_stats = pd.read_feather("sp500_combined_stats.ftr")


# combined_stats[combined_stats.Attribute.str.contains("Trailing P/E") # "Price/Sales", "Price/Book", "PEG", "Forward P/E"









tbl = df.iloc[:, 1:4]
tbl.columns = ["Ticker", "Field", "Value"]

tbl2 = tbl[tbl.Field.str.contains("PEG") | tbl.Ticker.str.contains("AAPL")].iloc[0:10]
tbl2.index
tbl2.reset_index()

# tbl3 = pd.concat(pd.Series([['a', 'b', 'c'], ['d', 'e', 'f']]), pd.Series([[2, 3, 4], [12, 13, 14]]))


x = True
y = False

x and y
x or y
not(not x and y)

isinstance(x, bool)
isinstance(x, int)
isinstance(x, str)
isinstance(x, float)


# tuple: An ordered collection of n values of any type (n >= 0).
#  - immutable
#  - indexable
#  - hashable if all members are hashable
a = (1, 2, 3)
b = ('a', 1, 'python', (1, 2))
b[2] = 'something else' # returns a TypeError


# list: An ordered collection of n values (n >= 0)
#  - mutable
#  - not hashable
a = [1, 2, 3]
b = ['a', 1, 'python', (1, 2), [1, 2]]
b[2] = 'something else' # allowed

# Repeated concatination
a * 3



# set: An unordered collection of distinct elements. 
#  - Items must be hashable
#  - mutable
#  - no index
#  - look like dicts, but with no indexes
a = {1, 2, 'a'}
# add an element to the set
a.add('b')

# Create an empty set
b = set()
b.add(2); b.add('a'); b.add('l')
# Get intersection of two sets
a.intersection(b)
# Get union of two sets
a.union(b)
# Get the set difference
a.difference(b)
# Get the symmetric difference (elements in a or b, but not both)
a.symmetric_difference(b)
# Testing membership
2 in a




# dict: An unordered collection of unique key-value pairs 
#  - keys must be hashable
#  - mutable
a = {1: 'one', 2: 'two'}
b = {'a': [1, 2, 3], 'b': 'a string'}
b.values()

for key in b.keys():
    print(key)

b.keys()

# Intersection
{1, 2, 3, 4, 5}.intersection({3, 4, 5, 6}) # {3, 4, 5}
# or
{1, 2, 3, 4, 5} & {3, 4, 5, 6}

# Difference
{1, 2, 3, 4}.difference({2, 3, 5}) # {1, 4}
# or
{1, 2, 3, 4} - {2, 3, 5} # {1, 4}

# Symmetric difference with (return unique members of each set)
{1, 2, 3, 4}.symmetric_difference({2, 3, 5}) # {1, 4, 5}
# or
{1, 2, 3, 4} ^ {2, 3, 5} 

# Subset check
{1, 2}.issubset({1, 2, 3}) # True
{1, 2} <= {1, 2, 3} # True

# Disjoint check
{1, 2}.isdisjoint({3, 4}) # True
{1, 2}.isdisjoint({1, 4}) # False

# Existence check
2 in {1,2,3} # True
4 in {1,2,3} # False
4 not in {1,2,3} # True

# Add and Remove
s = {1,2,3}
s.add(4) # s == {1,2,3,4}
# Remove element (no error if doesn't exist)
s.discard(3) # s == {1,2,4}
s.discard(5) # s == {1,2,4}
# Remove element (error if doesn't exist)
s.remove(2) # s == {1,4}
s.remove(2) # KeyError!

# Add elements in-place
s = {1, 2}
s.update({3, 4}) # s == {1, 2, 3, 4}




a = None # No value will be assigned. Any valid datatype can be assigned later



# data conversions

a = '123'
int(a)
float(a)
str(a)

a = 'hello'
list(a) # ['h', 'e', 'l', 'l', 'o']
set(a) # {'o', 'e', 'l', 'h'}
tuple(a) # ('h', 'e', 'l', 'l', 'o')



#-----------------------#
# lists
#-----------------------#
a = 'hello'
lst = list(a) # ['h', 'e', 'l', 'l', 'o']
# subset
lst[0:3] # ['h', 'e', 'l']
lst[0::3] # ['h', 'l']



lst.append(123) # in-place mutation
# x list = list.append(123)

# insert element at specified position
lst.insert(1, "Nikki")
# Remove element
lst.remove(123)
# Find index of element
lst.index("Nikki")
# Get length of list
len(lst)
# Count occurrence of any item in list
a = [1, 1, 1, 2, 3, 4]
a.count(1)

# Reverse the list
a.reverse()
# or
a[::-1]

# Remove and return item at index (defaults to the last item) with L.pop([index]), returns the item
lst.pop(2)

# Loop through list
for element in lst:
 print (element)


empty_list = []

mixed_list = [1, 'abc', True, 2.34, None]
nested_list = [['a', 'b', 'c'], [1, 2, 3]]

# Get unique elements of a list (remove duplicates)
set(a) # returns a set
list(set(a)) # get unique elements and return a list





#-----------------------#
# Dictionaries (dicts)
#-----------------------#
state_capitals = {
 'Arkansas': 'Little Rock',
 'Colorado': 'Denver',
 'California': 'Sacramento',
 'Georgia': 'Atlanta'
}

ca_capital = state_capitals['California']

state_capitals.items()
state_capitals.keys()
state_capitals.values()

for k in state_capitals.keys():
 print('{} is the capital of {}'.format(state_capitals[k], k))

for key, value in state_capitals.items():
 print(key, "::", value)




# Get all functions in a module
import math
dir(math)



# Specific functions of a module can be imported.
floor(1.23) # doesn't work
from math import floor
floor(1.23) # works!


# A module can be stand-alone runnable script.
# run_hello.py
# if __name__ == '__main__':
 # from hello import say_hello
 # say_hello()
# Run it!
# $ python run_hello.py
# => "Hello!"



# Math
# Assign multiple variables in one statement
a, b, c, d, e = 3, 2, 2.0, -3, 10

a / b
floor(a/b)
# or 
a // b

import math 
dir(math)
math.factorial(4) # works!
factorial(4) # doesn't work

from math import *
factorial(4) # works!
exp(log(1))
degrees(2*pi)
radians(180) / (2*pi)

3 * 3
# repeated concatination
3 * ('a', 'b')


x = 3.140000001
if 3.14 < x < 3.142:
    print("x is near pi")
else: 
    print("not near pi")


#--------------------#
# Conditionals
#--------------------#
n = 5
"Greater than 2" if n > 2 else "Smaller than or equal to 2"
"Hello" if n > 10 else "Goodbye" if n > 5 else "Good day"




# Truth Values
# The following values are considered falsey, in that they evaluate to False when applied to a boolean operator.

# None, False, 0, or any numerical value equivalent to zero, for example 0L, 0.0, 0j
# Empty sequences: '', "", (), []
# Empty mappings: {}

# All other values in Python evaluate to True.


# The and operator evaluates all expressions and returns the last expression if all expressions evaluate to True.
# Otherwise it returns the first value that evaluates to False:
1 and 2 # 2
1 and 0 # 0
1 and "Hello World" #"Hello World"
"" and "Pancakes" # ""

# The or operator evaluates the expressions left to right and returns the first value that evaluates to True or the last
# value (if none are True).
1 or 2 # 1
None or 1 # 1
0 or [] # []



# == vs. is
# a == b compares the value of a and b.
# a is b will compare the identities of a and b.
a = 'Python is fun!'
b = 'Python is fun!'
a == b # True
a is b # False

a = b
a is b # True
id(a) == id(b)



#---------------------#
# Loops
#---------------------#
i = 0
while i < 7:
    print(i)
    if i == 4:
        print("Breaking from loop")
        break
    i += 1


for i in (0, 1, 2, 3, 4):
    print(i)
    if i == 2:
        break

for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print(i)


def break_loop():
    for i in range(1, 5):
        if (i == 2):
            return(i) # breaks the outer loop too and returns 2 when reached
        print(i) # returns 1 since the outer loop was not broken
    return(5) # return 5 if the prior loops are not exited

break_loop()


for i in range(5):
 print(i)

x = map(lambda e : e.upper(), ['one', 'two', 'three', 'four'])
print(x)






collection = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]

for item in collection:
    i1 = item[0]
    print(i1)
    i2 = item[1]
    print(i2)
    i3 = item[2]
    print(i3)
 

lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

for s in lst:
    print(s[:1])

# get index and element with enumerate()

for idx, s in enumerate(lst):
 print("%s has an index of %d" % (s, idx))

for i in range(2,4):
 print("lst at %d contains %s" % (i, lst[i]))


for s in lst[1::2]:
    print(s)
# or 
for i in range(1, len(lst), 2):
    print(lst[i])




# p. 124/816... Arrays






