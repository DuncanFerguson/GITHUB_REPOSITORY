# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4581
# Assignment: Lab 6
# Date 7/20/2021

"""This Hash Table only takes strings. It  uses open addressing with linear probing.
The Assignment assumes that the hashtable will never fill up and thus you will always find a 'filled location"""


class MyHashtable(object):
    def __init__(self, size):  # Creates an empty hashtable
        self.size = size  # Creating the size of the table
        self.table = [None for _ in range(self.size)]  # Creating a table list
        self.status = ['empty' for _ in range(self.size)]  # Create a status list with empty

    def __str__(self):
        """This prints out both the table and the status"""
        return "table: " + str(self.table) + "\n" + "status:" + str(self.status)

    def gethash(self, elem):
        """This function grabs the desired hash value"""
        return ord(elem[0]) % self.size

    def insert(self, elem):
        """"This function first asserts that what is being entered is a string. It then checks
        to see if the hash spot is empty or deleted. If so it will insert the element. Otherwise it will
        continue to loop through until it finds a empty or deleted spot to be filled """
        assert type(elem) == str  # Only  strings can be inserted into the table
        self.hash = self.gethash(elem)
        if self.status[self.hash] == 'empty' or self.status[self.hash] == 'deleted':
            self.status[self.hash], self.table[self.hash] = 'filled', elem
            return
        else:
            while self.status[self.hash] != 'empty' or self.status[self.hash] != 'deleted':
                self.hash += 1  # Incrementing the hash
                if self.hash >= self.size:  # Looping back through if the hash is too large
                    self.hash = -1  # Since -1 is the same as the last element it will loop through and turn to 0
                elif self.status[self.hash] == 'empty' or self.status[self.hash] == 'deleted':  # Finding open spot
                    self.status[self.hash], self.table[self.hash] = 'filled', elem  # Filling status and table
                    return

    def member(self, elem):  # Returns if element exists in hashtable
        """This function searches to see if there is a member. If the status is empty for the hash
        it returns false. If it is filled or deleted it will continue to search for the elem untill it finds it
        or there is an empty slot"""
        self.hash = self.gethash(elem)
        if self.status[self.hash] == 'empty':
            return False
        elif self.table[self.hash] == elem:
            return True
        else:
            while self.status[self.hash] == 'filled' or self.status[self.hash] == 'deleted':
                self.hash += 1
                if self.hash >= self.size:  # Resetting the loop
                    self.hash = -1  # Since -1 is the same as the last element it will loop through and turn to 0
                elif self.status[self.hash] == 'empty':
                    break
                elif self.table[self.hash] == elem:
                    return True
            return False  # This is assuming that we get a empty slot

    def delete(self, elem):
        """This Function deletes a member if it finds it. Otherwise returns nothing. The implementation is similiar
        to the self.member finding"""
        self.hash = self.gethash(elem)
        if self.status[self.hash] == 'filled' and self.table[self.hash] == elem:
            self.status[self.hash], self.table[self.hash] = 'deleted', None
        elif self.status[self.hash] == 'empty':
            return
        else:
            while self.status[self.hash] == 'filled' or self.status[self.hash] == 'deleted':
                self.hash += 1
                if self.hash >= self.size:  # Reset loop
                    self.hash = -1  # Since -1 is the same as the last element it will loop through and turn to 0
                elif self.status[self.hash] == 'empty':  # Element doesn't exist
                    break
                elif self.table[self.hash] == elem:  # If the element is found delete it
                    self.status[self.hash], self.table[self.hash] = 'deleted', None
                    break
            return


def test_code():
    # Testing code
    s = MyHashtable(10)
    s.insert("amy")  # 97
    s.insert("chase")  # 99
    s.insert("chris")  # 99
    print(s.member("amy"))
    print(s.member("chris"))
    print(s.member("alyssa"))
    s.delete("chase")
    print(s.member("chris"))
    # You can use print(s) at any time to see the contents
    # of the table for debugging
    print(s)


def main():
    test_code()


if __name__ == '__main__':
    main()
