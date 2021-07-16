# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 6
# Date 7/ # TODO # /2021

""""
https://coderbook.com/@marcus/how-to-create-a-hash-table-from-scratch-in-python/
"""


# HashTable ADT with chaining implementation
# This hashtable accepts only strings and hashes based on their
# ASCII value of the first char
# The constructor takes in the size of the table
class MyHashtable(object):
    def __init__(self, size): # Creates an empty hashtable
        self.size = size
        # TODO Create the list (of size) of empty lists (chaining)
        self.table = []
        for i in range(self.size):
            print(i)
            self.table.append(['None'])

    def __str__(self):
        return str(self.table)

#
#     def insert(self, elem): # Adds an element into the hashtable
#         hash = ord(elem[0]) % self.size
#         self.table[hash].append(elem)
#
#     def member(self, elem): # Returns if element exists in hashtable
#         hash = ord(elem[0]) % self.size
#         return elem in self.table[hash]
#
# # weneededtomod(%)thehashcode(97)bythetablesize(10)inordertoalwaysproduceanindexthatisinthecorrectrangeforourtable.
#
#
# def delete(self, elem): # Removes an element from the hashtable
#     hash = ord(elem[0]) % self.size
#     self.table[hash].remove(elem)

def test_code():
    # Testing code
    s = MyHashtable(10)
    print(s)
    # s.insert("amy") #97
    # s.insert("chase") #99
    # s.insert("chris") #99
    # print(s.member("amy"))
    # print(s.member("chris"))
    # print(s.member("alyssa"))
    # s.delete("chase")
    # print(s.member("chris"))
    # You can use print(s) at any time to see the contents
    # of the table for debugging
    #print(s)

def main():
    test_code()

if __name__ == '__main__':
    main()