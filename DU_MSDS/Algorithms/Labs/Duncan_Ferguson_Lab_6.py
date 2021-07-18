# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 6
# Date 7/ # TODO # /2021

""""
https://coderbook.com/@marcus/how-to-create-a-hash-table-from-scratch-in-python/
https://www.geeksforgeeks.org/hashing-set-3-open-addressing/
https://www.youtube.com/watch?v=ea8BRGxGmlA
https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/4_HashTable_2_Collisions/Solution/exercise_hash_table_linear_probing.ipynb
https://www.youtube.com/watch?v=54iv1si4YCM
"""


# HashTable ADT with chaining implementation
# This hashtable accepts only strings and hashes based on their
# ASCII value of the first char
# The constructor takes in the size of the table
class MyHashtable(object):
    def __init__(self, size): # Creates an empty hashtable
        self.size = size
        self.table = [[None] for i in range(self.size)]
        self.status = [['empty'] for i in range(self.size)]  # Create the list (of size) of empty lists (chaining)

    def __str__(self):
        return str(self.table)

    def gethash(self, elem):
        return ord(elem[0]) % self.size


    def insert(self, elem): # Adds an element into the hashtable
        # TODO this is where the meat of the assignment goes down.
        hash = ord(elem[0]) % self.size
        if self.status[hash] is not ['filled']:
            self.status[hash][0] = 'filled'
            self.table[hash][0] = elem
            return
        else:
            print("Looping")
            self.insert(hash+1)



    def member(self, elem): # Returns if element exists in hashtable
        hash = ord(elem[0]) % self.size
        return elem in self.table[hash]

    def delete_member(self, elem):
        """This function is meant for deleting """
        return

    def return_status(self):
        return str(self.status)

#
#
# def delete(self, elem): # Removes an element from the hashtable
#     hash = ord(elem[0]) % self.size
#     self.table[hash].remove(elem)

def test_code():
    # Testing code
    s = MyHashtable(10)
    print(s)
    s.insert("amy") #97
    print(s, '\n', s.return_status())
    s.insert("chase") #99
    print(s,'\n', s.return_status())
    s.insert("chris") #99
    print(s, '\n', s.return_status())
    # print(s)
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