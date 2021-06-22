# Student: Duncan Ferguson
# Student ID: 871-641-260
# Class: COMP-3006-2; Assignment 2: Counting Characters
# Date: 2/4/2021
# Teacher: dalton.crutchfield@du.edu
# TA: sunny.shrestha@du.edu

import count
import string
import unittest

class TestCount(unittest.TestCase):

    def test_no_flasgs(self):
        """This Code tests count.py by reading text.txt with now flags. The returned dictionary should equal
        the test_d"""
        test_d = {"a":2, "b":2, "c":2, "d":2}
        result = count.searchflags(["text.txt"])
        self.assertDictEqual(result,test_d)


    def test_z_flags(self):
        """Testing if the "-z" flag is added. The returned dictionary should equal the test_d. Meaning displaying a
        count for the full alphabet"""
        test_d = {"a":2, "b":2, "c":2,"d":2,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,
                  "q":0,"r": 0,"s":0,"t": 0, "u":0, "v":0, "w":0, "x":0, "y":0, "z": 0}
        result = count.searchflags(["-z", "text.txt"])
        self.assertDictEqual(result,test_d)


    def test_c_flags(self):
        """This tests the c flag it calls upon the txt file """
        test_d = {"A":2, "C":1, "D":1, "b":2, "c":1, "d":1}
        result = count.searchflags(["-c", "text.txt"])
        self.assertDictEqual(result,test_d)


    def test_zc_flags(self):
        """Testing to see if the "-z" flag is returning a dictionary that is both upper and lower case with
        a count of zero in the dictionary"""
        letters = string.ascii_letters
        test_d = {}
        for letter in letters:
            test_d[letter] = 0
        result = count.searchflags(["-cz"])
        self.assertDictEqual(result,test_d)


    def test_l_flag(self):
        """This Tests looks at the l flag and determines if the dictionary reads only the letter that has been asked
        to count"""
        result = count.searchflags(["-l", "a", "text.txt"])
        test_d = {"a": 2}
        self.assertDictEqual(result,test_d)


    def test_lz_flag(self):
        """This tests if there is an l flag and a z flag. Only the -l flag character should return a value and the
        rest of the alphabet will return zeros
        that are a"""
        letters = string.ascii_letters
        letters = letters.lower()
        test_d = {}
        for letter in letters:
            test_d[letter] = 0

        for key,value in test_d.items():
            if key == "a":
                test_d[key] = 2

        result = count.searchflags(["-lz", "a", "text.txt"])
        self.assertDictEqual(result,test_d)


    def test_lc(self):
        """This tests if l and c flags are being tests. So case sensitive counting. """
        test_d = {"A":2}
        result = count.searchflags(["-lc", "A", "text.txt"])
        self.assertDictEqual(result,test_d)


    def test_lzc(self):
        """This tests if there is an 'l','z','c' flag. This runs the tests through my text file which has a letters
        that has A:2. All other upper and lower characters with have 0"""
        letters = string.ascii_letters
        test_d = {}
        for letter in letters:
            test_d[letter] = 0

        for key,value in test_d.items():
            if key == "A":
                test_d[key] = 2

        result = count.searchflags(["-lzc", "A", "text.txt"])
        self.assertDictEqual(result,test_d)


    def test_add_frequencies_remove_case_True(self):
        """This function tests weather or not the add frequences functions does in fact add frequences"""
        test_d = {"a":2, "b":2, "c":2, "d":2}
        blank_d = {}
        testfile = "text.txt"
        remove_case = True
        result =count.add_frequencies(blank_d, testfile, remove_case)
        self.assertDictEqual(result,test_d)


    def test_add_frequencies_remove_case_False(self):
        """This function tests weather or not the add frequences functions does in fact add frequences"""
        test_d = test_d = {"A":2, "C":1, "D":1, "b":2, "c":1, "d":1}
        blank_d = {}
        testfile = "text.txt"
        remove_case = False
        result = count.add_frequencies(blank_d, testfile, remove_case)
        self.assertDictEqual(result,test_d)


    def test_dict_2_csv_format(self):
        """This is testing the transition of a dictionary into a csv format"""
        csv_test_string = "'a',0\n'b',2\n"
        test_d = {"a":0, "b":2}
        result = count.dict_2_csv_format(test_d)
        self.assertEqual(result, csv_test_string)


if __name__ == '__main__':
    unittest.main()

