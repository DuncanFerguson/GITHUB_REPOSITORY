'''The code below is supposed to do a Fahrenheit to Celsius
temperature conversion (subtract 32 then multiply by 5 over 9). However, it is
producing the wrong answer in its current form. Fix the code so it performs the
calculation correctly.'''
f = 72
c = f - 32 * 5 // 9
print(c)

'''What does the following code segment output:'''
score = 80
if score > 90:
    print("A")
elif score < 90 and score > 80:
    print("B")
elif score < 80 and score > 70:
    print("C")
elif score < 70 and score > 60:
    print("D")
else:
    print("F")

'''What does the following code output:'''
def mystery(x, y):
    r = 1
    while y > 0:
        if (y % 2) == 1:
            r = r * x
        y = y // 2
        x = x * x
    return r
m = mystery(2, 5)
print(m)

'''Fill in the missing lines of code to find and output the smallest
value in the list. The given list, a, is there for testing purposes, but your code
should work for any length list with any numbers in it. You may not change my
code.'''
a = [4, 2, 6, 3, 5]
#TODO
for i in range('''TODO'''):
    #TODO
        #TODO
print(a[smallest])

'''What does the following code output:'''
def one(x, b):
    c = []
    for y in b:
        c.append([x,y])
    return c
def two(a, b):
    c = []
    for x in a:
        d = one(x, b)
        c.extend(d)
    return c
print(two([1,2,3],[4,5]))

'''Write a function that takes a list of tuples representing points. 
A point is a pair of numbers representing the x and y coordinates. 
The method should return the distance of the pair of points that have the smallest distance between them.  
Hint: you will want to compare every point to every other point, which often involves a double loop.  
An example call for your :

print(closestDist([(1,2), (4,3), (3,6), (5,7), (0,4)]) # should return 2.236...

You probably want to first write (and test) a distance function 
that takes two point tuples and returns the distance between 
them to use as a helper function.  
Note that Python has a square root function, 
but it is in the math library which you will need to import.  
So you must include the line:

import math

and then you can use the square root function like:

math.sqrt(16)  # returns 4'''

#TODO

'''

Write a function that takes a dictionary as an argument 
and returns a new dictionary with the keys and values inverted 
(keys become values and values become keys). 
You code needs to handle the case where there are duplicate 
values in the original dictionary.  
For example, this dictionary of names to favorite colors:
{'Alice':'red', 'Bob':'blue', 'Susan':'green', 'Dan':'blue'}
'''

#TODO

'''Sets can be used to represent mathematical relations.
  These will be sets of tuples. 
   For example:
r = {(1,2), (2,3), (2,4)}
Relations can have a number of properties.  
For this problem we will focus only on the symmetric 
and transitive properties of relations.
A relation is symmetric when:
For all (a,b) in the relation, (b,a) is also in the relation.
In terms of Python code, the following relation is symmetric:
r = {(1,2), (3,6), (6,3), (2,1)}
but this one is not, since (1,2) is in and (2, 1) is not:
r = {(1,2), (3,6), (6,3)}
A relation is transitive when:
For all (a, b) in the relation, if (b, c) is 
also in the relation, 
then (a, c) must be in the relation.
In terms of Python code, 
the following relation is transitive:
r = {(1,2), (2,3), (1,3)}
but this one is not, 
since (1,2) is in and (2, 3) is in, but (1, 3) is not in:
r = {(1,2), (2,3), (1,4)}
Write two function called isSymRel and isTranRel.  
Each should take a relation, such as one of the Rs above, 
as the only parameter.  
Each should return true if the given relation is 
symmetric or transitive, respectively.  
And return false otherwise.'''

#TODO isSymRel
#TODO isTranRel

'''This problem involves reading in a file of data and 
computing a few statistics on that data.
The first thing you will need to do is to create a file 
of data to read.  
You should call this file "scores.txt" and it should 
have the following information in it.  
Note that there should be a "header" line with the names 
of the exams.  Following this first line, 
there should be 1 line of scores for each student 
taking the class (we will not include the names of 
the students in this problem).  
Try to make the file human readable.  
You may use spaces or tabs (\t) to separate each of 
the entires.  Both spaces and tabs are treated as 
whitespace when we process it later.  
You do not need to create this file from Python 
by having it write data, but can simply just type 
in the data in your text favorite code editor 
(Atom/Notepad/etc -- try to avoid editors like MSWord 
as they often add extra things to the file beyond the data) 
and save it with a .txt extension.

exam1    exam2    final
87             85              90
90             95              89
73             81              85
98             93              94
78             76              82

The next step is to open the file for reading.  
Instead of hard-coding the filename, 
I would like you to ask the user to enter the name of the file.
If they type in an incorrect filename that doesn't exist, 
then you should tell them about the error and repeatedly 
ask them to keep entering the filename until they get it right.

Hints to open the file: You will have to use exception handling.

Once the file is open, it is now time to read it.  
Note that the way we read from files is line by line.  
However, for the statistics we want to compute later 
(things like mean of exam2), we will want our data organized 
by columns, one for each exam.  
For the file above, we want to produce the following list 
of columns:

[['exam1', 87, 90, 73, 98, 78], ['exam2', 85, 95, 81, 93, 76], ['final', 90, 89, 85, 94, 82]]

Hints to turn rows into columns: Since the first line is 
different than the rest of the lines (header info), 
that line will need to be read first and processed separately.  In particular, you should try and create the initial list of exam names [['exam1'], ['exam2'], ['final']].  After your list of lists is created, you can process each of the remaining lines by simply appending the values onto the correct list.  Recall that the string method split() will form a list of elements from a string, splitting it on whitespace.  Your code should work for any number of exams and any number of students scores for those exams.

Lastly, create a function that will print statistics for 
single exam.  That is, you would call it like:
printStats(['exam2', 85, 95, 81, 93, 76])

You will call this function for each of the exams columns.  
The function doesn't return anything, but instead prints out 
the min, max, mean, and median in the following format:

exam2 min: 76
exam2 max: 95
exam2 mean: 86
exam2 median: 85

Hints for printing statistics: You may use the min and max 
functions to find the min and max of a list of scores.  
For mean and median, you will have to import the statistics 
module:

import statistics

And then you can call the functions statistics.mean(someList) 
or statistics.median(someList).

Note that the list being passed to this printing function 
contains the name as the 0th item and the scores as the rest 
of the items.'''

#TODO

'''You are to write a function called recAdd that takes in a 
list of numbers and returns their sum.  
You must write this recursively.  For example:

print(recAdd([3, 2, 1, 6, 3, 8]))   # prints 23'''

#TODO
'''You are to write a function called isPalindrome that 
takes a string as a parameter.  
It should return True is the string is a palindrome and 
False if it isn't.  We wrote this iteratively earlier in 
the course.  For this problem I want you to write it recursively.

You should check your function for "racecar", "noon", 
and "abca".  For example:

isPalindrome("racecar")   # returns True'''

#TODO
