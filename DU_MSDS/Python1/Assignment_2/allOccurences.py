def allOccurrences(search_string,target_string):
    ''' This function looks for a target string within a search string and returns the index position _
    of which it occurs in the search string'''
    list = []
    i = 0
    while i <= len(search_string):
        # print(search_string[i:i+len(target_string)])
        if search_string[i:i+len(target_string)] == target_string:
            list.append(i)
        i += 1
    return print(list)

search_string = str(input("Enter the Search String: "))
target_string = str(input("Enter the Target String: "))
allOccurrences(search_string, target_string)
