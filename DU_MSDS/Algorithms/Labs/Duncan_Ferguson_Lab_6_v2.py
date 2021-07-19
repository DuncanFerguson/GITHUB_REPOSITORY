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
        assert type(elem) == str
        self.hash = self.gethash(elem)
        if self.status[self.hash] == 'empty' or self.status[self.hash] == 'deleted':
            self.status[self.hash], self.table[self.hash] = 'filled', elem
            return
        else:
            while self.status[self.hash] != 'empty' or self.status[self.hash] != 'deleted':
                self.hash += 1
                if self.hash == self.size:
                    self.hash = -1
                elif self.status[self.hash] == 'empty' or self.status[self.hash] == 'deleted':
                    self.status[self.hash], self.table[self.hash] = 'filled', elem
                    return


    def member(self, elem): # Returns if element exists in hashtable
        self.hash = self.gethash(elem)
        if self.status[self.hash] == 'empty':
            return False
        elif self.table[self.hash] == elem:
            return elem
        else:
            while self.status[self.hash] == 'filled' or self.status[self.hash] == 'deleted':
                self.hash += 1
                if self.hash == self.size:
                    self.hash = -1
                if self.status[self.hash] == 'empty':
                    break
                elif self.table[self.hash] == elem:
                    return elem
        return False  # This is assuming that we get a empty slot


    def delete(self, elem):
        """This Function is aimed at deleting a member"""
        self.hash = self.gethash(elem)
        if self.status[self.hash] == 'filled' and self.table[self.hash] == elem:
            self.status[self.hash], self.table[self.hash] = 'deleted', None
        elif self.status[self.hash] == 'empty':
            return "Name Does Not Exist"





def test_code():
    # Testing code
    s = MyHashtable(10)
    # print(s)
    s.insert("amy") #97
    # print("Amy Added", s)
    s.insert("chase") #99
    # print(s)
    s.insert("chris") #99
    s.insert("charles")
    # s.insert("abby")
    # s.insert("Gabrielle")
    print(s)
    # print("Chris Added:", s)
    print(s.member("amy"))
    print(s.member("chase"))
    print(s.member("alyssa"))
    print(s.member("chris"))
    print(s.member("charles"))
    print(s)
    s.delete("chase")
    print(s)
    print(s.member("chris"))
    print(s.member("chase"))
    # You can use print(s) at any time to see the contents
    # of the table for debugging
    #print(s)

def main():
    test_code()

if __name__ == '__main__':
    main()