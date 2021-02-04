

class TestCount(unittest.TestCase):



def main():
    """This main function allows the code to be run through the command line. It will also print out the dictionary
    that is returned from search flags in csv format"""
    ## Can search the comand line with set up
    # args = sys.argv[1:]
    # d = searchflags(args)
    deal_game()

## If the name is main. Run the main Function
if __name__ == "__main__":
    main()

if __name__ == '__main__':
    unittest.main()