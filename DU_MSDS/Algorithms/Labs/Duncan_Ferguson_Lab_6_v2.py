# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 6
# Date 7/20/2021

# HashTable ADT with chaining implementation
# This hashtable accepts only strings and hashes based on their
# ASCII value of the first char
# The constructor takes in the size of the table
class MyHashtable(object):
    def __init__(self, size):  # Creates an empty hashtable
        self.size = size
        self.table = [None for _ in range(self.size)]
        self.status = ['empty' for _ in range(self.size)]  # Create the list (of size) of empty lists (chaining)

    def __str__(self):
        return str(self.table) + "\n" + str(self.status)

    def gethash(self, elem):
        return ord(elem[0]) % self.size

    def insert(self, elem):
        self.hash = self.gethash(elem)
        if self.status[self.hash] == 'empty' or self.status[self.hash] == 'deleted':
            self.status[self.hash], self.table[self.hash] = 'filled', elem
        else:
            print("Here is where I need loop")
            while self.status[self.hash] == 'filled':
                if self.size >= self.hash:
                    self.hash = -1
                    print("reset")
                self.hash += 1
                if self.status[self.hash] == 'empty' or self.status[self.hash] == 'deleted':
                    self.status[self.hash], self.table[self.hash] = 'filled', elem
                    print("Adding")
            #     else:
            #         print("ON Continue")
            #         continue


    # def insert(self, elem): # Adds an element into the hashtable
    #     # TODO this is where the meat of the assignment goes down.
    #     hash = ord(elem[0]) % self.size
    #     if self.status[hash] != 'filled':
    #         self.status[hash] = 'filled'
    #         self.table[hash] = elem
    #         # print("Firing", self.status[hash])
    #         return
    #     else:
    #         print("Hash", hash, "Elem", elem)
    #         self.find_open_slot(elem, hash)
    #         # print("Here")

    # def find_open_slot(self, key, index):
    #     """This find's an open slot and inserts the element"""
    #     # print(self.size)
    #     self.index = index + 1  # Increasing the list one to search down the line
    #     self.key = key
    #     # print("Looking where to put in", self.key, "in this index", self.index)
    #     if self.index >= self.size:
    #         self.find_open_slot(self.key, -1)  # Sending it back around with a new index
    #     else:
    #         if self.status[self.index] != 'filled':
    #             self.status[self.index] = 'filled'
    #             self.table[self.index] = self.key
    #             return
    #         else:
    #             self.find_open_slot(self.key, self.index)



    # def member(self, elem): # Returns if element exists in hashtable
    #     hash = ord(elem[0]) % self.size
    #     if self.status[hash] == 'empty':
    #         return
    #     elif self.table[hash] == elem:
    #         return elem
    #     else:
    #         self.search_next_member(elem, hash)
    #         # return

    # def search_next_member(self, elem, hash):
    #     """ Looping through"""
    #     self.elem = elem
    #     self.hash = hash + 1
    #     if self.hash >= self.size:
    #         self.search_next_member(self.elem, -1)
    #     elif self.status[hash] == 'empty':
    #         return
    #     elif self.table[self.hash] == self.elem:
    #         print("Hit")
    #         print(self.elem)
    #     else:
    #         self.search_next_member(self.elem, self.hash)



# Interesting idea changing it around
    # def get_prob_range(self, index):
    #         return [*range(index, len(self.table))] + [*range(0, index)]


    # def delete_member(self, elem):
    #     """This function is meant for deleting """
    #     # TODO make sure to update the status list to deleted
    #     hash = ord(elem[0]) % self.size
    #     return

# def delete(self, elem): # Removes an element from the hashtable
#     hash = ord(elem[0]) % self.size
#     self.table[hash].remove(elem)

def test_code():
    # Testing code
    s = MyHashtable(10)
    # print(s)
    s.insert("amy") #97
    print("Amy Added", s)
    s.insert("chase") #99
    print(s)
    s.insert("chris") #99
    print("Chris Added:", s)
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